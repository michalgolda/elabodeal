$('#nav-menu-open').click(function(){
    if($('#nav-menu').is(':hidden')){
        $('#nav-menu').show();
        $('#nav-arrow-down').hide();
        $('#nav-arrow-up').show(); 
    } else {
        $('#nav-arrow-down').show();
        $('#nav-arrow-up').hide();
        $('#nav-menu').hide();
    }
})

$('#nav-menu').hover(function(){}, function(){
    $(this).hide();
    $('#nav-arrow-down').show();
    $('#nav-arrow-up').hide();
})