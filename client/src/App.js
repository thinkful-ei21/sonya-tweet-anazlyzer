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
  fetch("http://127.0.0.1:8000/analyze/", {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({search: this.input})
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
        <button type="submit" onSubmit={(e) => this.onSubmit}>Submit</button>
        <span>sentiment value: {this.state.sentiment}</span>
      </form>
    );
  }
}

export default App;
