$(function() {
    $('#button').click(function() {
        $.ajax({
            url: '/api',
            data: $('form').serialize(),
            type: 'POST',
            success:function(response){
                 $('#shorturl').text(response.short_url)
            }
        })
        event.preventDefault();
    });
});