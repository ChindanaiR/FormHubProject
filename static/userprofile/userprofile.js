
document.addEventListener('DOMContentLoaded', () => {

  document.querySelectorAll(".form-card").forEach(form => {
    form.onclick = () => window.location.replace(`/manage/responses/${form.dataset.code}`)
  })

});


  //ปุ่ม Edit Name
  const editButtons = document.getElementById('edit-acct-name');
editButtons.addEventListener('click', function() {
    // Prompt user to enter new name
    const newName = prompt('Enter new name:');
    if (newName !== null && newName.trim() !== '') {
        fetch(`update_userinfo`, {
            method: 'PUT',
            body: JSON.stringify({
                username: newName
            })
        }).then(response => {     //จะแจ้งเตือนหากมีซ้ำ
            if (response.ok) {
                return response.json();
            }
            throw new Error('username already exists');
        }).then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                const nameElement = document.querySelector('#acct_name');
                nameElement.textContent = `Username: ${newName}`;
            }
        }).catch(error => {
          alert(error.message)
        });
        }
    }
);

  //ปุ่ม Edit mail
  const editmailButtons = document.getElementById('edit-mail');
  editmailButtons.addEventListener('click', function() {
            // Prompt user to enter new name
            const newmail = prompt('Enter new email:');
            if (newmail !== null && newmail.trim() !== ''){
            fetch(`update_userinfo`, {  //ส่งค่าไปยัง views.py
              method: 'PUT',
              body: JSON.stringify({
                  email: newmail
              })
            }).then(response => response.json())
            .then(data => {
              alert(data.error)
            })
        
          
      }
  });


const getPic = () => {
  fetch("api/getpic", {
      method: "GET"
  })
  .then(response => response.json())
  .then(resp => {
      const img = document.querySelector("#prof-pic")
      img.src = "/" + resp.img
  })
}


const uploadFile = () => {
  const img = document.querySelector("#fileupload").files[0];

  const formData = new FormData();
  formData.append("img", img);
  
  fetch("api/upload", {
      method: "POST",
      body: formData,
  })
  .then(response => response.json())
  .then(() => {
    location.reload();
  });
}
