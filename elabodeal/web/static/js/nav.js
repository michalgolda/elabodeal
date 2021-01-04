( function( document ){
    document.addEventListener( 'DOMContentLoaded', function(){
        var navShowMenu = document.querySelector( '#js-show-menu' );
        var navMenu = document.querySelector( '#js-menu' );

        if ( !navShowMenu || !navMenu ) return;

        // Get arrow icons
        arrowDownIcon = $( navShowMenu.children[ 2 ] );
        arrowUpIcon = $( navShowMenu.children[ 3 ] );

        /* Show/Hide popup with menu on click for btn in top navigation */
        navShowMenu.addEventListener( 'click', function(){
            if ( $( navMenu ).is( ':hidden' ) ) {
                $( navMenu ).show();
                
                arrowDownIcon.hide();
                arrowUpIcon.show();
            } else {
                $( navMenu ).hide();

                arrowUpIcon.hide();
                arrowDownIcon.show();
            }
        } );

        /* Hide popup on mouse out with menu area */
        $( navMenu ).hover( function(){}, function(){
            $( this ).hide();
            $( arrowDownIcon ).show();
            $( arrowUpIcon ).hide();
        } );
    } );
} )( document );    