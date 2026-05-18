db_URL = "http://online_shop_project-api-gateway-1:8080/api/items/";

export const getItems = async () => {
    const response = await fetch(db_URL);
    const data = await response.json();
    return data
};
