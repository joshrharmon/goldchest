import React, {Component} from "react";
import { Link } from "react-router-dom";
import {CategoryGrid} from "../../CategoryGrid";
import {BestDealsGrid} from "../../BestDealsGrid";


//Query for search api
//http://localhost:5000/search?query=val&limit=10

//This is the Sports category component page
export class Category extends Component {

    //This is the HTML for 1 game (row) in the list displayed, we
    //use this html later to map the nr of rows to nr of games we fetch from api
    htmlCatList(game)
    {
        return (
            <a href={game.url} className="category-list-href">
            <li >
                <img src={game.art} width="70" height="25"/>
                <h3> {game.title}</h3>
                <p>{game.price_cut}% Discount NOW ${game.price_new}</p>
            </li>
                </a>
        );
    }

    //AJAX Call Request to the Flask Server, get the API data so we
    //can display it on the frontend
    fetchApiDynamicUrl(){
        if(window.location.pathname !== "/signin" && window.location.pathname !== "/accounts/profile/")
        {
            let categoryFromUrl = window.location.pathname.replace("/", "");
            console.warn(categoryFromUrl);
            fetch('http://localhost:5000/deals?cat='+categoryFromUrl+'&num=10')
                .then(res => res.json())
                .then(json => {
                    this.setState({
                        isLoaded: true,
                        catItems: json,
                    });
                    console.log(this.catItems)
             });
        }}



        //look at the bindings im making
    //use props to get CategoryFromURL,
    //console log
    componentDidMount() {
        this.fetchApiDynamicUrl();
    }
    render()
    {
        console.log(this.props);
        this.fetchApiDynamicUrl()
        let categoryFromUrl = window.location.pathname.replace("/", "");
        let isLoaded = this.state !== null ? this.state.isLoaded : false;
        if (!isLoaded)
        {
            return null
        }
        //remove this else and move into lifecycle
        //put this into componentDidUpdate
        //componentShouldUpdate
        else {
            if(categoryFromUrl !== this.state.catItems[0].category){
                //this.fetchApiDynamicUrl();
            }

            const mapHTMLtoNrOfGames = this.state.catItems.map( game => {
                return this.htmlCatList(game);
            });

            return (
                <div>
                    <CategoryGrid catItems={this.state.catItems}/>
                </div>,

            <div>
                <CategoryGrid/>
                <div className="container-fluid padding">
                    <div className="row welcome text-center">
                        <div className="col-12">
                            <h3>{categoryFromUrl}</h3>
                        </div>
                        <div className="col-12">
                        </div>
                    </div>
                    <div className="category">
                        <ul>
                                {mapHTMLtoNrOfGames}
                        </ul>
                    </div>
                </div>
            </div>
        )
            }
    }
}
