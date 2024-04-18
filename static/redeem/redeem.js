document.addEventListener('DOMContentLoaded', function() {
    //     var redeemButtons = document.querySelectorAll('.redeem-btn');
    //     redeemButtons.forEach(function(redeemButton) {
    //         redeemButton.addEventListener('click', function() {
            
    //         // hide redeemButton
    //         this.style.display = 'none'
    //         const confirmSet = this.parentNode.querySelector('#confirmButtons')
    //         confirmSet.style.display = 'block'; 

    //         // handle cancel button
    //         const cancelButton = this.parentNode.querySelector(".cancel-btn")
    //         cancelButton.addEventListener('click', function() {
                
    //             const parentContainer = this.closest('.card-body');
    //             const redeemButton = parentContainer.querySelector('.redeem-btn');

    //             // Now you can access the redeem button and perform actions
    //             console.log(redeemButton);
                
    //             // result
    //             redeemButton.style.display = 'block'
    //             confirmSet.style.display = 'none'

    //             // handle redeem (confirm) button -> hide the whole card
    //             const confirmButton = this.parentNode.querySelector(".confirm-btn")
    //             confirmButton.addEventListener('click', function() {
    //                 const redeemCard = this.closest('.card');
    //                 redeemCard.style.display = 'none'
                    
    //             })
    //         })
    //     })
    // })

 //ถึงอันนี้
    //  // เลือกทุกปุ่ม Redeem โดยใช้คลาส 'redeem-btn'
    //  const redeemButtons = document.querySelectorAll('#test_btn');

    //  // วนลูปผ่านทุกปุ่ม Redeem เพื่อเพิ่มอีเวนต์ที่ใช้ในการคลิก
    //  redeemButtons.forEach(function(button) {
    //     const parentElement = button.parentNode;
    //     const redeemBtn = parentElement.querySelector("#redeem_btn");
    //     const cancelBtn = parentElement.querySelector("#cancel_btn")
    //     const confirmBtn = parentElement.querySelector("#confirm_btn");

    //     if (redeemBtn) {
    //         redeemBtn.onclick = function () {
    //             redeemBtn.style.display = "none";
    //             cancelBtn.style.display = "block";
    //             confirmBtn.style.display = "block"
    //         }
    //     }

    //     if (cancelBtn) {
    //         cancelBtn.onclick = function () {
    //             redeemBtn.style.display = "block";
    //             cancelBtn.style.display = "none";
    //             confirmBtn.style.display = "none"
    //         }
    //     }

    //     if (confirmBtn) {
    //         confirmBtn.onclick = function () {
    //             redeemBtn.style.display = "none";
    //             cancelBtn.style.display = "none";
    //             confirmBtn.style.display = "none"
    //             console.log(confirmBtn.name)
                
    //             fetch(`redeem/${confirmBtn.name}`)
    //             .then(response => {
    //                 console.log(response)
    //                 // console.log(id_find.name)
    //                 return response.json();
    //             })
    //         }
    //     }
 
       
    //      });

    //ถึงอันนี้


     // เลือกทุกปุ่ม Redeem โดยใช้คลาส 'redeem-btn'
     const redeemButtons = document.querySelectorAll('#confirm');

     // วนลูปผ่านทุกปุ่ม Redeem เพื่อเพิ่มอีเวนต์ที่ใช้ในการคลิก
     redeemButtons.forEach(function(button) {
        const parentElement = button.parentNode;
        const redeemBtn = parentElement.querySelector("#redeem_btn");
        
        if (redeemBtn) {
            redeemBtn.onclick = function () {
                
                
                
                var confirmation = confirm("คุณต้องการแลกของรางวัลนี้ใช่หรือไม่?");
                if (confirmation) {
                    alert("แลกของรางวัลสำเร็จ!")
                    fetch(`redeem/${redeemBtn.name}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log(data.alert); // แสดงข้อความที่ได้รับจาก JSON ที่ได้รับมา
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                }
                if (redeemBtn.value == 'CSH'){
                }
                else {
                    parentElement.style.display="none"
                }
                    
            }
        }
    });
     });
