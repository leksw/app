import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import Button from '@material-ui/core/Button';
import { AuthContext } from './AuthProvider';

const AuthButton = () => {
  const [state, setState] = useContext(AuthContext);
  const { token } = state;

  const logOut = () => {
    setState({ ...state, token: null });
    localStorage.removeItem('token');
  };

  return Boolean(token) ? (
    <Button color="inherit" onClick={logOut} component={Link} to="/auth/login">
      Logout
    </Button>
  ) : (
    <Button color="inherit" component={Link} to="/auth/login">
      Login
    </Button>
  );
};

export default AuthButton;
