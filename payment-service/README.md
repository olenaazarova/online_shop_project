To send payment with curl:
```
curl -v -H "Content-Type: application/json" -d "{"""user_id""":10,"""payment_id""":11,"""amount""":-5,"""item""":"""laptop"""}" http://localhost:8000/
```