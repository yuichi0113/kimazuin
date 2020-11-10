$(function () {
    $(".btn-rule span").on("click", function () {
        if ($(this).text() == "キマズインとは！？") {
            $(this).text("×");
            $("#menu").removeClass("suru");
        } else {
            $(this).text("キマズインとは！？");
            $("#menu").addClass("suru");
        }
    });
});