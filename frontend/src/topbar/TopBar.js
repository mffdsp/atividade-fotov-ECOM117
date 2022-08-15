import React from "react";
import makeStyles from "@material-ui/core/styles/makeStyles";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';

const pages = ['Dashboard', 'History', 'Settings'];

const useStyles = makeStyles((theme) => ({
  edgeAppBar: {
    background: 'white',
  },
  topBarButton: {
    color: '#008EEA',
  }
}));

export default function ButtonAppBar() {
  const classes = useStyles();

  return (
    <AppBar position="static" className={classes.edgeAppBar}>
      <Toolbar>
        	<Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {pages.map((page) => (
              <Button
                key={page}
                className={classes.topBarButton}
                // onClick={handleCloseNavMenu}
              >
                {page}
              </Button>
            ))}
          </Box>
      </Toolbar>
    </AppBar>
  );
}