document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#logout').addEventListener('click', () => {
        alert("You Has Successfully Logged Out. See You Next Time! 🥹");
    });
});

// Wait for page to load
document.addEventListener('DOMContentLoaded', function() {

    // Get reference to the submit button
    var submitButton = document.querySelector('#submit');
    submitButton.disabled = true;
  
    // Function to check if all input fields are filled
    function checkInputs() {
      // Get all input fields within the form
      var inputFields = document.querySelectorAll('.form-control');
      var allFilled = true;
  
      // Loop through each input field
      inputFields.forEach(function(input) {
        if (input.value.trim().length === 0) {
          allFilled = false;
        }
      });
  
      // Enable or disable the submit button based on whether all input fields are filled
      submitButton.disabled = !allFilled;
    }
  
    // Add event listeners to all input fields to trigger checkInputs function on input change
    var inputFields = document.querySelectorAll('.form-control');
    inputFields.forEach(function(input) {
      input.addEventListener('input', checkInputs);
    });
  });
  
function validatePassword() {
    const enterpw = document.querySelector('#password').value;
    const confirmpw = document.querySelector('#confirmation').value;

    if (enterpw !== confirmpw) {
      alert("Passwords do not match!");
      return false;
    } else {
      return true;
    }
    document.querySelector('form').submit()
}