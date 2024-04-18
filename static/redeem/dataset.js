

function buyDataset(formId)  {
    console.log("clicked")
    console.log(formId)

    fetch("buy_dataset/", {
        method: "POST",
        body: JSON.stringify({
            formId: formId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.assign("/redeem")
        }
    })
}