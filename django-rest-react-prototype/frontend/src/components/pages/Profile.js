import React, {Component} from "react";
import { Link } from "react-router-dom";


//This is the Home component (aka startpage)
export class Profile extends Component {
    componentDidMount() {
      fetch('http://localhost:8000/current_user/', {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
        .then(res => {
          console.log(res);
          return res.json();
        })
        .then(json => {
          console.log(json);
        })
        // .then(json => {
        //   this.setState({ username: json.username });
        // })
      ;
    }

    render() {
        return (

            <div>
                <h1> Welcome to your profile!</h1>




            </div>



        )
    }
}
