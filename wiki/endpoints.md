# Endpoints

## List

Request:

```bash
curl "http://127.0.0.1:1337/api/v1/?format=json" | json_pp
```

Response:

```json
{
   "exercises" : "http://127.0.0.1:1337/api/v1/exercises/?format=json",
   "users" : "http://127.0.0.1:1337/api/v1/users/?format=json",
   "plans" : "http://127.0.0.1:1337/api/v1/plans/?format=json",
   "days" : "http://127.0.0.1:1337/api/v1/days/?format=json"
}
```
