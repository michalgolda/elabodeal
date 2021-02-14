import Vue from "vue";
import userService from '../../services/user';

// Components
import EmailConfirmationRequiredInfo from './userSettings/components/EmailConfirmationRequiredInfo.vue';


const mountElement = document.getElementById( "js-mount-settings-form" );
const mountData    = mountElement.dataset;

new Vue( {
	el: mountElement,
	name: "SettingsForm",
	components: {
		EmailConfirmationRequiredInfo
	},
	data() {
		return {
			...mountData,
			currentEditingOptionTrigger: null
		}
	},
	methods: {
		handleSaveSettings( e ) {
			this.handleDisableEditMode( null );

			const { saveSettingsAction } = this;

			const data = Object.fromEntries( new FormData( e.target ) );

			userService.updateSettings( 
				saveSettingsAction,
				data,
				{
					errorHandler: ( error ) => {
						var fieldErrors = Object.keys( error.response.data );

						for ( var fieldError of fieldErrors )
							this._showFieldError( fieldError );
					}
				}
			)
		},
		handleChangeOption( e ) {
			const { optionField } = this._getEditingOptionElements( e );

			this._clearFieldError( optionField.name );
		},
		handleEnableEditMode( e ) {
			if ( this.currentEditingOptionTrigger )
				this.handleDisableEditMode( null );

			const {
				optionContainer,
				optionField,
				optionEnableEditModeBtn,
				optionDisableEditModeBtn,
				optionAcceptChangeBtn
			} = this._getEditingOptionElements( e );

			this.currentEditingOptionTrigger = e;

			optionEnableEditModeBtn.style.display = "none";

			optionAcceptChangeBtn.style.display = null;
			optionDisableEditModeBtn.style.display = null;

			optionContainer.classList.add( "option__body-editing" );

			optionField.focus();
			optionField.removeAttribute( "readOnly" );
		},
		handleDisableEditMode( e, keepFieldValue = false ) {
			if ( this.currentEditingOptionTrigger && e === null )
				e = this.currentEditingOptionTrigger;
			else if ( !e ) return;

			this.currentEditingOptionTrigger = null;

			const {
				optionContainer,
				optionField,
				optionEnableEditModeBtn,
				optionDisableEditModeBtn,
				optionAcceptChangeBtn
			} = this._getEditingOptionElements( e );

			optionEnableEditModeBtn.style.display = null;

			optionAcceptChangeBtn.style.display = "none";
			optionDisableEditModeBtn.style.display = "none";

			optionContainer.classList.remove( "option__body-editing" );

			optionField.setAttribute( "readOnly", "" );

			if ( !keepFieldValue )
				optionField.value = optionField.getAttribute( "value" );
		},
		_getEditingOptionElements( e ) {
			var optionContainer = e.target.parentElement;

			return {
				optionContainer,
				optionField: optionContainer.children[ 0 ],
				optionEnableEditModeBtn: optionContainer.children[ 1 ],
				optionDisableEditModeBtn: optionContainer.children[ 3 ],
				optionAcceptChangeBtn: optionContainer.children[ 2 ] 
			}
		},
		_showFieldError( field ) {
			this.$refs[ field ].classList.add( "option__input-error" );
		},
		_clearFieldError( field ) {
			this.$refs[ field ].classList.remove( "option__input-error" );
		}
	}
} );