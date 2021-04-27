describe('Sign in', () => {
  it('click on sigin', () => {

    //visit site
    cy.visit('http://localhost:8000')
    //click on sign in in the main page
    cy.contains('Sign in')
    cy.wait(500)
    cy.get('a[href*="/signin"]').click()
    cy.url().should('include', '/signin')

    //click on icon
    cy.get('a[href*="/openid/login"]').click()
    cy.url().should('include', '/openid/login')

    //type in the info
    cy.get('input[id=steamAccountName]').type('goldchest161')
    cy.get('input[id=steamPassword]').type('Teamlightning161')
    cy.get('input[id=imageLogin]').click()
    cy.wait(500)
    cy.get('input[id=imageLogin]').click()
    cy.wait(500)
    cy.url().should('include', '/accounts/profile')
    cy.contains('goldchestcs161@gmail.com')

  })
})
