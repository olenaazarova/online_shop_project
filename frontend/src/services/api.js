// db_URL = "http://online_shop_project-api-gateway-1:8080/api/items/";

// export const getItems = async () => {
//     const response = await fetch(db_URL);
//     const data = await response.json();
//     return data
// };

import axios from "axios"
import { data } from "react-router-dom";
const api = axios.create({baseURL: "http://localhost:8080"});

const getItems = () => {
    api.get('/api/items');
}

export const registerUser = async (user) => {
    let res = null;
    try{
        res = await api.post("/api/auth/register", user);
        console.log("api", res);
    } catch (error) {
        console.log(error);
    }
    return res;
}

export const loginUser = async (user) => {
    let res = null;
    try {
        res = await api.post("/api/auth/login", user);
        console.log("log api", res);
    } catch (error) {
        console.log(error);
    }
    return res
}

const fetchUser = async (token) => {
    let res = null; 
    try {
        res = await api.get("/api/auth/me", {headers: {"Authorization": `Bearer ${token}`}});
        console.log("log api", res);
    } catch (error) {
        console.log(error);
    }
    return res
}

// export default {registerUser, loginUser};
