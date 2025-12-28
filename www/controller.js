$(document).ready(function() {
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").fadeIn(300).delay(2000).fadeOut(300);
    }
});