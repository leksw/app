import React, { useContext, useEffect } from 'react';
import { Redirect, Route } from 'react-router-dom';
import { AuthContext } from './AuthProvider';

const base = 'http://localhost:8000';

const AuthedRoute = ({ component: Component, loading, ...rest }) => {
  const [state, setState] = useContext(AuthContext);
  const { token } = state;

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) return;
    fetch(`${base}/auth/jwt/verify/`, {
      method: 'POST',
      body: JSON.stringify({ token: token }),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then(res => {
      if (res.ok) {
        setState({ ...state, token });
      } else {
        localStorage.removeItem('token');
      }
    });
  }, []);

  // if (!token) {
  //   setState({ ...state, token: token });
  // }

  // const localToken = localStorage.getItem('token');
  const isAuthed = Boolean(token);

  return (
    <Route
      {...rest}
      render={props =>
        loading ? (
          <p>Loading...</p>
        ) : isAuthed ? (
          <Component history={props.history} {...rest} />
        ) : (
          <Redirect
            to={{
              pathname: '/auth/login',
              state: { next: props.location },
            }}
          />
        )
      }
    />
  );
};

export default AuthedRoute;
