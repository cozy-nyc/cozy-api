# API Documentation for the Cozy API

The Cozy API is meant to handle all the different requests that will be made with the backend. These requests communicate with the multiple different Django apps needed for the site.

The Django apps are ```accounts``` ```boards``` ```exchange``` ```services``` and ```stream```  

These Django apps could be found in the ```apps``` folder of this repository




### Boards
For all API calls involving Boards they will start with ```boards``` in the URL.
The following API involving boards are

- ```boards/list```: Returns a list of all of the boards. Ex.
```json
[
    {
        "id": 2,
        "name": "fashion",
        "tag": "fa"
    },
    {
        "id": 3,
        "name": "general",
        "tag": "g"
    },
    {
        "id": 1,
        "name": "tech",
        "tag": "t"
    }
]
```
- ```boards/info```: Returns service info along with a list of all boards. Ex.
```json
{
    "service": {
        "service": "boards",
        "status": "online",
        "message": {
            "important": false,
            "text": "Service is Online"
        }
    },
    "boards": [
        {
            "id": 2,
            "name": "fashion",
            "tag": "fa"
        },
        {
            "id": 3,
            "name": "general",
            "tag": "g"
        },
        {
            "id": 1,
            "name": "tech",
            "tag": "t"
        }
    ]
}
```
- ```boards/board/[Tag Of Board]```: Return general info of the specific board, as well as the active threads on the site.
```json
{
    "id": 3,
    "name": "general",
    "tag": "g",
    "threads": [
        {
            "id": 1,
            "bid": 0,
            "title": "hello all",
            "blurb": "i hate k-pop",
            "views": 0,
            "replyCount": 0,
            "imageCount": 0,
            "created": "2019-08-20T23:58:12.835225Z",
            "poster": {
                "id": 1,
                "username": "mem",
                "profileImg": null,
                "location": "Nowhere",
                "bio": ""
            },
            "board": 3,
            "image": null
        },
        {
            "id": 2,
            "bid": 1,
            "title": "anyone else voting for joe biden?",
            "blurb": "i love his stance on medicare",
            "views": 0,
            "replyCount": 0,
            "imageCount": 0,
            "created": "2019-08-20T23:58:42.711575Z",
            "poster": {
                "id": 1,
                "username": "mem",
                "profileImg": null,
                "location": "Nowhere",
                "bio": ""
            },
            "board": 3,
            "image": null
        }
    ]
}
```
