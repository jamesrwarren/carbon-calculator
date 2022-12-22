# template-flask-web-app

## Basic web app for the purpose of learning

I aim to create a fully featured form based web app using only Flask (and it's dependencies) and psycopg2-binary.

The aim is to create our own form validation, ORM, authentication and user access controls. 
We will try to align ourselves over time to an MVC model of app development.  

The reasons for this is to properly understand the concepts underlying an MVC framework rather just using one.

## Progress

This is a work in progress but I would consider the template complete when we have the following:

### Pipeline

Will probably use github actions for this.

- Precommit hooks
- Linting
- Unit tests
- Build and packaging
- Automatic tagging and versioning
- Sending to docker repository
- Deploy to free hosting (maybe heroku? multiple envs? journey tests?)

### Tests

Start doing TDD.

- Unit tests with pytest
- Behaviour driven user journey tests (using behave?)

### Authentication

Create our own session based auth stored server side.

- Postgres initially but then Redis for session storage

### Frontend

As much barebones as possible. No idea about any of this stuff yet...

- JS (do we need ajax? no idea)
- Bootstrap for CSS?

### ORM

Let's make our own. Could be totally dumb but understand that we need to be able to push entities 
to the DB and retrieve them and use them as objects. Should be good abstraction of the DB layer. 

- Maybe Flask SQLAlchemy as later learning but like the idea of trying to make a simple version of our own

### Layers

Let's split frontend and backend

- Frontend can display results of API calls 
- Backend can have objects for each entity

### Infrastructure

Probably do this last

- Maybe build free infra in AWS

#### --- Issues to fix ---

What is up with gunicorn? Makes requests super slow, reverting to straight flask for now till I work it out.