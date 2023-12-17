import React, {useEffect, useState} from "react";
import {DataGrid, GridColDef} from '@mui/x-data-grid';


const PassengerTable = () => {

  const [isLoaded, setIsLoaded] = useState(false);
  const [passengers, setPassengers] = useState([])
  const [columns, setColumns] = useState<GridColDef[]>([])

  useEffect(() => {
    fetch('http://localhost:8000/passengers')
      .then(async res => {

        setIsLoaded(true);

        if (res.status === 204) {
          return;
        }

        const body = await res.json()
        setPassengers(body)
        setColumns(Object.keys(body[0]).map((key) => {
          return {
            field: key,
            headerName: key,
          }
        }))
      })
  }, [])

  if(isLoaded && passengers.length === 0) {
    return <div>No passengers found</div>
  }

  return (
    <DataGrid
      getRowId={(row) => row.passengerId}
      rows={passengers}
      columns={columns}
      initialState={{
        pagination: {
          paginationModel: {page: 0, pageSize: 10},
        },
      }}
      pageSizeOptions={[10, 30, 50]}
      checkboxSelection
    />
  )
}

export default PassengerTable;
