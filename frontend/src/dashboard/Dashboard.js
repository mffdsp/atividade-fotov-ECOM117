import React from 'react';
import makeStyles from "@material-ui/core/styles/makeStyles";
import Container from '@material-ui/core/Container'
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';

import CustomBarChart from '../custom-components/bar-chart';

const useStyles = makeStyles((theme) => ({
  card:{
    display: 'flex',
    flexDirection: 'column',
    height: 240,
  },
  chartContainer:{
    width: "100%",
    maxHeight: 300,
  }
}));

export default function Dashboard(props) {

    const classes = useStyles();

    return (
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Grid container spacing={3}>

          <Grid item xs={12} md={4} lg={3}>
            <Card variant="outlined" className={classes.card}>
              <CardHeader
                title="Yield today"
              />
            </Card>
          </Grid>

          <Grid item xs={12} md={8} lg={9}>
            <Card variant="outlined" className={classes.card}>
              <CardHeader
                title="Total Yield"
              />
              <CardContent>
                <CustomBarChart/>
              </CardContent>
            </Card>
          </Grid>

        </Grid>
      </Container>
    );

}