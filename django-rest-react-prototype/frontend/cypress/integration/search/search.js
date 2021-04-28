describe('Test Search Function', () => {
  it('Testing search bar', () => {
    //visit site
    cy.visit('http://localhost:8000')
    cy.get('input[id="search-bar"]').type('assassin creed{enter}')

    cy.contains('assassin creed')
  })
})
