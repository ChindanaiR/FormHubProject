
//Show ในหน้า userprofile
  fetch(`get_userinfo`, {  
    method: "GET",
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    const nameElement = document.querySelector('#acct_name');
    const emailElement = document.querySelector('#email');
    nameElement.textContent = `Username : ${data.name}`;
    emailElement.textContent = `Email : ${data.email}`;
  })

  
  //ปุ่ม Edit Name
  const editButtons = document.getElementById('edit-acct-name');
editButtons.addEventListener('click', function() {
    // Prompt user to enter new name
    const newName = prompt('Enter new name:');
    if (newName !== null && newName.trim() !== '') {
        console.log(newName);
        fetch(`update_userinfo`, {
            method: 'PUT',
            body: JSON.stringify({
                username: newName
            })
        }).then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('username already exists');
        }).then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                const nameElement = document.querySelector('#acct_name');
                nameElement.textContent = `Username : ${newName}`;
            }
        }).catch(error => {
            alert(error.message);
        });
    }
});
            
            
            

  //ปุ่ม Edit mail
  const editmailButtons = document.getElementById('edit-mail');
  editmailButtons.addEventListener('click', function() {
            // Prompt user to enter new name
            const newmail = prompt('Enter new email:');
            if (newmail !== null && newmail.trim() !== ''){
            console.log(newmail)
            fetch(`update_userinfo`, {  //ส่งค่าไปยัง views.py
              method: 'PUT',
              body: JSON.stringify({
                  email: newmail
              })
            }).then(response => {
              if (response.ok) {
                  return response.json();
              }
              throw new Error('Email already exists');
          }).then(data => {
              if (data.error) {
                  alert(data.error);
              } else {
                  const nameElement = document.querySelector('#acct_name');
                  nameElement.textContent = `Email : ${newmail}`;
              }
          }).catch(error => {
              alert(error.message);
          });
      }
  });
            
  


  