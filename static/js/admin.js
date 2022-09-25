if (typeof jQuery === 'undefined') {
    var jQuery = django.jQuery;
}

jQuery( document ).ready(function($) {
    var object_id = $('.confirm_button').attr('object_id');
    $('.confirm_button').click( function() {
        $.ajax
        ({
            type: "GET",
            url: `/orders/confirm/${object_id}/`,
            dataType: 'json',
            headers: {
                "Authorization": header
            },
            success: function (result) {
                alert(unit_information)
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
            }
        });
        location.reload();
    });
});