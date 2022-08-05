import React, { PureComponent } from 'react';
import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import makeStyles from "@material-ui/core/styles/makeStyles";
import Box from '@material-ui/core/Box'
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  card:{
    width: '80%',
    height: '50%'
  },
  chartContainer:{
    width: "100%",
    maxHeight: 300,
  }
}));

const data = [
  {
    name: 'Page A',
    uv: 4000,
    pv: 2400,
    amt: 2400,
  },
  {
    name: 'Page B',
    uv: 3000,
    pv: 1398,
    amt: 2210,
  },
  {
    name: 'Page C',
    uv: 2000,
    pv: 9800,
    amt: 2290,
  },
  {
    name: 'Page D',
    uv: 2780,
    pv: 3908,
    amt: 2000,
  },
  {
    name: 'Page E',
    uv: 1890,
    pv: 4800,
    amt: 2181,
  },
  {
    name: 'Page F',
    uv: 2390,
    pv: 3800,
    amt: 2500,
  },
  {
    name: 'Page G',
    uv: 3490,
    pv: 4300,
    amt: 2100,
  },
  ];

export default function Dashboard(props) {

    const classes = useStyles();

    return (
      <Box sx={{ flexGrow: 1 }}>
        <Grid container spacing={2} direction="row" justifyContent="center" alignItems="center">
          <Grid item xs={4}>
            <Card variant="outlined" className={classes.card}>
              <CardHeader
                title="Day"
              />
            </Card>
          </Grid>
          <Grid item xs={8}>
            <Card variant="outlined" className={classes.card}>
              <CardHeader
                title="Chart"
              />
              <CardContent>
                <ResponsiveContainer width="100%" height={400}>
                  <BarChart data={data}>
                      <Bar dataKey="uv" fill="#8884d8" />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Box>
    );

}