
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

```
sudo docker-compose run workout-project test
```

## TODO

1. i18n
1. docs
1. docstrings
