window.onload = function () {

    // document.addEventListener("DOMContentLoaded", function () {
    //     const dropdown = document.getElementById("id_some_field"); // Replace "id_some_field" with the actual ID of your dropdown field
    //     const blankOption = dropdown.querySelector("option[value='']");
    //
    //     if (blankOption) {
    //         blankOption.disabled = true;
    //     }
    // });

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