import React, {useDeferredValue, useEffect, useState} from "react";
import {DataGrid, GridColDef} from '@mui/x-data-grid';
import {Grid, Slider} from "@mui/material";


const PassengerTable = () => {
  const [isLoaded, setIsLoaded] = useState(false);
  const [passengers, setPassengers] = useState([])
  const [filteredPassengers, setFilterPassengers] = useState([])
  const [columns, setColumns] = useState<GridColDef[]>([])
  const [fares, setFares] = React.useState<number[]>([0, 100]);
  const [faresFilter, setFaresFilter] = React.useState<number[]>([0, 100]);

  const deferredValue = useDeferredValue(filteredPassengers);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/passengers`)
      .then(async res => {

        setIsLoaded(true);

        if (res.status === 204) {
          return;
        }

        const body = await res.json()
        setPassengers(body)

        const prices = body.map((passenger: any) => {
          return passenger.fare
        })
        setFares([Math.min(...prices), Math.max(...prices)]);
        setFaresFilter([Math.min(...prices), Math.max(...prices)]);

        setColumns(Object.keys(body[0]).map((key) => {
          return {
            field: key,
            headerName: key,
          }
        }))
      })
  }, [])

  useEffect(() => {
    setFilterPassengers(passengers.filter((passenger: any) => {
      return passenger.fare >= faresFilter[0] && passenger.fare <= faresFilter[1]
    }))
  }, [passengers, faresFilter])

  if (isLoaded && passengers.length === 0) {
    return <div>No passengers found</div>
  }

  const handleChange = (event: Event, newValue: number | number[]) => {
    setFaresFilter(newValue as number[]);
  };

  return (
    <Grid container>
      <Grid item xs={4}>
        <strong>Fares</strong>
        <Slider aria-label="fares" value={faresFilter} onChange={handleChange} max={fares[1]} min={fares[0]}
                valueLabelDisplay="auto"/>
      </Grid>
      <Grid item className={"card"}>
        <DataGrid
          getRowId={(row) => row.passengerId}
          rows={deferredValue}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: {page: 0, pageSize: 10},
            },
          }}
          pageSizeOptions={[10, 30, 50]}
          checkboxSelection
        />
      </Grid>
    </Grid>
  )
}

export default PassengerTable;
