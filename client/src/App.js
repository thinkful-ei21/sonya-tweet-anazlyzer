import React, { Component } from 'react';

import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      sentiment: null,
      loading: null
    }
  }
onSubmit(e) {
  e.preventDefault();
  this.setState({
    loading: true
  })
  console.log(this.input.value)
  fetch(`http://127.0.0.1:8000/analyze?search=${this.input.value}`, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    return response.json();
  })
  .then(sentiment => {
    if (sentiment > 0) {
      console.log("positive")
      this.setState({
        sentiment: "positive",
        loading: false
      })
    } else {
      console.log("negative")
        this.setState({
          sentiment: "negative",
          loading: false
        })
      }
    })
  .catch(err => console.log(err, "there's an error!"));
}


  render() {
    let message = ""
    if (this.state.loading === true) {
      message = "analyzing...."
    }
    return (
      <form>
        <label htmlFor="search">Enter Search Terms</label>
        <input type="text" name="search" ref={input => (this.input = input)}></input>
        <button type="submit" onClick={(e) => this.onSubmit(e)}>Submit</button>
        <span>sentiment value: {this.state.sentiment}</span>
        <p>{message}</p>
      </form>
    );
  }
}

export default App;
