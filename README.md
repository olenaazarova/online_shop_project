# online_shop_project
<img width="1258" height="652" alt="image" src="https://github.com/user-attachments/assets/b9d3cdc7-aecc-40e5-adc4-63ccc4325b2a" />

To run:
```
docker compose -f .\docker-compose.yml up
```

commands:
```
curl -H "Content-Type: application/json" -d "{"""title""":"""try""","""price""":10,"""quantity""":12}" http://localhost:8080/api/items/
curl http://localhost:8080/api/search/?q=try
curl -H "Content-Type: application/json" -d "{"""email""":"""try@gmail.com""","""password""":"""trypass""","""first_name""":"""12""","""last_name""":"""last"""}" http://localhost:8080/api/auth/register
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwMDIzNmNmNC1iMDIyLTQzZmEtYWJhMi0yYjhlZGQzNWExMGUiLCJlbWFpbCI6InRyeUBnbWFpbC5jb20iLCJzaWQiOiIwNDBlYzNmOS1iNDcwLTQ2YzktOTZmMy1jZWMzOGI4ODA2NDEiLCJpYXQiOjE3NzkxOTc3NjIsImV4cCI6MTc3OTIwNDk2Mn0.y9GzjY7MPG1SvOoRizd2kG98cluem47ODPSVmBbW5Is" http://localhost:8080/api/auth/me
```
