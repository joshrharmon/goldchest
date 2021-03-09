import React, {Component} from "react";
import { Link } from "react-router-dom";

//In javascript you dont need to specify folders in this server
// just write name of nameofhtml to find href

//This is the navigation/menu bar component
export class Navbar extends Component {
    render() {
        return (


<div className="menu-area">
    <ul>

        <li><Link className="nav-link" to="/">Home</Link></li>

        <li><Link className="nav-link" to="/signin">Sign in</Link></li>


        <li><input type="text" name="" id="search-bar" placeholder="Search product or category . . . "/></li>

</ul>
</div>

)
}
}
