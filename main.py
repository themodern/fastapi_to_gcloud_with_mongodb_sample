from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    """
    Connect to MongoDB client on app startup and set the database instance on the app.
    """
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    """
    Close the MongoDB client connection on app shutdown.
    """
    app.mongodb_client.close()

# Include the 'book_router' into the FastAPI application
app.include_router(
    book_router,    # The router containing book-related routes
    tags=["books"], # Assign the tag "books" to these routes for documentation
    prefix="/book") # Set the URL prefix for these routes to "/book"
