$(document).ready(function () {
    $("#date").datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: 'dd/mm/yy',
        yearRange: "2000:2022"
    });
    $("#modal").modal('show');
})