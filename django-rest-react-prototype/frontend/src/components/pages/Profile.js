import React, {Component} from "react";
import { Link } from "react-router-dom";



export class Profile extends Component {





  constructor(props) {
    super(props);
    this.state = {
      username: "",
      steamid: "",

      steamName: "",
      displayName: "",
      avatar: "",
      wishlist: []
    }
  }


  componentDidMount() {
    const steamkey = 'B1C3A57FCE4FD0CBECBF1EE80507A691';

    fetch('http://localhost:8000/steamid/')
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
              this.setState({
                steamName: player.profileurl
                  .substring(30,player.profileurl.length - 1),
                displayName: player.personaname,
                avatar: player.avatarmedium
              });
            });

          // profile must be public
          fetch('https://store.steampowered.com/wishlist/profiles/'
            + steamid
            + '/wishlistdata/')
            .then(res => {
              console.log(res);
              return res.json();
            })
            .then(json => {
              const wishlist = Object.keys(json).map(function(k) {
                return json[k];
              });
              console.log(wishlist);
              this.setState({wishlist: wishlist});
            })
          ;
        });
      })
    ;
    fetch('http://localhost:8000/current_user/')
      .then(res => {
        console.log(res);
        return res.json();
      })
      .then(json => {
        console.log(json);
        this.setState({ username: json.username });
      })
    ;

    ;
  }

  render() {
    const wishlistGames = this.state.wishlist.map(game => {
      // console.log(game);
      return <Game key={game.name} name={game.name} image={game.capsule}/>;
    });

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

      </div>



    )
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div className="col-md-4 product-grid">
            <h5 className="text-center">{this.props.name}</h5>
            <img src={this.props.image} alt="" className="w-100" />

            <h5 className="text-center"></h5>
            <a href="" className="btn buy">BUY NOW</a>

        </div>
    )
  }
}
