export const isExistElement = ( id, handler ) => {
    var element = document.getElementById( id );

    if ( !element ) return false;

    if ( handler instanceof Function )
        handler( element );

    return true;
};

export const isExistElements = ( classNames, handler ) => {
    var elements = document.getElementsByClassName( classNames );

    if ( elements.length === 0 ) return false;

    if ( handler instanceof Function )
        handler( elements );

    return true;
}
