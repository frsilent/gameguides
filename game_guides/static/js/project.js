/* Project specific Javascript goes here. */

/* Index Page */
$(document).ready(function() {
    $('.sample-video').click(function() {
        var url = $(this).data('url');
        var player = $('#feature-player').children('iframe');
        player.attr('src', url);
        return false;
    });
});
/* END Index Page */
