$(function() {
    $('#tratamento-lista > tbody > tr').click(function() {
        window.location = $(this).data('url');
    });
});