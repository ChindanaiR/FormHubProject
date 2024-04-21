

const buyDataset = (formId) => {
    $("#modal").modal("toggle")
    fetch("buy_dataset/", {
        method: "POST",
        body: JSON.stringify({
            formId: formId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.assign(`/manage/responses/${formId}`)
        }
    })
}

const buyingConfirmation = (formId) => {
    document.querySelector(".modal-title").innerHTML = "Alert!";
    document.querySelector(".modal-body").innerHTML = "Do you want to buy this dataset?";
    document.querySelector(".confirm").onclick = () => buyDataset(formId)
    $("#modal").modal("toggle")
}
