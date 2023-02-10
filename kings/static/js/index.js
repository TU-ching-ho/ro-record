const toggleBtn = document.getElementById("toggle-btn");
const orderBtn = document.getElementById("order-btn");
const table = document.getElementById("my-table");
const order_table = document.getElementById("my-order-table");
const deletebtn = document.getElementById("delete_tool");

toggleBtn.addEventListener("click", function () {
    if (table.style.display === "none") {
        table.style.display = "table";
        toggleBtn.style = toggleBtn.style;
    }
    else {
        table.style.display = "none";
        toggleBtn.style.backgroundColor = "black";
    }
});

orderBtn.addEventListener("click", function () {
    if (order_table.style.display === "none") {
        order_table.style.display = "table";
        orderBtn.style = orderBtn.style;
    }
    else {
        order_table.style.display = "none";
        orderBtn.style.backgroundColor = "black";
    }
})


