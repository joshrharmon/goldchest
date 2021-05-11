import React, {Component} from "react";
import { Link } from "react-router-dom";
import axios from 'axios';
import {GameInfo} from "./GameInfo";

//In javascript you dont need to specify folders in this server
// just write name of nameofhtml to find href

//The search bar uses npm install axios



//This is the navigation/menu bar component
export class Navbar extends Component {


    constructor(props){
        super(props);

        this.state = {
            query: '', //the users query that he typed
            results: {}, //the results
            loading: false, //if the search is currently loading
            message: '' //potential error message
        }
        this.cancel = '';
    }


    //21:48
    fetchSearchResults = (query) =>{
        //const searchUrl = 'https://pixabay.com/api/?key=21433317-73a0029f8286b31255959139d&q='+query+'&image_type=photo'
        const searchUrl = 'http://localhost:5000/search?query='+query+'&limit=3'
        //check if cancel has any value
        if(this.cancel){
            //if it has value then go ahead and cancel that request
            this.cancel.cancel()
        }

        this.cancel = axios.CancelToken.source();

        axios.get(searchUrl, {
            cancelToken: this.cancel.token
        })
            .then(res => {
                //if the length of the hits array is 0, then no results found
                const resultNotFoundMsg = !res.data.length ? 'No more search results' : '';
                console.warn(res.data);

                //Set the state for all the data fetched
                this.setState({
                    results: res.data,
                    message: resultNotFoundMsg,
                    loading: false
                })
        })
            .catch(error => {
                if(axios.isCancel(error) || error)
                {
                    this.setState({
                        loading: false,
                        message: 'Failed to fetch data axios'
                    })
                }
        })

    }


    handleInputChange = (event) => {
        const query = event.target.value;
        console.warn(query);
        this.setState({query: query, loading: true, message: ''}, () =>  {
            this.fetchSearchResults(query);
        });
    };

    renderSearchResults = () => {
        const { results } = this.state;

        if ( Object.keys( results ).length && results.length ) {
            return (
                <div className="results-container">
                    { results.map( result => {
                        return <GameInfo
                          key={result.title}
                          title={result.title}
                          art={result.art}
                          currency={result.price[0]}
                          price={result.price[1]}
                          url={result.url}
                        />
                    } ) }

                </div>
            )
        }
    };

    render() {
        const {query} = this.state;
        console.warn(this.state);

        return (
<div className="menu-area">
    <ul>
        <li><Link className="nav-link" to="/">Home</Link></li>
        <li><Link className="nav-link" to="/signin">Sign in</Link></li>
        <li><input
            type="text"
            value={query}
            name="query"
            id="search-bar"
            onChange={this.handleInputChange}
            placeholder="Search product or category . . . "/></li>
    </ul>




    <div className="container-fluid padding">
        <div className="row welcome text-center">
            <div className="col-12">

            </div>

        </div>
    </div>
    <div className="row">
        {this.renderSearchResults()}
    </div>



</div>

)

}
}
