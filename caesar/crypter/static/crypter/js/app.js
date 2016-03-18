// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Function to sending text and receiving data to plot a chart
function drawChart() {
    var msg   = $('#uncode_text').serialize();
            console.log(msg);
            $.ajax({
            type: 'POST',
            url: 'chart/',
            data: msg,
            success: function(data) {
                var chart_data = data['chart_text'];
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
// Function to send text and receive ciphertext in a text field for the result
function call() {
    var msg   = $('#uncode_text').serialize();
    console.log(msg);
    $.ajax({
    type: 'POST',
    url: 'ciphertext/',
    data: msg,
    success: function(data) {
        $('#code_text').html(data['code_text']);
    },
    error:  function(xhr, str){
    alert('Error: ' + xhr.responseCode);
    }
});
}