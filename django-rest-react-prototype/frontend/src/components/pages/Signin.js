import React, {Component} from "react";
import { Link } from "react-router-dom";


//This is the Home component (aka startpage)
export class Signin extends Component {
    render() {
        return (

            <div>
                <h1> Hello welcome to the Sign in React omponent</h1>



                <a href="/openid/login"> <img src="https://cdn.discordapp.com/attachments/745675669404385290/822209432648810526/sits_02.png"
                                                                     className="steamSignon" />
                </a>





            </div>



        )
    }
}
