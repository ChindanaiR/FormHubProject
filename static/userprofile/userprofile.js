// Get all edit buttons
const editButtons = document.querySelectorAll('.edit-button');

// Loop through each edit button
editButtons.forEach(button => {
    // Add click event listener
    button.addEventListener('click', function() {
        // Prompt user to enter new name
        const newName = prompt('Enter new name:');
        if (newName !== null && newName.trim() !== '') {
            // Update the corresponding name based on the button clicked
            const infoDiv = button.parentElement;
            const nameElement = infoDiv.querySelector('h4, h5');
            nameElement.textContent = newName;

            // Send a POST request to '/emails' to send the email
            fetch('/update-user-info', {
              method: 'POST',
              body: JSON.stringify({
                new_name: newName
              })
            })
            .then(response => response.json())
            .then(result => {
              // Log the result
              console.log(result);
              // Once the email is sent, load the user's sent mailbox
              load_mailbox('sent');
            });
        }
    });
});