import React, { Component } from 'react';

import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      sentiment: null
    }
  }
onSubmit(e) {
  e.preventDefault();
  console.log(this.input.value)
  fetch(`http://127.0.0.1:8000/analyze/?search=${this.input.value}`, {
    method: 'GET',
    headers: {
      "Content-Type": "application/json"
    }
  })
  .then(res => this.setState({
    sentiment: res.value
  }))
  .catch(err => console.log(err));
}


  render() {
    return (
      <form>
        <label htmlFor="search">Enter Search Terms</label>
        <input type="text" name="search" ref={input => (this.input = input)}></input>
        <button type="submit" onClick={(e) => this.onSubmit(e)}>Submit</button>
        <span>sentiment value: {this.state.sentiment}</span>
      </form>
    );
  }
}

export default App;
