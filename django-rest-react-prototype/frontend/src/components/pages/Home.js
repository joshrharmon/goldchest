import React, {Component} from "react";
import {Link, Route} from "react-router-dom";
import {CategoryGrid} from "../CategoryGrid";
import {BestDealsGrid} from "../BestDealsGrid";

import {BrowserRouter as Router} from "react-router-dom";


//In javascript you dont need to specify folders in this server
// just write name of nameofhtml to find href

//This is the Home component (aka startpage)
export class Home extends Component {

    thisFunctionShouldGetTheDataFromTheAPIOnTheServer()
    {
        //var responseFromServer = REPLACE_WITH_AJAX_REQUEST (== "{"data": "data"}")
        //var parsedJsonData = JSON.parse(responseFromServer);(== {data: "data"})
        /*
   $.ajax({
   url: url here, //localhost/getdata
   dataType: "json",
   success: function(data) {
   return parsedJSON  //(JSON.parse(responseFromServer);(== {data: "data"}))
   }.bind(this)
});*/
        var dumData = {
            data: {
                count: 6,
                list: [
                    {
                        price_low:10.5,
                        price_high: 15.0,
                        title: "Cyberpunk",
                        url: "https://store.steampowered.com/agecheck/app/1091500/"
                    },
                    {
                        price_low:11.5,
                        price_high: 17.0,
                        title: "Assassins Creed",
                        url: "https://store.steampowered.com/franchise/AC"
                    },
                    {
                        price_low:11.5,
                        price_high: 17.0,
                        title: "Kingdom Come",
                        url: "https://store.steampowered.com/agecheck/app/379430/"
                    },
                    {
                        price_low:10.5,
                        price_high: 15.0,
                        title: "Cyberpunk",
                        url: "https://store.steampowered.com/agecheck/app/1091500/"
                    },
                    {
                        price_low:11.5,
                        price_high: 17.0,
                        title: "Assassins Creed",
                        url: "https://store.steampowered.com/franchise/AC"
                    },
                    {
                        price_low:11.5,
                        price_high: 17.0,
                        title: "Kingdom Come",
                        url: "https://store.steampowered.com/agecheck/app/379430/"
                    }

                ],

            }};
        console.log(dumData);
        console.log(JSON.stringify(dumData));
        return dumData.data.list; //take top 6 best deals for our grid
    }

        render()
        {

            const bestDealsList = this.thisFunctionShouldGetTheDataFromTheAPIOnTheServer();
            return (

            <div>


                <CategoryGrid/>
                <BestDealsGrid bestDealsList={bestDealsList}/>



            </div>



        )
    }

}
