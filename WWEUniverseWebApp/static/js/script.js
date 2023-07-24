window.onload = function () {

    document.addEventListener("DOMContentLoaded", function () {
        const dropdown = document.getElementById("id_some_field"); // Replace "id_some_field" with the actual ID of your dropdown field
        const blankOption = dropdown.querySelector("option[value='']");

        if (blankOption) {
            blankOption.disabled = true;
        }
    });
}