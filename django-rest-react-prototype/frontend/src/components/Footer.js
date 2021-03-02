import React, {Component} from "react";
import { Link } from "react-router-dom";

//In javascript you dont need to specify folders in this server
// just write name of nameofhtml to find href

//This is the Footer bar component
export class Footer extends Component {
    render() {
        return (

            <footer>
                <div className="container-fluid padding">
                    <div className="row text-center">


                        <div className="col-md-4">
                            <hr className="light"/>
                            <h5>Learn More</h5>
                            <hr className="light"/>
                            <p>Get started</p>
                            <p>Safe shopping</p>
                            <p>New Features</p>
                            <p>Frequently Asked Questions</p>

                        </div>


                        <div className="col-md-4">
                            <hr className="light"/>
                                <h5>Contact Us</h5>
                                <hr className="light"/>
                                    <p>650-669-5578</p>
                                    <p>goldchest@sjsu.edu</p>
                                    <p>1368 Marvin's Drive</p>
                                    <p>San José, CA, 95056</p>
                        </div>


                        <div className="col-md-4">
                            <hr className="light"/>
                                <h5>User Policy</h5>
                                <hr className="light"/>
                                    <p>Why Goldchest?</p>
                                    <p>Privacy & Policies</p>
                                    <p>Privacy Settings</p>
                                    <p>Our App</p>
                        </div>

                        <div className="col-12">
                            <hr className="light-100"/>
                                <h5>&copy; goldchest.com</h5>
                        </div>


                    </div>
                </div>
            </footer>

        )
    }
}


