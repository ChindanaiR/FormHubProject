const closeForm = () => {
    $("#modal").modal("hide")
    document.querySelector("form.close-form").submit()
}

const sellForm = () => {
    $("#modal").modal("hide")
    document.querySelector("form.sell-form").submit()
}

const closeConfirmation = (event) => {
    event.preventDefault();
    document.querySelector(".modal-title").innerHTML = "Alert!";
    document.querySelector(".modal-body").innerHTML = "Are you sure to close this form?";
    document.querySelector(".confirm").onclick = () => closeForm()
    $("#modal").modal("toggle")
}

const sellConfirmation = (event) => {
    event.preventDefault();
    document.querySelector(".modal-title").innerHTML = "Alert!";
    document.querySelector(".modal-body").innerHTML = "Are you sure to sell this form?";
    document.querySelector(".confirm").onclick = () => sellForm()
    $("#modal").modal("toggle")
}

const closeBtn = document.querySelector(".close-form")
const sellBtn = document.querySelector(".sell-form")
if (closeBtn) document.querySelector(".close-form").addEventListener("submit", closeConfirmation)
if (sellBtn) document.querySelector(".sell-form").addEventListener("submit", sellConfirmation)

const downloadData = document.querySelector(".download-data");
if (downloadData) {
    // Export html table to Excel file.
    downloadData.addEventListener("click", () => {
        const table = document.querySelector("table");
        const rows = table.querySelectorAll("tbody tr");
        const data = [];
    
        const headers = [];
        document.querySelectorAll("th.header").forEach(header => {
            headers.push(header.innerText)
        })
        data.push(headers)

        for (let i = 0; i < rows.length; i++) {
            let row = [], cols = rows[i].querySelectorAll("td");
            for (let j = 0; j < cols.length; j++)
                row.push(cols[j].innerText);
            data.push(row);
        }
    
        const wb = XLSX.utils.book_new();
        const ws = XLSX.utils.aoa_to_sheet(data);
        XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
        const wbout = XLSX.write(wb, {bookType:'xlsx',  type: 'binary'});
    
        function s2ab(s) {
            var buf = new ArrayBuffer(s.length);
            var view = new Uint8Array(buf);
            for (var i=0; i<s.length; i++) view[i] = s.charCodeAt(i) & 0xFF;
            return buf;
        }
    
        var blob = new Blob([s2ab(wbout)],{type:"application/octet-stream"});
        var fileName = document.querySelector(".form-name h3").innerText + ".xlsx";
    
        if (window.navigator.msSaveOrOpenBlob) {
            window.navigator.msSaveBlob(blob, fileName);
        } else {
            var a = document.createElement("a");
            document.body.appendChild(a);
            a.style = "display: none";
            var url = window.URL.createObjectURL(blob);
            a.href = url;
            a.download = fileName;
            a.click();
            window.URL.revokeObjectURL(url);
        }
    });
}