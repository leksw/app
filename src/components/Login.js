import React, { useState, useContext } from 'react';
import { AuthContext } from './AuthProvider';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import { makeStyles } from '@material-ui/core/styles';
import FormControl from '@material-ui/core/FormControl';
import FormHelperText from '@material-ui/core/FormHelperText';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import useForm from 'react-hook-form';

const useStyles = makeStyles(theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  formControl: {
    margin: theme.spacing(1),
  },
  button: {
    margin: theme.spacing(1),
  },
}));

const base = 'http://localhost:8000';

const Login = props => {
  const classes = useStyles();
  const { history } = props;
  const { register, handleSubmit, errors } = useForm();
  const [state, setState] = useContext(AuthContext);
  const [snackbar, setSnack] = useState({
    open: false,
    message: '',
    vertical: 'bottom',
    horizontal: 'center',
  });

  const handleSnackbarClose = () => {
    setSnack({ ...snackbar, open: false });
  };

  const logIn = token => {
    setState({ ...state, token });
    localStorage.setItem('token', token);
  };

  const onSubmit = async data => {
    const authorization = await fetch(`${base}/auth/jwt/create/`, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (authorization.ok) {
      const { access } = await authorization.json();
      logIn(access);
      history.push('/');
    } else {
      const { detail } = await authorization.json();
      setSnack({ ...snackbar, message: detail, open: true });
    }
  };

  return (
    <Grid container direction="column" justify="center" alignItems="center">
      <Card>
        <form
          className={classes.container}
          noValidate
          autoComplete="off"
          onSubmit={handleSubmit(onSubmit)}>
          <FormControl
            className={classes.formControl}
            error={Boolean(errors.username)}>
            <InputLabel htmlFor="username">Username</InputLabel>
            <Input
              id="username"
              type="text"
              name="username"
              inputRef={register({ required: true })}
            />
            {errors.username && (
              <FormHelperText id="username-error">
                Username is required.
              </FormHelperText>
            )}
          </FormControl>

          <FormControl
            className={classes.formControl}
            error={Boolean(errors.password)}>
            <InputLabel htmlFor="password">Password</InputLabel>
            <Input
              id="password"
              type="password"
              name="password"
              inputRef={register({ required: true })}
            />
            {errors.password && (
              <FormHelperText id="password-error">
                Password is required.
              </FormHelperText>
            )}
          </FormControl>

          <Button
            type="submit"
            variant="contained"
            color="primary"
            className={classes.button}>
            Log in
          </Button>
        </form>
      </Card>
      <Snackbar
        anchorOrigin={{
          vertical: snackbar.vertical,
          horizontal: snackbar.horizontal,
        }}
        key={`${snackbar.vertical},${snackbar.horizontal}`}
        open={snackbar.open}
        onClose={handleSnackbarClose}
        ContentProps={{
          'aria-describedby': 'message-id',
        }}
        message={<span id="message-id">{snackbar.message}</span>}
      />
    </Grid>
  );
};

export default Login;
