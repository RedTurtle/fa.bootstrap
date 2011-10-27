$(document).ready(function(){
    window.setTimeout(function() { 
        $(".alert-message").children('a').trigger('click');
    }, 2000);
});
