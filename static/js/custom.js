//$(document).ready(function() {
//    $('form').on('submit', function(event) {
//        $.ajax({
//                data:{longurl: $('#longurl').val()},
//                type:'POST',
//                url: '/'
//            })
//            .done(function(data){
//                contents = data.results;
//                $('#shorturl').val = contents;
//            });
//        event.preventDefault();
//    });
//});
//
$(function() {
    $('#button').click(function() {
        $.ajax({
            url: '/api',
            data: $('form').serialize(),
            type: 'POST',
            success:function(response){
                console.log(response);
                console.log(response.short_url);
                 $('#shorturl').text(response.short_url)
            }
        })
//        .done(function(data){
//        console.log(data);
//            console.log(data.short_url);
//
////            contents = data.results
//            $('#shorturl').val = data.short_url
//        });
        event.preventDefault();
    });
});