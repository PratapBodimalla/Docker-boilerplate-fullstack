import React from "react";
import UserDataGrid from "./components/DataGrid";
import { useTheme } from "./themes/ThemeProvider";
import { Button } from "@mui/material";

const App = () => {
  const { toggleTheme } = useTheme();

  return (
    <div className="p-4">
      <header className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">User Management</h1>
        <Button variant="contained" onClick={toggleTheme}>
          Toggle Theme
        </Button>
      </header>
      <UserDataGrid />
    </div>
  );
};

export default App;
