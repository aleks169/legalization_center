$(document).ready(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 300) {
            $(".navbar-default").css("background", "rgb(149, 163, 227)");
            $("li>a").css("color", "white");
        } else {
            $(".navbar-default").css("background", " #d6d4dfb5");
            $("li>a").css("color", "#000");
        }
    })
});
