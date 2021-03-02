import React, {Component} from "react";
import { Link } from "react-router-dom";
import {CategoryGrid} from "../CategoryGrid";
import {BestDealsGrid} from "../BestDealsGrid";

//In javascript you dont need to specify folders in this server
// just write name of nameofhtml to find href

//This is the Home component (aka startpage)
export class Home extends Component {
    render() {
        return (

<div>
    <CategoryGrid/>
    <BestDealsGrid/>
</div>


        )
    }
}
