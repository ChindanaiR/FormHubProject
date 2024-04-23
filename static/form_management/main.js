var errorDict = {
    1: "Form name must be added.",
    2: "You have to tell a bit about your form.",
    3: "You have to choose the section type.",
    4: "You have to title you question or terminate the question section.",
    5: "You need at least one choice.",
};

// ================================= Form Creation =================================

document.querySelector(".add-section").onclick = () => {
    const sectionContainer = document.querySelector(".design-container");
    const section = document.createElement("section")
    section.classList.add("card", "p-3", "my-3")
    section.setAttribute("data-section", sectionContainer.childElementCount + 1)
    section.innerHTML = `
        <select name="section-type" class="form-select" onchange="selectFormType(this)">
            <option value="" disabled selected>Select Section Type</option>
            <option value="checkbox">Checkbox</option>
            <option value="dropdown">Dropdown</option>
            <option value="radio">Radio</option>
            <option value="short">Short text</option>
            <option value="long">Long Text</option>
            <option value="date">Date</option>
            <option value="time">Time</option>
        </select>
        <div class="display"></div>
    `
    sectionContainer.appendChild(section)
}

// Bind with the save button
document.querySelector(".save").onclick = () => {
    const validateResult = validateForm();
    const confirmBtn = document.querySelector(".confirm");
    if (validateResult.isValid) {
        document.querySelector(".modal-title").innerHTML = "Notice";
        document.querySelector(".modal-body").innerHTML = "Do you want to publish this form?";
        confirmBtn.classList.remove("hidden")
        confirmBtn.onclick = () => publishForm();
        $("#modal").modal("toggle");
    } else {
        document.querySelector(".modal-title").innerHTML = "Something went wrong.";
        document.querySelector(".modal-body").innerHTML = `<ul class="errors"></ul>`
        confirmBtn.classList.add("hidden")
        const errorList = document.querySelector(".errors");
        validateResult.errors.forEach(err => {
            const error = document.createElement("li");
            error.innerHTML = errorDict[err];
            errorList.appendChild(error)
        })
        $("#modal").modal("toggle");
    }
}

const publishForm = () => {

    const form = getFormDesign()

    fetch("save_form/", {
        method: "POST",
        body: JSON.stringify(form),
    })
    .then(response => response.json())
    .then(response => {
        if (response.msg === "Save successfuly") {
            const formId = response.formId
            const uploaded = uploadFile(formId);
            if (!uploaded) {
                document.querySelector(".modal-title").innerHTML = "Something went wrong.";
                confirmBtn.classList.add("hidden");
                $("#modal").modal("toggle");
            } else {
                window.location.assign("/") 
            }
        } else {
            document.querySelector(".modal-title").innerHTML = "Something went wrong.";
            confirmBtn.classList.add("hidden");
            $("#modal").modal("toggle");
        }
    })

}


const validateForm = () => {
    const errLog = new Set();
    
    // Validate form name; form name is a must
    const formName = document.querySelector(".form-name");
    if (!formName.value) {
        errLog.add(1)
        formName.classList.add("error")
    } else {
        formName.classList.remove("error")
    }

    // Validate form description;
    const description = document.querySelector(".form-descr");
    if (!description.value) {
        errLog.add(2)
        description.classList.add("error")
    } else {
        description.classList.remove("error")
    }

    // The form must have at least one section/question.
    const allSections = document.querySelectorAll("section");
    allSections.forEach((section,) => {
        
        const formType = section.querySelector(".form-select");
        // firstly, check if the .user choose the form type or not
        if (!formType.value) {
            errLog.add(3)
            formType.classList.add("error")
        } else {
            formType.classList.remove("error")
            const question = section.querySelector(".question");
            // if user have selected the type. then check if the user title the question.
            if (!question.value) {
                errLog.add(4)
                question.classList.add("error")
            } else {
                question.classList.remove("error")
                // if the user have titled the question, then check if the user have set the first choice, in case that form type is one from checkbox, radio, dropdown
                const choices = section.querySelectorAll(".choice");
                if (["checkbox", "dropdown", "radio"].includes(formType.value)) {
                    let filledChoices = 0;
                    choices.forEach(choice => {
                        if (choice.value) filledChoices++;
                    })
                    // check if the blank choices has been created and there are no filled choice, mean that there are zero choice for answering.
                    if (filledChoices === 0) {
                        errLog.add(5);
                        choices.forEach(choice => choice.classList.add("error"))
                    } else {
                        choices.forEach(choice => choice.classList.remove("error"))
                    }
                } else {
                    choices.forEach(choice => choice.classList.remove("error"));
                }
            }
        }
    })
    
    // Return the boolean values of true or false
    if (errLog.size === 0) return { isValid: true }
    else return { isValid: false, errors: errLog }
}


