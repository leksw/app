import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import { PrivateRoute } from '../components/PrivateRoute';
import Header from './components/Header';
import Login from './pages/Login';
import Home from './pages/Home';
import About from './pages/About';
import NoMatch from './pages/NoMatch';

export default () => (
  <Router>
    <Header />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/about" component={About} />
      <Route path="/login" component={Login} />
      <Route component={NoMatch} />
    </Switch>
  </Router>
);
