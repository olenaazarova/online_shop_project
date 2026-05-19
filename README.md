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
curl -H "Content-Type: application/json" -d "{"""email""":"""try@gmail.com""","""password""":"""trypass""","""first_name""":"""12""","""last_name""":"""last"""}" http://localhost:8080/api/auth/register
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwMDIzNmNmNC1iMDIyLTQzZmEtYWJhMi0yYjhlZGQzNWExMGUiLCJlbWFpbCI6InRyeUBnbWFpbC5jb20iLCJzaWQiOiIwNDBlYzNmOS1iNDcwLTQ2YzktOTZmMy1jZWMzOGI4ODA2NDEiLCJpYXQiOjE3NzkxOTc3NjIsImV4cCI6MTc3OTIwNDk2Mn0.y9GzjY7MPG1SvOoRizd2kG98cluem47ODPSVmBbW5Is" http://localhost:8080/api/auth/me
```
