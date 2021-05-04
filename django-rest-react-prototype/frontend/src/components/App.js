//Import react
import React, { Component } from "react";
import { render } from "react-dom";
//Import react router
import {BrowserRouter as Router, Switch, Route, useParams} from "react-router-dom";
//Import of category pages
import {Category} from "./pages/Categories/Category";


//Import navbar, sigin, home component/pages
import {Navbar} from "./Navbar";
import {Home} from "./pages/Home";
import {Signin} from "./pages/Signin";
import {Profile} from "./pages/Profile";
import {Footer} from "./Footer";


//import react router

//Import react router

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }


  render() {
    return (
      <Router>
        <div>

            <Navbar/>
            <Route path="/" exact component={Home}/>
            <Route path="/signin" component={Signin}/>
            <Route path="/:categoryID" component={Category}/>
            <Route path="/accounts/profile" component={Profile}/>
            <Footer/>

        </div>
      </Router>



    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
