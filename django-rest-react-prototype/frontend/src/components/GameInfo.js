import React, {Component} from "react";

export class GameInfo extends Component {
  constructor(props) {
    super(props);
    this.state = { tags: '' };
  }

  componentDidMount() {
    if (this.props.tags != undefined) {
      this.setState({tags: this.props.tags});
    } else {
      const gameID = "57690"; // TODO: regex match on url
      fetch("https://store.steampowered.com/api/appdetails?appids=" + gameID)
        .then(res => res.json()).then(json => {
          const tags = json[gameID].data.genres.map(obj => obj.description);
          this.setState({tags: tags});
        });
    }
  }

  render() {
    const isDeal = this.props.price_cut != undefined;
    const hasPrice = this.props.price != undefined;
    const tags = this.state.tags;

    function like(e) {
      e.preventDefault();
      console.log(tags);
      // TODO:
      // get their steam ID IF they are logged in
      // IF they are logged in, call REST endpoint to update database with
      // these tags and steam ID (I'll need to create this REST endpoint)
    };

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
      <button onClick={like}>Like</button>
      </div>
    );
  }

}
