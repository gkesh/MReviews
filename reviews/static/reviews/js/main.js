$(document).ready(function () {
    $('.col-menu-item').on('click', function(){
        $('.col-menu-item').removeClass('active');
        $('.col-container').removeClass('d-block').addClass('d-none');
        $("."+$(this).attr('data-attr')).removeClass('d-none').addClass('d-block');
        $(this).addClass('active');
    });
    $('.toast button').on('click', function () {
        $('.toast').addClass('d-none');
    });
    $('.close-greeting').on('click', function () {
       $('.greeting').addClass('d-none');
    });
});