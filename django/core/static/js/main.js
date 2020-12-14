// Get the value of a URL parameter by providing the key
function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    // Store the value outside of loop, so if multiple of the same param name the last is taken
    var lastValueFound;

    // Loop through each parameter
    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] === sParam) lastValueFound = sParameterName[1] === undefined ? true : sParameterName[1];
    }

    return lastValueFound;
}


// Initiate jQuery
$(document).ready(function() {

    // Scroll down to main welcome section when clicking on the proceed button in the welcome banner
    $('#welcome-banner-proceed').on('click', function(){
        $('html,body').animate({ scrollTop: $('#welcome-content').offset().top - 50 }, 800); 
    });

    // Show advanced options on list page
    $('#list-options-advanced-show').find('strong').on('click', function(){
        $('#list-options-advanced-popup').fadeIn(100);
    });
    // Hide advanced options on list page
    $('#list-options-advanced-popup-content-close, #list-options-advanced-popup').on('click', function(){
        $('#list-options-advanced-popup').fadeOut(200);
    });
    // Prevent it from closing when clicking popup content
    $('#list-options-advanced-popup-content').click(function(e) { 
        e.stopPropagation();
    });

});