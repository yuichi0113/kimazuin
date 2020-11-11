$(function () {
    $(".btn-rule").on("click", function () {
        if ($(this).text() == "キマズインとは！？") {
            $(this).text("キマズインとは！？");
            $("#menu").removeClass("suru");
        } else {
            $(this).text("キマズインとは！？");
            $("#menu").addClass("suru");
        }
    });
});

$(function () {
    $(".btn-rule-close").on("click", function () {
        if ($(this).text() == "キマズインとは！？") {
            $(this).text("CLOSE");
            $("#menu").removeClass("suru");
        } else {
            $(this).text("CLOSE");
            $("#menu").addClass("suru");
        }
    });
});

