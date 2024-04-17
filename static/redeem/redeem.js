document.addEventListener('DOMContentLoaded', function() {
        var redeemButtons = document.querySelectorAll('.redeem-btn');
        redeemButtons.forEach(function(redeemButton) {
            redeemButton.addEventListener('click', function() {
            
            // hide redeemButton
            this.style.display = 'none'
            const confirmSet = this.parentNode.querySelector('#confirmButtons')
            confirmSet.style.display = 'block'; 

            // handle cancel button
            const cancelButton = this.parentNode.querySelector(".cancel-btn")
            cancelButton.addEventListener('click', function() {
                
                const parentContainer = this.closest('.card-body');
                const redeemButton = parentContainer.querySelector('.redeem-btn');

                // Now you can access the redeem button and perform actions
                console.log(redeemButton);
                
                // result
                redeemButton.style.display = 'block'
                confirmSet.style.display = 'none'

                // handle redeem (confirm) button -> hide the whole card
                const confirmButton = this.parentNode.querySelector(".confirm-btn")
                confirmButton.addEventListener('click', function() {
                    const redeemCard = this.closest('.card');
                    redeemCard.style.display = 'none'
                    
                })
            })
        })
    })
});