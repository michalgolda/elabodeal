const menu = $( '#js-menu' );
const showMenuTrigger = $( '#js-show-menu' );
const arrowIcons = {
    up: showMenuTrigger.children( '.fa-angle-down' ),
    down: showMenuTrigger.children( '.fa-angle-up' )
}

const hideMenu = () => {
    menu.hide();

    arrowIcons.up.show();
    arrowIcons.down.hide();
};

const showMenu = () => {
    menu.show();

    arrowIcons.up.hide();
    arrowIcons.down.show();
}

menu.hover( null, hideMenu );

showMenuTrigger.on( 'click', () => {
    var isHidden = menu.is( ':hidden' );

    if ( isHidden ) showMenu();
    else hideMenu();
} );