import React from 'react';
import './App.css';
import PassengerTable from "./components/PassengerTable";
import SurvivalDistribution from "./components/SurvivalDistribution";
import {Grid} from '@mui/material';

function App() {
  return (
    <Grid container className="section">
      <Grid item xs={12}>
        <PassengerTable/>
      </Grid>
      <Grid item xs={4} className={"card"}>
        <SurvivalDistribution/>
      </Grid>
    </Grid>
  );
}

export default App;
