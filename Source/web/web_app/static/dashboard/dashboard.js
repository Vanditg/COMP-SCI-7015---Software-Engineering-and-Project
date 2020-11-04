var Dashboard = function(){

    var loadSomethingViaAjax = function(ajaxUrl){
        $.ajax({
            url: ajaxUrl,
            method: 'post',
            contentType: 'application/json; charset=utf-8',
            success: function(response){
                // arbitrary
                $('#ajax-data').html(response.name);
            }
        });
    }

    var init = function(ajaxUrl){
        var ctx = $('#myChart')[0];

        var myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            datasets: [{
              data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
              lineTension: 0,
              backgroundColor: 'transparent',
              borderColor: '#007bff',
              borderWidth: 4,
              pointBackgroundColor: '#007bff'
            }]
          },
          options: {
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: false
                }
              }]
            },
            legend: {
              display: false,
            }
          }
        });

        loadSomethingViaAjax.call(this, ajaxUrl);
    };
    

    return {
        init: init
    };
};