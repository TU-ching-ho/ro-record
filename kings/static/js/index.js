const toggleBtn = document.getElementById("toggle-btn");//隱藏/顯示按鈕
const orderBtn = document.getElementById("order-btn");//排序按鈕
const table = document.getElementById("my-table");//無排序表格
const order_table = document.getElementById("my-order-table");//排序表格
const checkBtn = document.getElementById("check"); //查詢按鈕
resetBtn = document.getElementById("reset") //清除按鈕

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
});


resetBtn.addEventListener("click", function () {
    let ch_table = document.getElementById("my-table")
    let tds = ch_table.getElementsByTagName("td");
    document.getElementById("monster").selectedIndex = 0;
    document.getElementById("looking_name").innerHTML = "Name :&nbsp;";
    document.getElementById("looking_times").innerHTML = "times :&nbsp;";
    for (i = 0; i < tds.length; i++) {
        if (tds[i].textContent != monster) {
            tds[i].style.backgroundColor = "white"

        }
    }

});



checkBtn.addEventListener("click", function () {
    let monster = document.querySelector("#monster").value;
    if (monster == "") {
        alert("沒有選擇怪物哦!!!");
        return;
    }
    else {
        get_looking_monster();
    }
})

function get_looking_monster() {
    let looking_name = document.getElementById("looking_name");
    let looking_times = document.getElementById("looking_times");

    $.ajax(
        {
            url: "/jsondata/",
            type: "GET",
            datatype: "json",
            success: (data) => {
                //let record_kings = document.querySelector("#record_kings")
                let ch_table = document.getElementById("my-table")
                let tds = ch_table.getElementsByTagName("td");
                let monster = document.querySelector("#monster").value;
                for (let index = 0; index < data.kings.length; index++) {
                    if (monster == data["kings"][index]) {
                        looking_name.innerText = data["kings"][index];
                        looking_times.innerText = data["times"][index];
                    }

                }
                for (i = 0; i < tds.length; i++) {
                    //console.log(tds[i].textContent);
                    if (tds[i].textContent == monster) {
                        tds[i].style.backgroundColor = "yellow"
                    }
                }
            }
        }
    )
};
