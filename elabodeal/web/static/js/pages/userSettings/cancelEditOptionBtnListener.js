export const CancelEditOptionBtnListener = ( e ) => {
    
    // Allow to click for edit btn
    delete window.currentEditing;
    
    var btn = e.target;

    var editBtn = btn.parentNode.children[ 1 ];
    var input = btn.parentNode.children[ 0 ];

    btn.style.display = 'none';

    input.readOnly = true;
    input.classList.remove( 'current-editing-input' );

    // Remove selected test
    window.getSelection().removeAllRanges();

    editBtn.style.display = 'block';

    btn.style.display = 'none';
}