function populateRoles() {
    document.addEventListener("DOMContentLoaded", function () {
        const teamField = document.getElementById("id_team");
        const roleField = document.getElementById("id_role");

        teamField.addEventListener("change", function () {
            const selectedTeam = teamField.value;
            roleField.innerHTML = "";  // Clear existing options

            let defaultOption = document.createElement("option");
            defaultOption.value = "";
            defaultOption.textContent = "Select a role";
            roleField.appendChild(defaultOption);

            if (selectedTeam) {
                fetch(`get_roles/?team=${selectedTeam}`)
                    .then(response => response.json())
                    .then(data => {
                        data.roles.forEach(role => {
                            let option = document.createElement("option");
                            option.value = role;
                            option.textContent = role;
                            roleField.appendChild(option);
                        });
                    })
                    .catch(error => console.error("Error fetching roles:", error));
            }
        });
    });
}