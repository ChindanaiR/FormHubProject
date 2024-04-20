document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll(".form-card").forEach(form => {
        form.onclick = () => window.location.replace(`/form/${form.dataset.code}`)
    })
    
    
    
    
    // function loadFormImage(formId) {
        
    //     fetch('get_form_image/', {
    //         method:"POST",
    //         body:JSON.stringify({
    //             form_id:formId
    //         })
    //     })
    //     .then(response=>response.json())
    //     .then(data => { 
    //         console.log(data.image_path)
    //         document.getElementById(`form_pic_${formId}`).src = data.image_path;

    //     })
            
    // }

   
    //  document.querySelectorAll(".form-card").forEach(form => {
    //     console.log(form.dataset.code)
    //     loadFormImage(form.dataset.code);    
    // })
    
    


});