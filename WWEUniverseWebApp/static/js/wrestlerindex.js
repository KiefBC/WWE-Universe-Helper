window.onload = function () {
        // This will add a onkeyup to our input id wrestlerIndexSearch
        function wrestlerIndexSearch() {
            // Declare variables
            var input, filter, table, tr, td, i, txtValue;
            input = document.getElementById("wrestlerIndexSearch");
            filter = input.value.toUpperCase();
            table = document.getElementById("wrestlerIndexTable");
            tr = table.getElementsByTagName("tr");

            // Loop through all table rows, and hide those who don't match the search query
            for (i = 1; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[0];
                if (td) {
                    txtValue = td.textContent || td.innerText;

                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";

                    }
                }
            }
        }

        // This will add a onclick to our th elements in our table id wrestlerIndexTable
        function addOnClickToTH() {
            // Get the table element by its ID
            const table = document.getElementById('wrestlerIndexTable');

            // If the table doesn't exist, log an error and return
            if (!table) {
                console.error('Table with ID "wrestlerIndexTable" not found.');
                return;
            }

            // Get all the th elements within the table's thead
            const thElements = table.querySelectorAll('thead th');

            // Loop through the th elements and add the onclick attribute
            thElements.forEach((th, index) => {
                th.setAttribute('onclick', `sortTable(${index})`);
            });
        }

        function sortTable(n) {
            // This function will sort the table by the column that is clicked
            var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
            table = document.getElementById("wrestlerIndexTable");
            // Set the sorting direction to ascending:
            switching = true;
            dir = "asc";
            // Make a loop that will continue until no switching has been done:
            while (switching) {
                switching = false;
                rows = table.rows;
                for (i = 1; i < (rows.length - 1); i++) {
                    // Start by saying there should be no switching:
                    // Get the two elements you want to compare, one from current row and one from the next:
                    shouldSwitch = false;
                    x = rows[i].getElementsByTagName("TD")[n];
                    y = rows[i + 1].getElementsByTagName("TD")[n];
                    // Check if the two rows should switch place, based on the direction, asc or desc:
                    if (dir === "asc") {
                        if (isNaN(x.innerHTML) ? x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase() : parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    } else if (dir === "desc") {
                        if (isNaN(x.innerHTML) ? x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase() : parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                }
                // If a switch has been marked, make the switch and mark that a switch has been done:
                if (shouldSwitch) {
                    rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                    switching = true;
                    switchcount++;
                } else {
                    if (switchcount === 0 && dir === "asc") {
                        dir = "desc";
                        switching = true;
                    }
                }
            }
        }

        addOnClickToTH();
}