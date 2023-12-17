import React from 'react';
import './App.css';
import PassengerTable from "./components/PassengerTable";
import PriceScatter from "./components/PriceScatter";
import Card from "./components/Card";
import Section from "./components/Section";

function App() {
  return (
    <Section>
      <Card>
        <PassengerTable/>
      </Card>
      <Card>
        <PriceScatter/>
      </Card>
    </Section>
  );
}

export default App;
