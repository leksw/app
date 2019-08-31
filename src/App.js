import React from 'react';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Routes from './routes';

const theme = createMuiTheme();

export default function App() {
  return (
    <MuiThemeProvider theme={theme}>
      <React.Fragment>
        <CssBaseline />
        <Routes />
      </React.Fragment>
    </MuiThemeProvider>
  );
}
