/**
 * Created by Adge on 8/31/2015.
 */
function ready_function(jQuery) {
    var table = $('#alarmtable').DataTable({
        ajax: {
            url: '/alarms',
            dataSrc: 'alarms'
        },
        columns: [
            {data: 'date'},
            {data: 'name'},
            {data: 'severity'},
            {data: 'description'}]
    });
    setInterval( function () {
    table.ajax.reload( null, false ); // user paging is not reset on reload
    }, 30000 );
}

$(document).ready(ready_function);
