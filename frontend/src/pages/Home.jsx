import './Home.css'
import '../style.css'
import ItemCard from "../components/ItemCard"
import { useState } from "react";

function Home() {

    const [searchQuery, setSearchQuery] = useState("")

    const items = [
        { id: 1, name: "laptop", price: 50, url: "https://techterms.com/img/xl/laptop_586.png" },
        { id: 2, name: "phone", price: 20, url: "https://miro.medium.com/v2/resize:fit:1200/1*53xRFGSOhc1RS1xlDN_Ixw.jpeg" },
        { id: 3, name: "tree", price: 5, url: "https://s3-eu-west-1.amazonaws.com/blog-ecotree/blog/0001/01/ad46dbb447cd0e9a6aeecd64cc2bd332b0cbcb79.jpeg" },
        { id: 4, name: "window", price: 40, url: "https://www.sheerwaterglass.co.uk/app/uploads/2023/11/anthracite-grey-slimline-window-copy.jpg" },
        { id: 5, name: "laptop", price: 50, url: "" },
        { id: 6, name: "phone", price: 20, url: "" },
        { id: 7, name: "tree", price: 5, url: "" },
        { id: 8, name: "window", price: 40, url: "" },
    ]

    const handleSearch = (e) => {
        e.preventDefault()
        alert(searchQuery)
    }

    return <div className="home">

        <div className='search-form-div'>
            <form onSubmit={handleSearch} className="search-form flex space-btwn">
                <input type="text" placeholder="Search for item..." className="search-input" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} />
                <button type="submit" className="typ-button">Search</button>
            </form>
        </div>

        <div className="items-grid flex space-btwn">
            {items.map(item => <ItemCard item={item} key={item.id} />)}
        </div>
    </div>
}

export default Home;