// =========================================== Render the form ===========================================

const dropdownRender = (parent, section, design) => {
    console.log("dropdown detected")

    // set initial layout
    section.innerHTML = `
        <h6 class="question">${design.section}. ${design.question}</h6>
        <select class="choices form-control">
            <option value="" disabled selected>Select one</option>
        </select>
    `

    // get the "select" tag to append the options into it
    choiceContainer = section.querySelector(".choices")
    design.options.forEach((option, idx) => {
        choice = document.createElement("option")
        choice.setAttribute("value", option)
        choice.innerHTML = option;
        choiceContainer.appendChild(choice)
    })

    // append the completed section to the form div.
    parent.appendChild(section)
    
}
const checkboxRender = (parent, section, design) => {
    console.log("checkbox detected")

    // set initial layout
    section.innerHTML = `
        <h6 class="question">${design.section}. ${design.question}</h6>
        <div class="checkboxes"></div>
    `

    choiceContainer = section.querySelector(".checkboxes");
    design.options.forEach((option, idx) => {
        choice = document.createElement("div")
        choice.classList.add("checkbox")

        checkbox = document.createElement("input")
        checkbox.setAttribute("type", "checkbox")
        checkbox.setAttribute("name", option)
        checkbox.classList.add("me-2")

        label = document.createElement("label")
        label.innerHTML = option;

        choice.appendChild(checkbox)
        choice.appendChild(label)
        choiceContainer.appendChild(choice)
    })

    parent.appendChild(section)
}


const getData = () => {
    fetch("/api/get_form_data/", {
        method: "GET",
    })
    .then(response => response.json())
    .then(data => {
        const formName = data.formName
        const sections = data.design

        document.querySelector(".form-name").innerHTML = formName;

        sections.forEach((sectionDesign, idx) => {
            // get parent form element
            const formDiv = document.querySelector(".form");

            // create section for the form, and initialize the class
            const section = document.createElement("div");
            section.classList.add("card", "my-3", "p-3", "section")
            section.setAttribute("data-sectionnum", idx + 1)
            
            // checking the form type then call the right renderer.
            type = sectionDesign.type
            section.setAttribute("data-formtype", type) // set the formtype
            if (type == "dropdown") dropdownRender(formDiv, section, sectionDesign)
            else if (type == "checkbox") checkboxRender(formDiv, section, sectionDesign)
        })

    })
}

getData()

// =========================================== Saving response ===========================================

const getAnswer = () => {

}

const saveResponse = () => {
    const responses = [];
    document.querySelectorAll(".section").forEach((section) => {
        formType = section.dataset.formtype;
        const question = /\s(.+)/.exec(section.querySelector(".question").textContent)[1]
        const sectionNumber = section.dataset.sectionnum;
        if (formType === "dropdown") {
            console.log("DD")
            responses.push({
                section: sectionNumber,
                type: formType,
                response: section.querySelector("select").value,
            })
        } else if (formType === "checkbox") {
            console.log("CB")
            checkedEntry = [];
            section.querySelectorAll(".checkbox").forEach(item => {
                checkbox = item.querySelector("input")
                if (checkbox.checked) checkedEntry.push(checkbox.name)
            })
            responses.push({
                section: sectionNumber,
                type: formType,
                response: checkedEntry
            })
        }
        console.log(responses)
    })
}