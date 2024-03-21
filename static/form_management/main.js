document.addEventListener('DOMContentLoaded', () => {

    
    
});

document.querySelector(".add-section").onclick = () => {
    console.log("ADD")
}
document.querySelector(".save").onclick = () => {
    console.log("SAVE")
    const design = [];
    const sections = document.querySelectorAll("section");
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

const test = (elem) => {
    console.log(elem.parentNode.dataset.section);
    console.log(elem.value);
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

    displayDiv = elem.parentNode.querySelector(".display");
    displayDiv.innerHTML = `
        <div class="card my-2 p-3">
            <input type="text" class="question" placeholder="Untitled Question">
            <ol class="choices">
                <li><input type="text" class="choice"></li>
                <li><input type="text" class="choice"></li>
                <li><input type="text" class="choice"></li>
            </ol>
            <button class="add-choices">Add choices</button>
        </div>
    `
    displayDiv.querySelector(".add-choices").onclick = () => addChoices(elem)
}

const checkboxHandler = (elem) => {
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