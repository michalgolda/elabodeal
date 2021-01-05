export default function alert( message, type, duration = 3600 ){
    var alert = $( '#js-alert' );

    if ( !alert ) return;

    var currentTypeClass = null;

    switch( type ){
        case 'success':
            currentTypeClass = 'alert-success';

            alert.addClass( currentTypeClass );
            break;
        case 'error':
            currentTypeClass = 'alert-error';
            
            alert.addClass( currentTypeClass );
            break;
        default:
            currentTypeClass = 'alert-success';

            alert.addClass( currentTypeClass );
    }

    alert.html( message );
    alert.show();

    setTimeout( function(){
        alert.hide();
        alert.removeClass( currentTypeClass );

    }, duration );
}