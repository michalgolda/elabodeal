export const SectionDropdown = ( trigger, section ) => {
    trigger.addEventListener( 'click', function( e ) {
        e.preventDefault();

        var dropdownCaretElement = this.children[1];

        var isHidden = section.style.display === 'none' ? true : false;
        
        if ( isHidden ) { 
            section.style.display = 'grid'; 
            dropdownCaretElement.style.transform = 'rotate(180deg)';
        } else { 
            section.style.display = 'none'; 
            dropdownCaretElement.style.transform = '';
        }
    } );
};