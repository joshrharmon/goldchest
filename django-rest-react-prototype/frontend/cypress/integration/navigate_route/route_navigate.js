describe('Navigate Categories Routing', () => {

    it('clicks the link: sports games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Sports Games')
        cy.wait(500)
        cy.get('a[href*="/sports"]').click()
        cy.url().should('include', '/sports')
    })

    it('clicks the link: adventure games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Adventure Games')
        cy.wait(500)
        cy.get('a[href*="/adventure"]').click()
        cy.url().should('include', '/adventure')
    })

    it('clicks the link: action games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Action Games')
        cy.wait(500)
        cy.get('a[href*="/action"]').click()
        cy.url().should('include', '/action')
    })

    it('clicks the link: children games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Childrens Games')
        cy.wait(500)
        cy.get('a[href*="/childrens"]').click()
        cy.url().should('include', '/childrens')
    })

    it('clicks the link: horror games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Horror Games')
        cy.wait(500)
        cy.get('a[href*="/horror"]').click()
        cy.url().should('include', '/horror')
    })

    it('clicks the link: racing games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Racing Games')
        cy.wait(500)
        cy.get('a[href*="/racing"]').should('be.visible').click()
        cy.url().should('include', '/racing')
    })

    it('clicks the link: shooter games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Shooter Games')
        cy.wait(500)
        cy.get('a[href*="/shooter"]').click()
        cy.url().should('include', '/shooter')
    })

    it('clicks the link: anime games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Anime Games')
        cy.wait(500)
        cy.get('a[href*="/anime"]').click()
        cy.url().should('include', '/anime')
    })

    it('clicks the link: RPG games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('RPG Games')
        cy.wait(500)
        cy.get('a[href*="/rpg"]').click()
        cy.url().should('include', '/rpg')
    })

    it('clicks the link: mystery games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Mystery Games')
        cy.wait(500)
        cy.get('a[href*="/mystery"]').click()
        cy.url().should('include', '/mystery')
    })

    it('clicks the link: puzzle games', () => {
        cy.visit('http://localhost:8000')
        cy.contains('Puzzle Games')
        cy.wait(500)
        cy.get('a[href*="/puzzle"]').click()
        cy.url().should('include', '/puzzle')
    })


  })
