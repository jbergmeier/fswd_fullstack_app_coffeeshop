# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. DONE Create a new Auth0 Account
2. DONE Select a unique tenant domain
   https://jbe.eu.auth0.com/authorize?audience=Drinks&response_type=token&client_id=KfdmrtBtLZ1BHiBcnnuiaOIF8cE1zI77&redirect_uri=http://localhost:8100/login-results
3. DONE Create a new, single page web application
4. DONE Create a new API
   - in API Settings:
     - DONE Enable RBAC
     - DONE Enable Add Permissions in the Access Token
5. DONE Create new API permissions:
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. DONE Create new roles for:
   - DONE Barista
     - DONE can `get:drinks-detail`
   - DONE Manager
     - DONE can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
     - barista@theapi.com (Coffee123!)
       - eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FTXdRa1ZFT0VKRU1USkROakpGTkRRME4wWkNPVGswTUVZeVJVRkVOekkwUXpaRk1FVTFOQSJ9.eyJpc3MiOiJodHRwczovL2piZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhZGRmY2QwMmIxNzcwYmU0NzU5NzEyIiwiYXVkIjoiRHJpbmtzIiwiaWF0IjoxNTg4NDUzMzMxLCJleHAiOjE1ODg0NjA1MzEsImF6cCI6IktmZG1ydEJ0TFoxQkhpQmNubnVpYU9JRjhjRTF6STc3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6W119.Up61BFuPDFEYfENOeQ9o1rVp6ZplEQj802wiWIsJwOip_q8gNwzWUOHz33-5gTTI_L7nlI_KWmJnu6wSB7G6C4q1E7OlKWhxBlgG5qx02u1LN_Wv4NZmeFyQns6Ik0kmEKoxSwsEgCr_3LggiqYVaQS61hul3Bd5QOxT-mBZzpLpTOqTkUwE0cfsqlSbS2dwkJn-h2gmi0AxsiG5R_SRSeygvj7NTfZnEnqRBUd2V534OXiCNpOYNwtehVSgBuHzoqApSWLaueVaKp5L-8XwxGSzDKnWPYih8B7Ez4bODCKVR5LJd5apHH9GfMr2Jepnubm_uxIoB-cN_plVJ-RWLA
     - coffeemanager@theapi.com (Coffee123!)
       - eeyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FTXdRa1ZFT0VKRU1USkROakpGTkRRME4wWkNPVGswTUVZeVJVRkVOekkwUXpaRk1FVTFOQSJ9.eyJpc3MiOiJodHRwczovL2piZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhZGUwOTJlYWY4NTEwYmU3ZTk4NGFmIiwiYXVkIjoiRHJpbmtzIiwiaWF0IjoxNTg4NTA3OTQ3LCJleHAiOjE1ODg1MTUxNDcsImF6cCI6IktmZG1ydEJ0TFoxQkhpQmNubnVpYU9JRjhjRTF6STc3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6W119.OE8z1XjdiPlXysW0Hw4nkA5sl-LSd4Ieoh4BO2YyU3q00V-itg22h7xk5A5wlK0Nl3IY7bCmsr1GMS8MGhIHS8a6P6LNOZKOjfyrZ6iLgCq5fMHE83sJLANbJxQpEJjdAbECdnK1fKj6Oz6PqvTc6q4pcYV4obuLXS84C9U9tDS6tbDKJFCDH8wQ9_wLQEu60ksdaEFNQE4JPvqeffrn8V3gIWB3PI6ayfLpsraV94J3Xjru5IW3ihBWPgK3jNs9AlqQGw_rxENRH-lo_rp6gPM4Kd42o5HeyfqVD3O_HLGd8SAXvGLzbBUKdM_lVcSFqR-eGNXH4DBGyya3F38fpg
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