const getFormDesign = () => {
    const design = [];
    const sections = document.querySelectorAll("section");
    const formName = document.querySelector(".form-name").value;
    const formDescription = document.querySelector(".form-descr").value;

    // Get the value of each section of the form by its type, then add it to the design array.
    sections.forEach((section, idx) => {
        type = section.querySelector("select").value
        if (["dropdown", "checkbox", "radio"].includes(type)) {
            choices = [];
            question = section.querySelector(".question").value
            section.querySelectorAll("input.choice").forEach(choice => choices.push(choice.value))
            design.push({
                section: idx + 1,
                type: type,
                question: question,
                options: choices,
            })
        } else if (["short", "long", "date", "time"].includes(type)) {
            question = section.querySelector(".question").value
            design.push({
                section: idx + 1,
                type: type,
                question: question,
            })
        } else {
            design.push({
                section: idx + 1,
                type: type,
                remark: "others"
            })
        }
    })

    return {
        formName: formName,
        description: formDescription,
        design: design
    }
}


const selectFormType = (elem) => {
    // Get the type of the form section.
    type = elem.value;
    displayDiv = elem.parentNode.querySelector(".display");
    if (type == "dropdown") dropdownHandler(elem);
    else if (type == "checkbox") checkboxHandler(elem)
    else if (type == "radio") radioHandler(elem)
    else if (type == "short") shortTextHandler(elem)
    else if (type == "long") longTextHandler(elem)
    else if (type == "date") dateHandler(elem)
    else if (type == "time") timeHandler(elem)
}


const dropdownHandler = (elem) => {

    // Initialize drowndown section
    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <ol class="choices my-3">
            <li class="my-1"><input type="text" class="choice"></li>
        </ol>
        <button class="add-choices btn btn-secondary">Add choices</button>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}


const checkboxHandler = (elem) => {

    // Initialize checkbox section
    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <div class="choices my-3">
            <div class="my-1">
                <input type="checkbox" class="form-check-input" disabled>
                <input type="text" class="choice">
            </div>
        </div>
        <button class="add-choices btn btn-secondary">Add choices</button>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}


const radioHandler = (elem) => {

    // Initialize checkbox section
    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <div class="choices my-3">
            <div class="my-1">
                <input type="radio" class="form-check-input" disabled>
                <input type="text" class="choice">
            </div>
        </div>
        <button class="add-choices btn btn-secondary">Add choices</button>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}


const shortTextHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <input type="text" class="answer my-2 p-1" disabled/>
    `
}


const longTextHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <textarea class="answer my-2 p-1" disabled></textarea>
    `
}


const dateHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <input type="date" class="answer form-control my-3" disabled/>
    `
}


const timeHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <input type="text" class="question form-control mt-3" placeholder="Untitled Question">
        <input type="time" class="answer form-control my-3" disabled/>
    `
}


const addChoices = (elem) => {
    const type = elem.parentNode.querySelector("select").value

    if (type === "dropdown") {
        choice = document.createElement("li")
        choice.classList.add("my-1")
        choice.innerHTML = `<input type="text" class="choice"> <i class="delete" onclick="deleteChoice(this)">&times;</i>`
        elem.parentNode.querySelector("ol").appendChild(choice)
    } else if (type === "checkbox") {
        choice = document.createElement("div")
        choice.classList.add("my-1")
        choice.innerHTML = `<input type="checkbox" class="form-check-input" disabled>
                            <input type="text" class="choice"> <i class="delete" onclick="deleteChoice(this)">&times;</i>`
        elem.parentNode.querySelector("div.choices").appendChild(choice)
    } else if (type === "radio") {
        choice = document.createElement("div")
        choice.classList.add("my-1")
        choice.innerHTML = `<input type="radio" class="form-check-input" disabled>
                            <input type="text" class="choice"> <i class="delete" onclick="deleteChoice(this)">&times;</i>`
        elem.parentNode.querySelector("div.choices").appendChild(choice)
    }
}

const deleteChoice = (elem) => {
    elem.parentNode.remove();
}

const uploadFile = (formId) => {
    const img = document.querySelector("#fileupload").files[0];

    if (!img) return true; // Mean that user are not upload photo, so we don't need to upload any photo
    
    const formData = new FormData();
    formData.append("img", img);
    formData.append("formId", formId); // เพิ่ม formId ลงใน FormData

    return fetch("upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(response => {
        if (response.msg === "success") return true;
        else return false;
    });
}


// =================================================================================