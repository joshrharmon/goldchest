describe('My First Test', () => {
    it('clicks the link: action games', () => {
        cy.visit('http://localhost:8000')
        cy.contains("Category Games").click()
        cy.url().should('include', '/action')
    })
  })
