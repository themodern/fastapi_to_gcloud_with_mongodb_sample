![main workflow](https://github.com/mongodb-developer/pymongo-fastapi-crud/actions/workflows/main.yml/badge.svg)

# PyMongo with FastAPI CRUD application

This is a simple CRUD application built using PyMongo and FastAPI. You can also follow the step-by-step [tutorial](https://www.mongodb.com/languages/python/pymongo-tutorial) for building this application.

## Running the server

Set your [Atlas URI connection string](https://docs.atlas.mongodb.com/getting-started/) as a parameter in `.env`. Make sure you replace the username and password placeholders with your own credentials.

```
ATLAS_URI=mongodb+srv://<username>:<password>@sandbox.jadwj.mongodb.net
DB_NAME=pymongo_tutorial
```

Install the required dependencies:

```
python -m pip install -r requirements.txt
```

Start the server:
```
python -m uvicorn main:app --reload
```

When the application starts, navigate to `http://localhost:8000/docs` and try out the `book` endpoints.

## Running the tests

Install `pytest`:

```
python -m pip install pytest
```

Execute the tests:

```
python -m pytest
```

## Disclaimer

Use at your own risk; not a supported MongoDB product

######################################

sending the docker container to gcloud
1. Build the Docker image with the command below
```
docker build -t gcr.io/PROJECT_ID/IMAGE_NAME .
```

2. Push the Docker image to GCR
```
docker push gcr.io/PROJECT_ID/IMAGE_NAME
```

3. Deploy the docker image to gcloud
variables: 
3.1 PROJECT_ID  
to check your project_id on gcloud:
```
gcloud config list project
```
3.2 IMAGE_NAME
that is the image_name you have put in step 1

3.3 REGION
the gcloud service deployment region, google will give you hint if you miss it. 
we will use australia-southeast1
```
gcloud run deploy SERVICE_NAME --image gcr.io/PROJECT_ID/IMAGE_NAME --platform managed --region REGION --allow-unauthenticated --set-env-vars KEY1=VALUE1,KEY2=VALUE2
```