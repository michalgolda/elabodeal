describe('Tests for index page', function() {
  test('Test index page', function(browser) {
    browser
      .init()
      .waitForElementVisible('body')
      .assert.title('Elabodeal - Home')
      .assert.elementPresent('.category-list')
      .assert.elementPresent('.nav')
      .assert.elementPresent('.big-footer')
      .assert.elementPresent('form')
      .assert.elementPresent('.product-list')
      .assert.elementPresent('.banner')
      .assert.attributeEquals('input[name=q]', 'type', 'text')
      .assert.attributeEquals('input[name=q]', 'required', 'true')
      .assert.attributeEquals('input[name=q]', 'placeholder', 'Imię, nazwisko autora lub tytuł')
      .assert.attributeEquals('button', 'type', 'submit')
      .assert.containsText('button', 'Szukaj')
      .end();
  });
});