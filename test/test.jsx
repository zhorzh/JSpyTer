// vanilla JS
test = [1,2,3]
[1, 2, 3].map(n => n + 1)

// JSX
require('react')
const profile = (
  <div>
    <img src="avatar.png" className="profile" />
  </div>
)

// ES6
const a = 1
let b = 2
console.log(a, b)

let colors = ['red', 'green', 'blue']
for (const color of colors.reverse()) {
  console.log(color)
}

// ES6 and react
import React from 'react'
class Hello extends React.Component {
  render() {
    return React.createElement('div', null, `Hello ${this.props.toWhat}`);
  }
}

// JSX and react
require('react')
var createReactClass = require('create-react-class');
var Greeting = createReactClass({
  render: function() {
    return <h1>Hello, {this.props.name}</h1>;
  }
});

// JSX, ES6 and react
import React from 'react'
class Greeting extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
