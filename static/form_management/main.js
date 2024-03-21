document.addEventListener('DOMContentLoaded', () => {

    
    
});

// ================================= Form Creation =================================

document.querySelector(".add-section").onclick = () => {
    console.log("ADD")
}

document.querySelector(".save").onclick = () => {
    const design = [];
    const sections = document.querySelectorAll("section");

    // Get the value of each section of the form by its type, then add it to the design array.
    sections.forEach((section, idx) => {
        type = section.querySelector("select").value
        if (type === "dropdown") {
            choices = [];
            question = section.querySelector(".question").value
            section.querySelectorAll("input.choice").forEach(choice => choices.push(choice.value))
            design.push({
                section: idx + 1,
                type: type,
                question: question,
                options: choices,
            })
        } else if (type === "checkbox") {
            choices = [];
            question = section.querySelector(".question").value
            section.querySelectorAll("input.choice").forEach(choice => choices.push(choice.value))
            design.push({
                section: idx + 1,
                type: type,
                question: question,
                options: choices,
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

const designContainer = document.querySelector(".design-container");

const selectFormType = (elem) => {
    // Get the type of the form section.
    type = elem.value;
    displayDiv = elem.parentNode.querySelector(".display");
    if (type == "dropdown") {
        dropdownHandler(elem);
    } else if (type == "checkbox") {
        checkboxHandler(elem)
    } else if (type == "radio") {
        displayDiv.innerHTML = ("radio selected")
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
    }
}

// =================================================================================