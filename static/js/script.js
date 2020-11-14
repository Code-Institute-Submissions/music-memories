$(document).ready(function () {

    // Date Selector
    $("#date").datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: 'dd/mm/yy',
        yearRange: "2000:2022"
    });

    // Modal Display
    $("#modal").modal('show');


    // Search Results
    var list = $("#artist-lists").length;

    if (list < 1) {
        $(".concert-header").hide();
        $(".flash-add").removeClass('flash-add');
    }
})