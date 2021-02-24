import React, { Component } from "react";
import { render } from "react-dom";
import {Navbar} from "./Navbar";
import {Home} from "./pages/Home";
import {Signin} from "./pages/Signin";

//import react router
//Import react router
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import {Link} from "react-router-dom";




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

         
    <ul>
        {this.state.data.map(contact => {
          return (
            <li key={contact.id}>
              {contact.name} - {contact.email}
            </li>
          );
        })}
    </ul>
        </div>
        </Router>

        

    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
