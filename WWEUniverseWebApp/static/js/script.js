window.onload = function () {

    // This code is for the "Run" button on the home page
    // It makes an AJAX request to the Django server to run the script
    // It will reset the database and re-populate it with the pre-determined data
    document.getElementById("runButton").addEventListener("click", function () {
        // Make an AJAX request to your Django server
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "{% url 'run_reset_db' %}", true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                var response = JSON.parse(xhr.responseText);
                if (response.status === "success") {
                    alert("Database reset successfully.");
                } else {
                    alert("Error occurred: " + response.message);
                }
            }
        };
        xhr.send();
    });
};