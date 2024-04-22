document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll(".form-card").forEach(form => {
        form.onclick = () => window.location.replace(`/redeem/preview_page/${Number(form.dataset.code)}`)
    })

});