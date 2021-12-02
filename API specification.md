### Get specific user info

GET /api/users/{id}/

Response

```json
{
    "id":"id",
    "name":"username"
    "tracks":[
    ...
    ]
}
```



### Add new user

Request

```json
{
    "name":"some user name"
}
```

Response

```json
{
    "id":"id",
    "name":"username"
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


