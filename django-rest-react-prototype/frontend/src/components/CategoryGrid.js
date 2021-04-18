import React, {Component} from "react";
import {Link} from "react-router-dom";

export class CategoryGrid extends Component
{
    render()
    {
        return(
            <div>




                <div className="container-fluid padding">
                    <div className="row welcome text-center">
                        <div className="col-12">
                            <h3 className="display-4">Browse our Categories</h3>
                        </div>

                        <div className="col-12">
                            <p className="lead">We cover a wide variety of different game discounts</p>
                        </div>
                    </div>
                </div>


                <div className="best-deals-grid">
                    <ul>


                        <div className="column" >
                            <li>  <Link className="row" to="/sports"> <i className="fas fa-football-ball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/adventure"> <i className="fas fa-mountain"></i> Adventure Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/action"> <i className="fas fa-running"></i> Action Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/strategy"> <i className="fas fa-chess"></i> Strategy Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/childrens"> <i className="fas fa-cookie-bite"></i> Childrens Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/horror"> <i className="fab fa-snapchat-ghost"></i> Horror Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/racing"> <i className="fas fa-car"></i> Racing Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/shooter"> <i className="far fa-sun"></i> Shooter Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/anime"> <i className="fas fa-surprise"></i> Anime Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/rpg"> <i className="fas fa-gamepad"></i> RPG Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/mystery"> <i className="fas fa-user-secret"></i> Mystery Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/puzzle"> <i className="fas fa-puzzle-piece"></i> Puzzle Games</Link></li>
                        </div>


                    </ul>



                </div>

            </div>


        )
    }
}