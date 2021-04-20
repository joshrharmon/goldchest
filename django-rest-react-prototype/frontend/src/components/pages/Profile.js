import React, {Component} from "react";
import { Link } from "react-router-dom";


//This is the Home component (aka startpage)
export class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      steamid: ""
    }
  }

  componentDidMount() {
    fetch('http://localhost:8000/steamid/')
      .then(res => {
        console.log(res);
        return res.json();
      })
      .then(steamid => {
        this.setState({ steamid: steamid });
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
  }

  render() {
      return (
        <div>
          <h1> Welcome to your profile!</h1>
          <p>{this.state.username}</p>
          <p>{this.state.steamid}</p>
        </div>
      )
  }
}
