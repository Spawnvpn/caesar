// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var msg   = $('#uncode_text').serialize();
            console.log(msg);
            $.ajax({
            type: 'POST',
            url: 'chart/',
            data: msg,
            success: function(data) {
                var chart_data = data['chart_text'];
                console.log("result:");
                console.log(chart_data);
                addRows(chart_data)
            },
            error:  function(xhr, str){
            alert('Возникла ошибка: ' + xhr.responseCode);
            }
        });
    function addRows (chart_data) {
        var data_table = new google.visualization.DataTable();
        console.log(data_table);
        data_table.addColumn('string', 'Topping');
        data_table.addColumn('number', 'Number of letters');
        data_table.addRows(chart_data);
                // Set chart options
        var options = {'title':'Letter frequency',
                   'width':900,
                   'height':300};

    // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data_table, options);
    }
}

function call() {
    var msg   = $('#uncode_text').serialize();
    console.log(msg);
    $.ajax({
    type: 'POST',
    url: 'ajax_func/',
    data: msg,
    success: function(data) {
        console.log("data:");
        console.log(data);
        $('#code_text').html(data['code_text']);
    },
    error:  function(xhr, str){
    alert('Возникла ошибка: ' + xhr.responseCode);
    }
});
}