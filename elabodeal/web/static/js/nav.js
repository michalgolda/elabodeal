$('#acc-action').click(function(){
    if($('#acc-actions-popup').is(':hidden')){
        $('#acc-actions-popup').show();
        $('#nav-arrow-down').show();
        $('#nav-arrow-up').hide(); 
    } else {
        $('#nav-arrow-down').hide();
        $('#nav-arrow-up').show();
        $('#acc-actions-popup').hide();
    }
})

$('#acc-actions-popup').hover(function(){}, function(){
    $(this).hide();
    $('#nav-arrow-down').hide();
    $('#nav-arrow-up').show();
})