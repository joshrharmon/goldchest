import React, {Component} from "react";
import { Link } from "react-router-dom";
import Cookies from "js-cookie";
import {GameInfo} from "../GameInfo";

// Profile component
export class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      steamid: "",

      steamName: "",
      displayName: "",
      avatar: "",
      wishlist: [],
      items: [],
      isLoaded: false

    }
  }

  componentDidMount() {
    const steamkey = 'B1C3A57FCE4FD0CBECBF1EE80507A691';
    const address =
      window.location.protocol + "//" + window.location.host + "/";
    console.log(address);

    fetch(address + 'steamid/')
      .then(res => {
        return res.json();
      })
      .then(steamid => {
        this.setState({ steamid: steamid }, function() {
          fetch('http://api.steampowered.com/ISteamUser/'
            + 'GetPlayerSummaries/v0002/'
            + '?key='
            + steamkey
            + '&steamids='
            + this.state.steamid)
            .then(res => {
              return res.json();
            })
            .then(json => {
              const player = json.response.players[0];

              // set profile info for this user
              this.setState({
                // steamName: player.profileurl
                //   .substring(30,player.profileurl.length - 1),
                displayName: player.personaname,
                avatar: player.avatarmedium
              });
            });


            //Recommendation fetch
            fetch('http://localhost:5000/rec?op=get&args=RECC&user=' + this.state.steamid + '&limit=6')
                .then(res => res.json())
                .then(json => {
                    this.setState({
                        isLoaded: true,
                        items: json,
                    })
                });

          // profile and wishlist data must be public for this to work
          fetch('https://store.steampowered.com/wishlist/profiles/'
            + steamid
            + '/wishlistdata/')
            .then(res => {
              return res.json();
            })
            .then(json => {
              const wishlist = Object.keys(json).map(function(k) {
                return json[k];
              });
              this.setState({wishlist: wishlist});
            })
          ;
        });
      })
    ;

    fetch(address + 'current_user/')
      .then(res => {
        return res.json();
      })
      .then(json => {
        this.setState({ username: json.username });
      })
    ;

    ;


  }


  render() {
    //for recomendation fetch
    var {isLoaded, items} = this.state;
    //for wishlist map html
    const wishlistGames = this.state.wishlist.map(game => {
      return <GameInfo
        key={game.name}
        title={game.name}
        art={game.capsule}
        tags={game.tags}
      />;
    });

    const wishlist = this.state.wishlist;
    const steamid = this.state.steamid;

    // handle a request to process the wishlist for the recomendation engine
    function processWishlist(e) {
      e.preventDefault();
      const address =
        window.location.protocol + "//" + window.location.host + "/";

      const csrftoken = Cookies.get('csrftoken');

      const data = {
        wishlist: wishlist,
        steamid: steamid
      }

      fetch(address + 'processWishlist/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
      });
    }

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
                          src={this.state.avatar}
                          className="img-radius" alt="User-Profile-Image"/></div>
                        <h6 className="f-w-600">{this.state.displayName}</h6>
                        <p>{this.state.steamName}</p> <i
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
                            <p className="m-b-10 f-w-600"></p>
                            <h6 className="text-muted f-w-400"></h6>
                            <h6 className="text-muted f-w-400"></h6>
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


          <div className="container-fluid padding">
              <div className="row welcome text-center">
                  <div className="col-12">

                  </div>
                  <div className="col-12">
                      <p className="lead"><b>Your current Steam wishlist</b></p>
                  </div>
              </div>
          </div>

          <div className="row">
              {wishlistGames}
          </div>



          <div className="container-fluid padding">
              <div className="row welcome text-center">
                  <div className="col-12">

                  </div>
                  <div className="col-12">
                      <p className="lead"><b>Recommended Games for YOU</b></p>

                      <button type="button" className="btn btn-outline-dark"
                              onClick={processWishlist}>Import wishlist recommendations
                      </button>

                  </div>
              </div>
          </div>


            <div className="row">
                {this.state.items.map((recGame) => (
                  <GameInfo
                    key={recGame.title}
                    title={recGame.title}
                    art={recGame.art}
                    currency={recGame.currency}
                    price={recGame.price_new}
                    price_cut={recGame.price_cut}
                    url={recGame.url}
                  />
              ))}

                </div>


      </div>



    )
  }
}
