import { Link } from "react-router-dom"
import "./Profile.css"
import "../style.css"

function Profile() {

    let token = sessionStorage.getItem('token');
    // console.log(token);
    if (token !== null) {
        return <p>Already registered or logged in</p>
    }

    return <div className="profile-main">
        <div className="buttons">
            <Link to="/register">
                <button className="profile-btn typ-button">Register</button>
            </Link>
            <Link to="/login">
                <button className="profile-btn typ-button">Login</button>
            </Link>
        </div>
    </div>;
}

export default Profile;