document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll(".form").forEach(form => {
        form.onclick = () => window.location.replace(`/form/${form.dataset.code}`)
    })
    
});
