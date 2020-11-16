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
    console.log(list);
    if (list < 1) {
        $(".concert-header").hide();
        $(".flash-add").removeClass("flash-add");
    }

    // Profile Text Section

    var profList = $("#artist-lists-profile").length;
    console.log(profList);
    if (profList < 1) {
        $(".profile-add").removeClass("profile-add");
        $(".profile-with-details").addClass("profile-with-details");
    }
})