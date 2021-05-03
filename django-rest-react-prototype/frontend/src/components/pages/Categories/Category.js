import React, {Component} from "react";
import {CategoryGrid} from "../../CategoryGrid";
import {BestDealsGrid} from "../../BestDealsGrid";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    useParams
} from "react-router-dom";
import { withRouter } from "react-router";
import queryString from 'query-string';



//Query for search api
//http://localhost:5000/search?query=val&limit=10



//This is the Sports category component page
export class Category extends Component {


    state = {
        load: false,
        games: []
    }


    fetchApiData(){
        //get an object with the link to which url linker we are on
        const categoryID = this.props.match.params
        //get the first element in the categoryID object
        const firstElementInCategoryID = Object.values(categoryID)[0]
        console.log(firstElementInCategoryID)
        console.log('Do something with it', categoryID);
        //console.log('http://localhost:5000/deals?cat=' + firstElementInCategoryID + '&num=12')
        fetch('http://localhost:5000/deals?cat=' + firstElementInCategoryID + '&num=6')
            .then((response) => response.json())
            .then(gamesList => {
                this.setState({
                    games: gamesList
                    });
                console.log(this.games)
            });
    }

    componentDidMount() {
        this.fetchApiData()
    }


    componentDidUpdate(prevProps, prevState) {
        //get an object with the link to which url linker we are on
        const categoryID = this.props.match.params
        //get the first element in the categoryID object
        const firstElementInCategoryID = Object.values(categoryID)[0]

        //Debugging to see statements to see which variables to compare
        console.log('hello' + this.state)
        console.log('hello2' + prevState.state)
        console.log('hello3' + prevState.state)
        console.log('Games array' , this.state.games)
        console.log('category content ' + this.state.games[0].category)
        console.log('firstElementInCategoryID' + firstElementInCategoryID)
        console.log('hello5' + categoryID)
        console.log('hello' + this.state)

        //compare current category with the category state from the games list
        // (when you change state clicking on a different category)
        if (firstElementInCategoryID !== this.state.games[0].category) {
            console.log('State has changed.')
            this.fetchApiData()
        }
        }





render()
{
    const categoryIDhej = this.props.match.params
    //get the first element in the categoryID object
    const catName = Object.values(categoryIDhej)[0]
    return(
        <div>
            <CategoryGrid/>
            <div>
                <div className="container-fluid padding">
                    <div className="row welcome text-center">
                        <div className="col-12">

                        </div>
                        <div className="col-12">
                            <p className="lead"><b>{catName}</b></p>
                        </div>
                    </div>
                </div>
                <div className="row">
            {this.state.games.map((game) => (
                    <div className="col-md-4 product-grid">
                        <h5 className="text-center">{game.title}</h5>
                        <img src={game.art} alt="" className="w-100" />
                        <h5 className="text-center">NOW {game.currency}{game.price_new} SAVE {game.price_cut}%</h5>
                        <a href={game.url} className="btn buy">BUY NOW</a>
                    </div>
            ))}
        </div>
        </div>
        </div>

    )
}

}

