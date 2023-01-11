"""
You own a small online store, consisting of its own site and a bunch of products presented on it. Your task is to
retrieve all the products that are currently contained in the store using the provided REST API.

The current site contains the products represented by the following fields:

id - the unique identifier of the product (integer);
name - the name of the product (string);
updated_at - timestamp of the last product update (integer);
price - the price of the product (positive integer);
manufacturer (optional) - the name of the manufacturer. This field is optional, and if it is not presented, then the product is considered to be produced locally, by yourself.
To obtain information about the current products from the site, you are given an API endpoint. Use HTTP requests to obtain information about the current products from this endpoint.

API information

The API is served at http://127.0.0.1:8081 and supports the only endpoint:

A GET request of the form http://127.0.0.1:8081/products

This endpoint returns a JSON array, containing a list of JSON objects representing the information about the product with the fields described above.

For example, the response for this endpoint may look like:

[
  {
    "id": 1,
    "name": "ProductName",
    "updated_at": 150000000,
    "price": 100,
    "manufacturer": "ManufacturerCompanyName"
  },
  {
    "id": 3,
    "name": "ProductName 2",
    "updated_at": 150000230,
    "price": 90
  }
]
Your task is to request an API endpoint and print the information of all the products in the following format:

Product <name> has price <price> and no manufacturer
if product has no manufacturer field, and

Product <name> has price <price> and manufacturer <manufacturer>
otherwise.

The information about the products should be returned in the same order as the products were returned in response.

Example

If the response from http://127.0.0.1:8081/products is

[
  {"id": 1, "updated_at": 1565641075, "price": 110, "manufacturer": "m2", "name": "Product1"},
  {"id": 2, "updated_at": 1565645377, "price": 100, "name": "Product2"}
]
The following should be printed to the standard output:

Product Product1 has price 110 and manufacturer m2
Product Product2 has price 100 and no manufacturer
[execution time limit] 12 seconds (py3)
"""
import requests

# import mysql.connector

url = 'http://127.0.0.1:8081/products'
r = requests.get(url)
# Product <name> has price <price> and no manufacturer
