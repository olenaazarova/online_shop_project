import { Link } from "react-router-dom"
import "./Profile.css"
import "../style.css"

function Profile() {
    return <div className="profile-main">
        <div className="buttons">
            <Link to="/register">
                <button className="profile-btn typ-button">Register</button>
            </Link>
            <Link>
                <button className="profile-btn typ-button">Login</button>
            </Link>
        </div>
    </div>;
}

export default Profile;