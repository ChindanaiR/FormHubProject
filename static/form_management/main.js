document.addEventListener('DOMContentLoaded', () => {

    
    
});

// ================================= Form Creation =================================

document.querySelector(".add-section").onclick = () => {
    console.log("ADD")
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
            <option value="file">Upload file</option>
            <option value="date">Date</option>
            <option value="time">Time</option>
        </select>
        <div class="display"></div>
    `
    sectionContainer.appendChild(section)
}

document.querySelector(".save").onclick = () => {
    const design = [];
    const sections = document.querySelectorAll("section");

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
        } else if (["short", "long", "file", "date", "time"].includes(type)) {
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
    console.log(design)
}


const selectFormType = (elem) => {
    // Get the type of the form section.
    type = elem.value;
    displayDiv = elem.parentNode.querySelector(".display");
    if (type == "dropdown") {
        dropdownHandler(elem);
    } else if (type == "checkbox") {
        checkboxHandler(elem)
    } else if (type == "radio") {
        radioHandler(elem)
    } else if (type == "short") {
        console.log("short")
        shortTextHandler(elem)
    } else if (type == "long") {
        console.log("long")
        longTextHandler(elem)
    } else if (type == "file") {
        console.log("file")
        fileUploadHandler(elem)
    } else if (type == "date") {
        console.log("date")
        dateHandler(elem)
    } else if (type == "time") {
        console.log("time")
        timeHandler(elem)
    }
}

const dropdownHandler = (elem) => {

    // Initialize drowndown section
    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <ol class="choices">
                <li><input type="text" class="choice"></li>
            </ol>
            <button class="add-choices">Add choices</button>
        </div>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}

const checkboxHandler = (elem) => {

    // Initialize checkbox section
    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <div class="choices">
                <div>
                    <input type="checkbox" disabled>
                    <input type="text" class="choice">
                </div>
            </div>
            <button class="add-choices">Add choices</button>
        </div>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}

const radioHandler = (elem) => {

    // Initialize checkbox section
    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <div class="choices">
                <div>
                    <input type="radio" disabled>
                    <input type="text" class="choice">
                </div>
            </div>
            <button class="add-choices">Add choices</button>
        </div>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}

const shortTextHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <input type="text" class="answer my-2 p-1" disabled/>
        </div>
    `
}

const longTextHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <textarea class="answer my-2 p-1" disabled></textarea>
        </div>
    `
}

const fileUploadHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
        <input type="text" class="question" placeholder="Untitled Question">
            <div class="input-group my-3">
                <input type="file" class="form-control answer" id="inputGroupFile03" aria-describedby="inputGroupFileAddon03" aria-label="Upload" disabled>
            </div>
        </div>
    `
}

const dateHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <input type="date" class="answer" />
        </div>
    `
}

const timeHandler = (elem) => {

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <input type="time" class="answer" />
        </div>
    `
}

const addChoices = (elem) => {
    const type = elem.parentNode.querySelector("select").value

    if (type === "dropdown") {
        choice = document.createElement("li")
        choice.innerHTML = `<input type="text" class="choice">`
        elem.parentNode.querySelector("ol").appendChild(choice)
    } else if (type === "checkbox") {
        choice = document.createElement("div")
        choice.innerHTML = `<input type="checkbox" disabled>
                            <input type="text" class="choice">`
        elem.parentNode.querySelector("div.choices").appendChild(choice)
    } else if (type === "radio") {
        choice = document.createElement("div")
        choice.innerHTML = `<input type="radio" disabled>
                            <input type="text" class="choice">`
        elem.parentNode.querySelector("div.choices").appendChild(choice)
    }
}

// =================================================================================