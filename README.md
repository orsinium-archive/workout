
## Run server

1. Apply migrations:
    ```
    sudo docker-compose run workout-project migrate
    ```
2. Run server:
    ```bash
    sudo docker-compose up workout-project
    ```
3. Open API: [127.0.0.1:1337/api/v1/](http://127.0.0.1:1337/api/v1/)

## Run tests

```bash
sudo docker-compose run --entrypoint tox workout-project
```

## Make requests

1. Add user:
    ```bash
    sudo docker-compose run workout-project createsuperuser
    ```
1. Get token:
    ```bash
    curl -X POST -d "username=USER&password=PASSWORD" http://127.0.0.1:1337/api/v1/token/obtain/
    ```
1. Get endpoints:
    ```bash
    curl -H "Authorization: JWT <your_token>" http://127.0.0.1:1337/api/v1/ | json_pp
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
