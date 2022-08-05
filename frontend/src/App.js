import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Box from '@material-ui/core/Box';
import TopBar from "./topbar/TopBar"
import Dashboard from "./dashboard/Dashboard"

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    height: '100%',
    flexDirection: 'column',
    backgroundColor: '#f0f2f5'
  }
}));

function App() {

  const classes = useStyles();

  return (
    <div className={classes.root}>
      <TopBar />
      <Dashboard />
    </div>
  );
}

export default App;