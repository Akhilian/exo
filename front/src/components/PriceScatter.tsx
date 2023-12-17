import React, {useEffect} from "react";
import {ScatterChart} from '@mui/x-charts';


const PriceScatter = () => {
  const data = [{
    id: 'data-0',
    x1: 329.39,
    y1: 443.28,
  }]

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/passengers/distribution?axis=`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
      })
  })

  return (
    <ScatterChart
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
