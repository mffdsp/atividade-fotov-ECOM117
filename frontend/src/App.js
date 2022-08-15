import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Box from '@material-ui/core/Box';
import TopBar from "./topbar/TopBar"
import Dashboard from "./dashboard/Dashboard"

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: '#f0f2f5',
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  }
}));

function App() {

  const classes = useStyles();

  return (
    <Box component="main" className={classes.root}>
      <TopBar />
      <Dashboard />
    </Box>
  );
}

export default App;