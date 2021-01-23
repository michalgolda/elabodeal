import { isExistElement, isExistElements } from '../exist';


describe( 'Test utils function in exist module', () => {
    test( 'Test isExistElement function if element does not exist in dom', () => {
        expect( 
            isExistElement( 'element' )
        ).toBe( false );
    } );

    test( 'Test isExistElement function if element does exist in dom', () => {
        document.body.innerHTML = `
            <div id="element"></div>
        `;

        expect(
            isExistElement( 'element' )
        ).toBe( true );
    } );
    
    test( 'Test isExistElement function execute handler function', () => {
        document.body.innerHTML = `
            <div id="element"></div>
        `;
        
        expect(
            isExistElement( 'element', ( element ) => {
                element.innerHTML = 'Handler function';
            } )
        ).toBe( true );
        
        var element = document.getElementById( 'element' );

        expect(
            element.textContent
        ).toEqual( 'Handler function' );
    } );

    test( 'Test isExistElements function if element does not exist in dom', () => {
        expect( 
            isExistElements( 'element' )
        ).toBe( false );
    } );

    test( 'Test isExistElements function if element does exist in dom', () => {
        document.body.innerHTML = `
            <div class="element"></div>
            <div class="element"></div>
        `;

        expect(
            isExistElements( 'element' )
        ).toBe( true );
    } );
    
    test( 'Test isExistElement function execute handler function', () => {
        document.body.innerHTML = `
            <div class="element"></div>
            <div class="element"></div>
        `;
        
        expect(
            isExistElements( 'element', ( elements ) => {
                elements[ 0 ].innerHTML = 'Handler function';
            } )
        ).toBe( true );
        
        var elements = document.getElementsByClassName( 'element' );

        expect(
            elements[ 0 ].textContent
        ).toEqual( 'Handler function' );
    } );
} );