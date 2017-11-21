$(document).ready(function(){
    $('input.autocomplete').autocomplete({
        data: {
        "Apple": null,
        "Microsoft": null,
        "Google": null,
        "Gargle":null
        }
    });
});

(function($){
    $(function(){
        $('.button-collapse').sideNav({'edge': 'left'});
    });
})(jQuery);
