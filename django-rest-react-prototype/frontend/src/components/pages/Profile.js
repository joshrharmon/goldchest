import React, {Component} from "react";
import { Link } from "react-router-dom";


//This is the Home component (aka startpage)
export class Profile extends Component {
  render() {
    return (
      <div>
        <div className="page-content page-container" id="page-content">
          <div className="padding">
            <div className="row container d-flex justify-content-center">
              <div className="col-xl-6 col-md-12">
                <div className="card user-card-full">
                  <div className="row m-l-0 m-r-0">
                    <div className="col-sm-4 bg-c-lite-green user-profile">
                      <div className="card-block text-center text-white">
                        <div className="m-b-25"><img
                          src="https://img.icons8.com/bubbles/100/000000/user.png"
                          className="img-radius" alt="User-Profile-Image"/></div>
                        <h6 className="f-w-600">iLoveVideoGamez123</h6>
                        <p>John Smith</p> <i
                          className=" mdi mdi-square-edit-outline feather icon-edit m-t-10 f-16"></i>
                      </div>
                    </div>
                    <div className="col-sm-8">
                      <div className="card-block">
                        <h6 className="m-b-20 p-b-5 b-b-default f-w-600">User Account Profile</h6>
                        <div className="row">
                          <div className="col-sm-6">
                            <p className="m-b-10 f-w-600">Email</p>
                            <h6 className="text-muted f-w-400">iLoveVideoGamez123@gmail.com</h6>
                          </div>
                          <div className="col-sm-6">
                            <p className="m-b-10 f-w-600">Phone</p>
                            <h6 className="text-muted f-w-400">98979989898</h6>
                          </div>
                        </div>
                        <h6 className="m-b-20 m-t-40 p-b-5 b-b-default f-w-600">Goldchest</h6>
                        <div className="row">
                          <div className="col-sm-6">
                            <p className="m-b-10 f-w-600">Address</p>
                            <h6 className="text-muted f-w-400">1460 Balboa Park Sunnyvale CA</h6>
                          </div>
                          <div className="col-sm-6">
                            <p className="m-b-10 f-w-600">Wishlist</p>
                            <h6 className="text-muted f-w-400">Red Dead Redemption 2</h6>
                            <h6 className="text-muted f-w-400">Valheim</h6>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
