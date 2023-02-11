# Session Authentication Implementation 

Simple HTTP API for playing with `User` model. and Implementing the Session Auth


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model.
- `user_session.py`: user session model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints
- `views/session_auth.py`: all the endpoints for session manipulation.
- `auth/auth.py`: Base auth class
- `auth/basic_auth.py`: Base class for basic authentication
- `auth/session_auth.py`: base clas or session authentication
- `auth/session_db_auth.py`: session object for the DB.
- `auth/session_exp_auth.py`: Object for session expireration

## Setup

```
$ pip3 install -r requirements.txt
```
## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```



- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

#### Author