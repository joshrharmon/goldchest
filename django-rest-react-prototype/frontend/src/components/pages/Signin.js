import React, {Component} from "react";
import { Link } from "react-router-dom";


//This is the Home component (aka startpage)
export class Signin extends Component {
    render() {
        return (

            <div>

                <div className="container-fluid padding">
                    <div className="row welcome text-center">
                        <div className="col-12">
                            <h3 className="display-4">Sign In Component Page</h3>
                        </div>

                        <div className="col-12">
                            <p className="lead">Below is a simple working demo of the Steam Single Sign on</p>
                        </div>
                    </div>
                </div>


                <a href="/openid/login"> <img src="https://cdn.discordapp.com/attachments/745675669404385290/822209432648810526/sits_02.png"
                                                                     className="steam-signon" />
                </a>





            </div>



        )
    }
}
