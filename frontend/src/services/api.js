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

const registerUser = async (user) => {
    let res = await api.post("/api/auth/register", user);
    console.log(res);
}

export default registerUser;