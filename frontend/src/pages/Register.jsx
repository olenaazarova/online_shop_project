import "./Register.css"
import "../style.css"
import registerUser from "../services/api";

function Register() {

    const handleForm = (event) => {
        event.preventDefault();
        let form = event.target;
        let formData = new FormData(form);
        // console.log(formData);
        let formDataObj = Object.fromEntries(formData.entries());
        console.log(formDataObj)    
        // let formJson = JSON.stringify(formDataObj);
        // console.log(formJson);
        registerUser(formDataObj);
    }

    return <div className="register">
        <form onSubmit={handleForm} className="register-form">
            <div className="register-items">
                <div className="register-item">
                    <label htmlFor="first_name">Name: </label>
                    <input name="first_name" type="text" placeholder="..." className="search-input"/>
                </div>
                <div className="register-item">
                    <label htmlFor="last_name">Surname: </label>
                    <input name="last_name" type="text" placeholder="..." className="search-input"/>
                </div>
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

export default Register