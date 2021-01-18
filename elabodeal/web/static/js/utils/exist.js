export const isExistElement = ( id, handler ) => {
    var element = document.getElementById( id );

    if ( !element ) return false;

    handler( element );
};

export const isExistElements = ( classNames, handler ) => {
    var elements = document.getElementsByClassName( classNames );

    if ( !elements ) return false;

    handler( elements );
}
