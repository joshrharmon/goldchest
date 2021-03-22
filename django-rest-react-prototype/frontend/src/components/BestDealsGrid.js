import React, {Component} from "react";

export class BestDealsGrid extends Component {
  html(deal){
    return (

      <div className="col-md-4 product-grid">

        <div className="image">
          <a href="#">
            <div className="overlay">
              <div className="detail">View Details</div>
            </div>
          </a>
        </div>
        <h5 className="text-center">{deal.title}</h5>
        <h5 className="text-center">{deal.price_low}</h5>
        <a href={deal.url} className="btn buy">VIEW DETAILS</a>

      </div>
    );
  }
  //<img src="images/sparklingwater.jpg" alt="description of picture" className="w-100"/>


  render() {
    console.warn(this.props.bestDealsList);
    const mapHTMLtoNrOfDeals = this.props.bestDealsList.map( deal => {
      return this.html(deal);
    });

    return(

      <div>

        <div className="container-fluid padding">
          <div className="row welcome text-center">
            <div className="col-12">
              <h1 className="display-4"> .</h1>
            </div>

            <div className="col-12">
              <p className="lead">See our hottest deals right now!</p>
            </div>
          </div>
        </div>

        <div className="row">
          {mapHTMLtoNrOfDeals}
        </div>

      </div>
    )
  }
}
