(function( $ ) {
    $.fn.listenRadioEnable = function(mutable_input) {
        $(this).click(function() {
            if($(this).is(':checked')) {
                mutable_input.removeAttr("disabled");
            }
        });
    };

    $.fn.listenRadioDisable = function(mutable_input) {
        $(this).click(function() {
            if($(this).is(':checked')) {
                mutable_input.attr("disabled", true);
            }
        });
    };

    $.fn.listenCheck = function(mutable_input) {
        $(this).click(function() {
            if($(this).is(':checked')) {
                mutable_input.removeAttr("disabled");
            }
            else {
                mutable_input.attr("disabled", true);
            }
        });
    };

    $.fn.listenCheckReverse = function(mutable_input) {
        $(this).click(function() {
            if(!$(this).is(':checked')) {
                mutable_input.removeAttr("disabled");
            }
            else {
                mutable_input.attr("disabled", true);
            }
        });
    };

    $.fn.listenSelect = function(val, mutable_input) {
        $(this).change(function(){
            if($(this).val() != val){
               mutable_input.removeAttr("disabled");
            }
            else {
                mutable_input.attr("disabled", true);
            }
        });
    };

}( jQuery ));
