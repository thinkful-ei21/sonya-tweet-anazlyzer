import React, { Component } from 'react';

import Spinner from 'react-spinkit';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      sentiment: null,
      loading: null,
      error: null,
      search: null
    }
  }


onSubmit(e) {
  e.preventDefault();
  this.setState({
    sentiment: null,
    loading: true,
    error: null,
    search: this.input.value
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
    this.input.value = "";
    console.log(sentiment.sentiment)
    if (sentiment.sentiment > 0) {
      console.log("positive")
      this.setState({
        sentiment: "positive",
        loading: false,
        error: null
      })
    } else {
      console.log("negative")
        this.setState({
          sentiment: "negative",
          loading: false,
          error: null
        })
      }
    })
  .catch(err => {
    console.log(err)
    this.setState({
      loading: false,
      error: "Uh oh, something went wrong..."
    })
  });
}


  render() {
    let message;
   
    if (this.state.loading) {
      message = <Spinner className="spinner" name="ball-grid-pulse" color="blue"/>
    } else if (this.state.sentiment) {
      message = <span className="result-message">Twitter is thinking {this.state.sentiment} things about {this.state.search}.</span>
    } else if (this.state.error) {
      message = <span className="error-message" >{this.state.error}</span>
    } 
    
    return (
      <React.Fragment>
        <form>
          <label htmlFor="search">Enter Search Term</label>
          <input type="text" name="search" ref={input => (this.input = input)}></input>
          <button type="submit" onClick={(e) => this.onSubmit(e)}>Submit</button>
        </form>
        <div className="result-container ">
          {message}
        </div>

      </React.Fragment>
      
    );
  }
}

export default App;
