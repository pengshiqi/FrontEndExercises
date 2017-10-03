'use strict';

var
    table = $('.table'),
    league = $("table>caption").text();


function reqListener() {
    var data = JSON.parse(this.responseText);
    data = data['data'];

    for (var i = 0; i < data.length; i++) {
        table.append(`<tr>
                    <th style='text-align:center'>${data[i]['排名']}</th>
                    <th style='text-align:center'>${data[i]['球队名']}</th>
                    <th style='text-align:center'>${data[i]['场次']}</th>
                    <th style='text-align:center'>${data[i]['积分']}</th>
                    <th style='text-align:center'>${data[i]['胜']}</th>
                    <th style='text-align:center'>${data[i]['平']}</th>
                    <th style='text-align:center'>${data[i]['负']}</th>
                    <th style='text-align:center'>${data[i]['进球']}</th>
                    <th style='text-align:center'>${data[i]['失球']}</th>
                    <th style='text-align:center'>${data[i]['净胜球']}</th>
                    </tr>`);
    }
};

// Method 1 :

// var url = 'http://138.68.40.103:8123/api/table/' + league;
var url = 'http://localhost:8123/api/table/' + league;
var xhr = new XMLHttpRequest();

xhr.onload = reqListener;
xhr.open('GET', url, true);
xhr.send(null);


// Method 2:

// $.ajax({
//     url: "http://138.68.40.103:8123/api/table/England",    //请求的url地址
//     dataType: "json",   //返回格式为json
//     async: true, //请求是否异步，默认为异步，这也是ajax重要特性
//     type: "GET",   //请求方式
//     beforeSend: function() {
//         //请求前的处理
//     },
//     success: function(req) {
//         console.log(req)
//         // var data = JSON.parse(req.responseText);
//         var data = req['data'];
//         for (var i = 0; i < data.length; i++) {
//             table.append(`<tr>
//                         <th>${data[i]['排名']}</th>
//                         <th>${data[i]['球队名']}</th>
//                         <th>${data[i]['场次']}</th>
//                         <th>${data[i]['积分']}</th>
//                         <th>${data[i]['胜']}</th>
//                         <th>${data[i]['平']}</th>
//                         <th>${data[i]['负']}</th>
//                         <th>${data[i]['进球']}</th>
//                         <th>${data[i]['失球']}</th>
//                         <th>${data[i]['净胜球']}</th>
//                         </tr>`);
//         }
//     },
//     complete: function() {
//         console.log('Accomplished!');
//     },
//     error: function() {
//         //请求出错处理
//     }
// });
