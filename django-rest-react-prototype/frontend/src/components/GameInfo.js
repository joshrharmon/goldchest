import React, {Component} from "react";

export class GameInfo extends Component {
  render() {
    const isDeal = this.props.price_cut != undefined;
    const hasPrice = this.props.price != undefined;

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
      </div>
    );
  }

}
