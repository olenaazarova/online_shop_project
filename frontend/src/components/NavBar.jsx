import { Link } from "react-router-dom"
import './NavBar.css'
import '../style.css'

function NavBar() {
    return <nav className="navbar flex">
        <div className="navbar-inner flex space-btwn">
            <div className="navbar-logo">
                <Link to="/">Online shop</Link>
            </div>
            <div className="navbar-links flex space-btwn">
                <Link to="/" className="nav-link">Home</Link>
                <Link to="/cart" className="nav-link">Cart</Link>
            </div>
        </div>
    </nav>
}

export default NavBar