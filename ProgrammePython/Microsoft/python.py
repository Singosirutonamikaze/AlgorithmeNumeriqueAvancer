# Create a web API using FastAPI with a route to products.
from fastapi import FastAPI
app = FastAPI()

@app.get("/products")
def read_products():
    return []


















