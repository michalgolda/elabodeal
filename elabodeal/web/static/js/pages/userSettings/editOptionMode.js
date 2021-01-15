
/** 
 * @param { HTMLElement } trigger - The element are in div which has a option__body class
 */
function ToggleEditOptionMode ( trigger ){
    var currentEditingOption = window.currentEditingOption;

    // Disable edit mode of last edited option
    if ( currentEditingOption ) 
        DisableEditOptionMode( currentEditingOption );
    
    var optionContainer = trigger.parentNode;
    
    currentEditingOption = trigger;
    
    window.currentEditingOption = currentEditingOption;

    var $optionContainer = $( optionContainer );
    var $optionInput = $optionContainer.find( '.js-option-input' );
    var $optionToggleModeBtn = $optionContainer.find( 'button.js-edit-option' );
    var $optionCancelEditBtn = $optionContainer.find( '.js-cancel-edit-option' );
    var $optionAcceptEditBtn = $optionContainer.find( '.js-accept-edit-option' );

    $optionToggleModeBtn.hide();

    $optionAcceptEditBtn.show();
    $optionCancelEditBtn.show();

    $optionContainer.addClass( 'option__body-editing' );

    $optionInput.focus();
    $optionInput.attr( 'readOnly', false );
}

/** 
 * @param { HTMLElement } trigger - The element are in div which has a option__body class
 * @param { Boolean } keepInputValue - Save or not input value
 */
function DisableEditOptionMode ( trigger, keepInputValue = false ){
    var currentEditingOption = window.currentEditingOption;

    // If has exist disable edit mode of last edited option else ingore
    if ( currentEditingOption && trigger === undefined )
        trigger = currentEditingOption;
    else if ( !trigger ) return;
    
    delete window.currentEditingOption;

    var optionContainer = trigger.parentNode;

    var $optionContainer = $( optionContainer );
    var $optionInput = $optionContainer.find( '.js-option-input' );
    var $optionToggleModeBtn = $optionContainer.find( 'button.js-edit-option' );
    var $optionCancelEditBtn = $optionContainer.find( '.js-cancel-edit-option' );
    var $optionAcceptEditBtn = $optionContainer.find( '.js-accept-edit-option' );

    $optionAcceptEditBtn.hide();
    $optionCancelEditBtn.hide();

    $optionToggleModeBtn.show();

    $optionContainer.removeClass( 'option__body-editing' );

    $optionInput.attr( 'readOnly', true );

    if ( !keepInputValue )
        $optionInput.val( $optionInput.attr( 'value' ) );
}

export { DisableEditOptionMode, ToggleEditOptionMode };