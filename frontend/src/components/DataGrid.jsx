import React, { useEffect } from "react";
import { observer } from "mobx-react-lite";
import { DataGrid } from "@mui/x-data-grid";
import userStore from "../stores/UserStore";

const UserDataGrid = observer(() => {
    useEffect(() => {
        userStore.fetchUsers();
    }, []);

    const columns = [
        { field: "id", headerName: "ID", width: 100 },
        { field: "name", headerName: "Name", width: 200 },
        { field: "email", headerName: "Email", width: 250 },
    ];

    return (
        <div className="h-[400px] w-full bg-gray-100 p-4 rounded-lg">
            <DataGrid
                rows={userStore.users}
                columns={columns}
                pageSize={5}
                rowsPerPageOptions={[5]}
            />
        </div>
    );
});

export default UserDataGrid;
