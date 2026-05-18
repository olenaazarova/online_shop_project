# online_shop_project
<img width="1501" height="751" alt="APZ_schema drawio" src="https://github.com/user-attachments/assets/b7fd9b59-b497-427c-aaca-fada5b16f9fa" />

To run:
```
docker compose -f .\docker-compose.yml up
```

commands:
```
curl -H "Content-Type: application/json" -d "{"""title""":"""try""","""price""":10,"""quantity""":12}" http://localhost:8080/api/items/
curl http://localhost:8080/api/search/?q=try
```
