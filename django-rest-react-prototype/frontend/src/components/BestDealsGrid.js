


import React, {Component} from "react";

export class BestDealsGrid extends Component
{


    html(deal){
        return (

            <div className="col-md-4 product-grid">

            <h5 className="text-center">{deal.title}</h5>
                <img src={deal.art} alt="" className="w-100" />

                <h5 className="text-center">NOW ${deal.price_new} SAVE ${deal.price_cut}</h5>
            <a href={deal.urls.buy} className="btn buy">BUY NOW</a>
            
        </div>
        );
    }


    render()
    {
        console.warn(this.props.items);
        const mapHTMLtoNrOfDeals = this.props.items.map( deal => {

            return this.html(deal);

        } );



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
