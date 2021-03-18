//Import react
import React, { Component } from "react";
import { render } from "react-dom";
//Import react router
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
//Import of category pages
import {Sports} from "./pages/Categories/Sports";
import {Adventure} from "./pages/Categories/Adventure";
import {Action} from "./pages/Categories/Action";
import {Strategy} from "./pages/Categories/Strategy";
import {Childrens} from "./pages/Categories/Childrens";
import {Horror} from "./pages/Categories/Horror";
import {Racing} from "./pages/Categories/Racing";
import {Shooter} from "./pages/Categories/Shooter";
import {Anime} from "./pages/Categories/Anime";
import {RPG} from "./pages/Categories/RPG";
import {Mystery} from "./pages/Categories/Mystery";
import {Puzzle} from "./pages/Categories/Puzzle";
//Import navbar, sigin, home component/pages
import {Navbar} from "./Navbar";
import {Home} from "./pages/Home";
import {Signin} from "./pages/Signin";
import {Footer} from "./Footer";
import {CategoryGrid} from "./CategoryGrid";




class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/lead")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
        <Router>
        <div>


            <Navbar/>
            <Route path="/" exact component={Home}/>
            <Route path="/signin" component={Signin}/>
            <Route path="/sports" component={Sports}/>
            <Route path="/adventure" component={Adventure}/>
            <Route path="/action" component={Action}/>
            <Route path="/strategy" component={Strategy}/>
            <Route path="/childrens" component={Childrens}/>
            <Route path="/horror" component={Horror}/>
            <Route path="/racing" component={Racing}/>
            <Route path="/shooter" component={Shooter}/>
            <Route path="/anime" component={Anime}/>
            <Route path="/rpg" component={RPG}/>
            <Route path="/mystery" component={Mystery}/>
            <Route path="/puzzle" component={Puzzle}/>


            <Footer/>

        </div>
        </Router>



    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
