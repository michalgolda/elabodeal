import './setCodeInputValue';

/**
 * This function getting code from all inputs which has class of "code__input"
 * and setting main input of code value
 * 
 * @param {HTMLElement} form Form element containing input 
 *                           which has "name" property equals "code" 
 */
export const setCodeInputValue = ( form ) => {
    var $form = $( form );
    
    var code = $form.find( 'input[name="code"]' );
    var codeInputElements = $( '.code__input' );

    if ( !codeInputElements || !code ) return;

    var codeString = '';
    for ( var input of codeInputElements )
        codeString += input.value;

    code.val( codeString );
};