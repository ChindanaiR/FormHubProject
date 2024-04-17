document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll(".form-card").forEach(form => {
        form.onclick = () => window.location.replace(`responses/${form.dataset.code}`)
    })
    
});