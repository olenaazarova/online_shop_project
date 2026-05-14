
function ItemCard({item}) {

    function onBuy() {
        alert('bought')
    }

    return <div className="item-card">
        <div className="item-imag">
            <img src={item.url}></img>
            <div className="item-to-buy">
                <button className="to-buy-btn" onClick={onBuy}>
                    buy
                </button>
            </div>
        </div>
        <div className="item-info">
            <p>{item.name}</p>
            <p>{item.price}</p>
        </div>
    </div>
}

export default ItemCard