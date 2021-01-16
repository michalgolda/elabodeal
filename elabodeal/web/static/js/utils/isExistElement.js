const isExistElement = ( elementId, handler ) => {
    var element = document.getElementById( elementId );

    if ( !element ) return false;

    handler( element );
};

export default isExistElement;