import * as React from 'react';
import {useEffect, useState} from 'react';
import {PieChart} from '@mui/x-charts/PieChart';

export default function SurvivalDistribution() {

  const [gender, setGender] = useState<any[]>([])

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/passengers/distribution?axis=gender`)
      .then((res) => res.json())
      .then((data) => {
        setGender([
          {id: 0, value: data[0], label: 'Not survived'},
          {id: 1, value: data[1], label: 'Survived'},
        ])
      })
  }, [])

  if (gender.length === 0) {
    return <div>Loading...</div>
  }

  return (
    <article>
      <h1>Survival Distribution</h1>
      <PieChart
        series={[
          {
            data: gender
          },
        ]}
        width={400}
        height={200}
      />
    </article>
  );
}
