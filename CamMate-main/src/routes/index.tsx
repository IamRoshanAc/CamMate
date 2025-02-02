import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import './index.css';
import App from './App'; 

const isAuthenticated = !!localStorage.getItem('token'); 

ReactDOM.render(
  <Router>
    <App isAuthenticated={isAuthenticated} />
  </Router>,
  document.getElementById('root')
);
