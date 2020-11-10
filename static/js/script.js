$(function () {
    $("header span").on("click", function () {
        if ($(this).text() == "三") {
            $(this).text("×");
            $("#menu").removeClass("suru");
        } else {
            $(this).text("三");
            $("#menu").addClass("suru");
        }
    });
});