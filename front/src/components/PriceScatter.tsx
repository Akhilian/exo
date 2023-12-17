import React, {useEffect} from "react";
import {ScatterChart} from '@mui/x-charts';


const PriceScatter = () => {
  const data = [{
    id: 'data-0',
    x1: 329.39,
    y1: 443.28,
  }]

  useEffect(() => {
    fetch('http://localhost:8000/passengers/distribution?axis=fare')
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
      })
  })

  return (
    <ScatterChart
      width={600}
      height={300}
      series={[
        {
          label: 'Price',
          data: data.map((v) => ({ x: v.x1, y: v.y1, id: v.id })),
        },
      ]}
    />
  )
}

export default PriceScatter;
