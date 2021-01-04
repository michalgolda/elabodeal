export const EditOptionBtnListener = ( e ) => {
    var btn = e.target;
    var input = btn.previousElementSibling;
    var cancelBtn = btn.nextElementSibling;

    // Current editing option elements
    var currentEditing = window.currentEditing;

    if ( !input || currentEditing ) return;

    // Forbid for edit another option
    window.currentEditing = [btn, input, cancelBtn];
 
    input.focus();
    input.select();
    input.readOnly = false;
    input.className = 'current-editing-input';

    btn.style.display = 'none';

    cancelBtn.style.display = 'block';
}