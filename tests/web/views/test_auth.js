describe('Simple test of auth pages', function() {
  test('Test login page', function(browser) {
    browser
      .url(`${browser.options.launch_url}/auth/login/`)
      .waitForElementVisible('body')
      .assert.title('Elabodeal - Zaloguj się')
      .assert.elementPresent('form')
      .assert.elementPresent('.footer')
      .assert.elementPresent('.decorator')
      .assert.elementPresent('.logo')
      .assert.elementPresent('input[name=csrfmiddlewaretoken]')
      .assert.elementPresent('input[name=email]')
      .assert.elementPresent('input[name=password]')
      .assert.attributeEquals('input[name=csrfmiddlewaretoken]', 'type', 'hidden')
      .assert.attributeEquals('input[name=email]', 'type', 'text')
      .assert.attributeEquals('input[name=password]', 'type', 'password')
      .assert.containsText('button', 'Zaloguj się')
      .assert.attributeEquals('input[name=email]', 'required', 'true')
      .assert.attributeEquals('input[name=password]', 'required', 'true')
      .assert.attributeEquals('form', 'method', 'POST')
      .assert.attributeEquals('button[type=submit]', 'type', 'submit')
      .assert.attributeEquals('form', 'autocomplete', 'off')
      .assert.attributeEquals('form', 'action', '/auth/login/')
      .end();
  });

  test('Test register page', function(browser) {
    browser
      .url(`${browser.options.launch_url}/auth/register/`)
      .waitForElementVisible('body')
      .assert.title('Elabodeal - Stwórz swoje konto')
      .assert.elementPresent('form')
      .assert.elementPresent('.footer')
      .assert.elementPresent('.decorator')
      .assert.elementPresent('.logo')
      .assert.elementPresent('input[name=csrfmiddlewaretoken]')
      .assert.elementPresent('input[name=email]')
      .assert.elementPresent('input[name=username]')
      .assert.elementPresent('input[name=password1]')
      .assert.elementPresent('input[name=password2]')
      .assert.attributeEquals('input[name=csrfmiddlewaretoken]', 'type', 'hidden')
      .assert.attributeEquals('input[name=email]', 'type', 'text')
      .assert.attributeEquals('input[name=username]', 'type', 'text')
      .assert.attributeEquals('input[name=password1]', 'type', 'password')
      .assert.attributeEquals('input[name=password2]', 'type', 'password')
      .assert.containsText('button', 'Zarejestruj się')
      .assert.attributeEquals('input[name=email]', 'required', 'true')
      .assert.attributeEquals('input[name=username]', 'required', 'true')
      .assert.attributeEquals('input[name=username]', 'maxlength', '30')
      .assert.attributeEquals('input[name=password1]', 'required', 'true')
      .assert.attributeEquals('input[name=password2]', 'required', 'true')
      .assert.attributeEquals('button[type=submit]', 'type', 'submit')
      .assert.attributeEquals('form', 'method', 'POST')
      .assert.attributeEquals('form', 'autocomplete', 'off')
      .assert.attributeEquals('form', 'action', '/auth/register/')
      .end();
  });
});