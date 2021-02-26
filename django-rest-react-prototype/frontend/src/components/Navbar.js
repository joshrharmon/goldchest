import React, {Component} from "react";
import { Link } from "react-router-dom";

//In javascript you dont need to specify folders in this server
// just write name of nameofhtml to find href

//This is the navigation/menu bar component
export class Navbar extends Component {
    render() {
        return (

            <nav className="navbar navbar-expand-md navbar-light bg-">
                <div>

                    <div className="collpase navbar-collapse" id="navbarResponsive">
                        <ul className="navbar-nav ml-auto">
                            <li className="nav-item active nav-item-padding">
                                <Link className="nav-link" to="/">Home</Link>
                            </li>

                            <li className="nav-item active nav-item-padding">
                                <Link className="nav-link" to="/signin">Sign in</Link>
                            </li>

                        </ul>
                    </div>

                </div>
            </nav>



        )
    }
}
