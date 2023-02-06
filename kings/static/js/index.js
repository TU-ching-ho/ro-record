const toggleBtn = document.getElementById("toggle-btn");
const table = document.getElementById("my-table");

toggleBtn.addEventListener("click", function () {
    if (table.style.display === "none") {
        table.style.display = "table";
    }
    else {
        table.style.display = "none";
    }
});
