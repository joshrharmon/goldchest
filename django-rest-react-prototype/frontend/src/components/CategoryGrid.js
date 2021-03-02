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
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Adventure Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Action Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Strategy Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Childrens Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Childrens Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>

                        <div className="column" >
                            <li><Link className="row" to="/signin"> <i className="fas fa-baseball"></i> Sports Games</Link></li>
                        </div>



                    </ul>



                    {/* <div className="row">
                        <div className="column" >
                            <p>Cat 1</p>
                        </div>
                        <div className="column">
                            <p Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                        <div className="column" >
                            <h2>Sports Games</h2>
                            <p>Some text..</p>
                        </div>
                    </div>
*/}

                </div>





            </div>


        )
    }
}