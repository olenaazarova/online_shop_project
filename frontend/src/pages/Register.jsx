import "./Register.css"
import "../style.css"

function Register() {
    return <div className="register">
        <form className="register-form" action="">
            <div className="register-items">
                <div className="register-item">
                    <label htmlFor="name">Name: </label>
                    <input name="name" type="text" placeholder="..." className="search-input"/>
                </div>
                <div className="register-item">
                    <label htmlFor="surname">Surname: </label>
                    <input name="surname" type="text" placeholder="..." className="search-input"/>
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