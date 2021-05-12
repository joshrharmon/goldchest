import React, {Component} from "react";

export class GameInfo extends Component {
  constructor(props) {
    super(props);
    this.state =
      { tags: ''
      , username: ''
      , steamid: ''
      };

    this.like = this.like.bind(this);
  }

  componentDidMount() {
    if (this.props.category != undefined) {
      // prefer category if we have it
      this.setState({tags: [this.props.category]});
    } else if (this.props.tags != undefined) {
      // use tags if we have them
      this.setState({tags: this.props.tags});
    } else {
      // get the genres using game steam ID
      const gameID = "57690"; // TODO: extract ID from url
      fetch("https://store.steampowered.com/api/appdetails?appids=" + gameID)
        .then(res => res.json()).then(json => {
          const tags = json[gameID].data.genres.map(obj => obj.description);
          this.setState({tags: tags});
        });
    }
  }


  like(e) {
    e.preventDefault();
    console.log(this.state.tags);
    const address =
      window.location.protocol + "//" + window.location.host + "/";

    fetch(address + 'current_user/')
      .then(res => {
        return res.json();
      })
      .then(json => {
        if (json.username) {
          fetch(address + 'steamid/')
            .then(res => {
              return res.json();
            })
            .then(steamid => {
              console.log('steamid:', steamid);
            });
          // TODO:
          // IF they are logged in, call REST endpoint to update database with
          // these tags and steam ID (I'll need to create this REST endpoint)
        }
      })
    ;
  };

  render() {
    const isDeal = this.props.price_cut != undefined;
    const hasPrice = this.props.price != undefined;
    const tags = this.state.tags;


    return (
      <div className="col-md-4 product-grid">
      <h5 className="text-center">{this.props.title}</h5>
        <img src={this.props.art} alt="" className="w-100" />

        { hasPrice &&
          ( isDeal
          ? <h5 className="text-center">NOW {this.props.currency}{this.props.price} {this.props.price_cut} OFF </h5>
          : <h5 className="text-center">PRICE {this.props.currency}{this.props.price}</h5>
          )
        }

      <a href={this.props.url} className="btn buy">BUY NOW</a>
      <button onClick={this.like}>Like</button>
      </div>
    );
  }

}
