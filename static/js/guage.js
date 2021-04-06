$(document).ready(function () {
    $(document).on("change", "select", function () {

        // var pathname = window.location.pathname; // Returns path only (/path/example.html)
        // var url = window.location.href;     // Returns full URL (https://example.com/path/example.html)
        var origin = window.location.origin;
        var weight = $(this).val();
        // alert(origin);
        $(location).attr('href', origin + '/index_update/' + weight)

    });


});

