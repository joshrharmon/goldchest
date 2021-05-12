describe('Navigate to a game inside the page', () => {

    it('Click the link of the first game', () => {
        cy.visit('http://localhost:8000')
        //get the name of the first game
        cy.get('h5[class*="text-center"]:first').then(($value) => {
          //store it
          const game_name = $value.text()
          //click buy now to direct to a new page
          cy.get('a[class*="btn buy"]:first').click()
          //check if the new page contains the name of the game
          cy.contains(game_name)
        })
    })
})
