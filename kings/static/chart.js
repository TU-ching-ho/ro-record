let chart = echarts.init(document.querySelector("#chart"))

$(document).ready(() => {
    draw_records()
});

window.onresize = function () {
    chart.resize();
}

function draw_records() {
    chart.showLoading();
    $.ajax(
        {
            url: "/jsondata/",
            type: "GET",
            dataType: "json",
            success: (data) => {
                chart.hideLoading();
                records(data["kings"], data["times"])
                console.log(data)
            },
            error: () => {
                chart.hideLoading();
                alert("讀取資料失敗")
            }
        }
    )
};




function records(xdata, ydata) {
    let option = {
        title: {
            text: 'ro-record'
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'left',
            top: 'center',
            feature: {
                magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        tooltip: { trigger: 'axis' },
        legend: {},
        xAxis: {
            data: xdata
        },
        yAxis: {},
        series: [
            {
                itemStyle: {
                    color: '#172b85'
                },

                name: 'ˋ次數',
                type: 'bar',
                data: ydata
            }
        ]
    };
    chart.setOption(option);
}