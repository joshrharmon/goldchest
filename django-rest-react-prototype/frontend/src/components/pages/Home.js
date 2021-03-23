import React, {Component} from "react";
import {Link, Route} from "react-router-dom";
import {CategoryGrid} from "../CategoryGrid";
import {BestDealsGrid} from "../BestDealsGrid";

import {BrowserRouter as Router} from "react-router-dom";


//This is the Home component (aka startpage)
export class Home extends Component {


    constructor(props)
    {
        super(props);
        this.state = {
            items: [],
            isLoaded: false
        }
    }

    //AJAX Call Request to the Flask Server, get the API data so we
    //can display it on the frontend
    componentDidMount() {
        fetch('http://localhost:5000/deals?num=6')
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    items: json,
                })
            });
    }


        render()
        {
            var {isLoaded, items} = this.state;
            if (!isLoaded)
            {
                return <div> Data Is Loading...</div>
            }

            else {

            return (

            <div>

                <h2>Data has been loaded</h2>
                <CategoryGrid/>
                <BestDealsGrid items={items}/>


            </div>



        )
            }
    }

}
