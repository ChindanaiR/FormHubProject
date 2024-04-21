// Export html table to Excel file.
document.querySelector(".download-data").addEventListener("click", function () {
    const table = document.querySelector("table");
    const rows = table.querySelectorAll("tr");
    console.log("CLICKED")
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
    var fileName = "table.xlsx";

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