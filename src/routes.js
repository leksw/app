import React from 'react';
import { BrowserRouter as Router, Switch } from 'react-router-dom';
import Header from './components/Header';
import Login from './components/Login';
import Home from './pages/Home';
import About from './pages/About';
import NoMatch from './pages/NoMatch';
import AuthedRoute from './components/AuthedRoute';
import UnauthedRoute from './components/UnauthedRoute';
import { AuthProvider } from './components/AuthProvider';

export default () => (
  <AuthProvider>
    <Router>
      <Header />
      <Switch>
        <AuthedRoute exact path="/" component={Home} />
        <AuthedRoute exact path="/about" component={About} />
        <UnauthedRoute path="/auth/login" component={Login} />
        <AuthedRoute component={NoMatch} />
      </Switch>
    </Router>
  </AuthProvider>
);
