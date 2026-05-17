import "./ItemCard.css"
import "../style.css"

function ItemCard({item}) {

    function onBuy() {
        alert('bought')
    }

    return <div className="item-card space-btwn">
        <div className="item-imag">
            <img src={item.url}></img>
        </div>
        <div className="item-description space-arnd">
            <div className="item-info">
                <p>{item.name}</p>
                <p>{item.price}</p>
            </div>
            <div className="item-to-buy">
                <button className="to-buy-btn" onClick={onBuy}>
                    buy
                </button>
            </div>
        </div>
    </div>
}

export default ItemCard