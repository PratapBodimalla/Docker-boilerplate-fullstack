import React, { createContext, useContext, useState } from "react";
import { createTheme, ThemeProvider as MUIThemeProvider } from "@mui/material/styles";

const ThemeContext = createContext();

const themes = {
    light: createTheme({
        palette: {
            mode: "light",
        },
    }),
    dark: createTheme({
        palette: {
            mode: "dark",
        },
    }),
};

export const ThemeProvider = ({ children }) => {
    const [theme, setTheme] = useState("light");

    const toggleTheme = () => {
        setTheme((prev) => (prev === "light" ? "dark" : "light"));
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            <MUIThemeProvider theme={themes[theme]}>{children}</MUIThemeProvider>
        </ThemeContext.Provider>
    );
};

export const useTheme = () => useContext(ThemeContext);
