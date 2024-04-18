document.addEventListener('DOMContentLoaded', function() {

     // เลือกทุกปุ่ม Redeem โดยใช้คลาส 'redeem-btn'
    const redeemButtons = document.querySelectorAll('#confirm');
    
     // วนลูปผ่านทุกปุ่ม Redeem เพื่อเพิ่มอีเวนต์ที่ใช้ในการคลิก
    redeemButtons.forEach(function(button) {
        const parentElement = button.parentNode;
        const redeemBtn = parentElement.querySelector("#redeem_btn");

        if (redeemBtn) {
            redeemBtn.onclick = function () {
                console.log(redeemBtn.name)
                

                fetch('check_point/', {
                    method:"POST",
                    body:JSON.stringify({
                        redeem_id:redeemBtn.name
                    })
                })
                    .then(response=>response.json())
                    .then(data => { console.log(data.msg)
                    
            if(data.msg==='pass_check'){  
                var confirmation = confirm("คุณต้องการแลกของรางวัลนี้ใช่หรือไม่?");
                if (confirmation) {
                    alert("แลกของรางวัลสำเร็จ!")
                    fetch(`redeem/${redeemBtn.name}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log(data.alert);
                        show_point(); 
                                    
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
            else {
                alert(`ไอโง่`)
            }
            });      
            }
        }
    });

    const display_point = document.querySelector('#display_point');
    function show_point(){
    fetch('get_point/')
    .then(response=>response.json())
    .then(data => {
        display_point.textContent = data.total_point.toLocaleString();
    });
    }

});
