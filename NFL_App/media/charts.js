var React = require('react');
var ReactDOM = require('react-dom');

/*
var Heading = React.createClass({
  render: function() {
    return <div><h3>Break Down</h3></div>
  }
});

var app = React.createClass({
  getInitialState: function() {
    return {
      data: null
    };
  },
  componentDidMount: function() {
    this.setState({data: 'Hi'});
  },
  render: function() {
  return <div><h1>HI</h1></div>
}
});
*/

var work = React.createClass({
  render: function() {
    return (
      <div><h3>{this.props.test}</h3></div>
    );
  }
});

ReactDOM.render(<work test="Please Work" />, document.getElementById('reactContainer'));
