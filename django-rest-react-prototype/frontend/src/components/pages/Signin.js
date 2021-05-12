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
                            <p className="lead">Sign in below using Steam</p>
                        </div>
                    </div>
                </div>

                <div className="container px-4 py-5 mx-auto">
                    <div className="card card0">
                        <div className="d-flex flex-lg-row flex-column-reverse">
                            <div className="card card1">
                                <div className="row justify-content-center my-auto">
                                    <div className="col-md-8 col-10 my-5">
                                        <div className="row justify-content-center px-3 mb-3">
                                                <div className="logo-signinJS">
                                                    <img  src="https://cdn.discordapp.com/attachments/687798557138616390/841584406056402964/GoldChestLogo.png"
                                                    />
                                                </div>
                                        </div>
                                        <h3 className="mb-5 text-center heading">We are Goldchest</h3>
                                        <h6 className="msg-info">Please login to your account using Steam</h6>

                                        <a href="/openid/login"> <img src="https://cdn.discordapp.com/attachments/745675669404385290/822209432648810526/sits_02.png"
                                                                      className="steam-signon" />
                                        </a>

                                    </div>
                                </div>
                                <div className="bottom text-center mb-5"><div className="dont-have-link">
                                    <a className="dont-have-link" href="https://store.steampowered.com/join/?&snr=1_60_4__62" >Don't have a Steam account?
                                        <button  className="btn btn-white ml-2">Create one</button>
                                    </a></div>
                                </div>
                            </div>
                            <div className="card card2">
                                <div className="my-auto mx-md-5 px-md-5 right">
                                    <h3 className="text-white">Find video game discounts at Goldchest</h3>
                                    <small className="text-white">Browse thousands of video game discounts at the Goldchest application.
                                        We have a variety of different categories including action, adventure, anime, childrens, horror,
                                        mystery, puzzle, racing, RPG, shooter, sports and strategy. Search for the game you are looking for
                                        using the search bar, or see the hottest game deals at in our deals selection.
                                    </small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>



        )
    }
}
