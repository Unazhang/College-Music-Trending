### Get specific user info

GET /api/users/{id}/

Response

```json
{
    "id":"id",
    "name":"username",
    "tracks":[
    ...
    ]
}
```



### Add new user

Request

POST /api/users/

```json
{
    "name":"some user name",
    "apikey":"api key"
}
```

Response

```json
{
    "id":"id",
    "name":"username",
    "apikey":"apikey",
    "tracks":[
    ...
    ]
}
```

### Get Tracks

GET /api/tracks/

Response

```json
{
    "Tracks":[
        {
        "id": "id",
        "trackname": "track_name",
        "artist": "artist_name"
        },
        {
        "id": <id iter>,
        "trackname": "track_name",
        "artist": "artist_name"
        }
        ...
     ]
}
```

### Add Track to Database

Request

```json
{
    "trackname": "track_name",
    "artist": "artist_name"
}
```

Response

```json
{
    "Tracks":[
    ...,
    <New Added Track>
    ]
}
```


