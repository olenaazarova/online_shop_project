// import './Home.css'
import ItemCard from "../components/ItemCard"

function Home() {

    const items = [
        {id: 1, name: "laptop", price: 50},
        {id: 2, name: "phone", price: 20},
        {id: 3, name: "tree", price: 5},
        {id: 4, name: "window", price: 40},
    ]

    return <div className="home">

        <form action="" className="search-form">
            <input type="text" placeholder="Search for item..." className="search-input"/>
            <button type="submit" className="search-btn">Search</button>
        </form>

        <div className="items-grid">
            {items.map(item => <ItemCard item={item} key={item.id}/>)}
        </div>
    </div>
}

export default Home;