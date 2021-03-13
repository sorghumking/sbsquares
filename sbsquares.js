$(document).ready(function() {
    $('td').on('mouseover', function() {
        highlightCommon($(this).text(), '#ff9933');
    });

    $('td').on('mouseout', function() {
        highlightCommon($(this).text(), '#ffffff');
    });
});

// highlight all <td> cells with text that matches name
function highlightCommon(name, color) {
    $('td.player').each(function() {
        if ($(this).text() == name) {
            $(this).css({
            WebkitTransition : 'background-color 0.3s ease-in-out',
            MozTransition    : 'background-color 0.3s ease-in-out',
            MsTransition     : 'background-color 0.3s ease-in-out',
            OTransition      : 'background-color 0.3s ease-in-out',
            transition       : 'background-color 0.3s ease-in-out'
            });
            $(this).css('backgroundColor', color);
        }
    });
}