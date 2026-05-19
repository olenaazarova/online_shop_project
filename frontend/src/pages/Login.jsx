import "./Register.css"
import "../style.css"
import { loginUser } from "../services/api";
import { useNavigate } from "react-router-dom";
// import { useState } from 'react';

function Login() {

    const navigate = useNavigate();
    // const [token, setToken] = useState("");

    const handleForm = (event) => {
        event.preventDefault();
        let form = event.target;
        let formData = new FormData(form);
        // console.log(formData);
        let formDataObj = Object.fromEntries(formData.entries());
        // console.log(formDataObj)    
        // let formJson = JSON.stringify(formDataObj);
        // console.log(formJson);
        let res = registerUser(formDataObj).then(res => {
            console.log("res:", res);

            if (res !== null) {
                sessionStorage.setItem('token', res.data.token)
                navigate("/profile");
            }
        });
    }

    let token = sessionStorage.getItem('token');
    console.log(token);
    if (token !== null) {
        return <p>Already registered or logged in</p>
    }

    return <div className="register">
        <form onSubmit={handleForm} className="register-form">
            <div className="register-items">
                <div className="register-item">
                    <label htmlFor="email">Email: </label>
                    <input name="email" type="text" placeholder="..." className="search-input"/>
                </div>
                <div className="register-item">
                    <label htmlFor="password">Password: </label>
                    <input name="password" type="password" placeholder="..." className="search-input"/>
                </div>
            </div>

            <button type="submit" className="typ-button submit-button">Register</button>
        </form>
    </div>
}

export default Login