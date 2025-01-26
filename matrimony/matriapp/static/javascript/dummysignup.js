document.querySelector('form').addEventListener('submit', function(event) {
    const userInputs = document.querySelectorAll('input');
    for (let input of userInputs) {
        if (!input.value) {
            alert(`${input.name} is required.`);
            event.preventDefault(); // Prevent form submission
            return; // Exit the function
        }
    }
});