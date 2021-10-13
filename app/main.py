############################################## Python script to create API #############################################

'''
The script implements API for customer data using FastAPI module
'''

########################################################################################################################

### Importing required modules

# 3rd party libraries
from fastapi import FastAPI, status, HTTPException          # Required to create and API and handle status
from pydantic import BaseModel                              # Type hints
from typing import Optional                                 # Type annotations
from fastapi.encoders import jsonable_encoder               # Encoding data as JSON
from fastapi.responses import JSONResponse                  # Creating a JSON response 

########################################################################################################################

class Customer(BaseModel):
    '''
    Class to define customer entity
    ...

    Attributes
    ----------
    customer_id (str):
        Unique identifier of the customer
    country (str):
        Country to which the customer belongs
    '''

    customer_id: str
    country: str


class URLLink(BaseModel):
    '''
    Class defined url where customer information is stored
    ...

    Attributes
    ----------
    url (optional) (str):
        url to the link where customer information is stored
    '''

    url: Optional[str] = None


class Invoice(BaseModel):
    '''
    Class to define invoice entity
    ...

    Attributes
    ----------
    invoice_no (int):
        Unique indentifier of the invoice
    invoice_date (str):
        date when the invoice was generated
    customer (str):
        Information of the customer
    '''

    invoice_no: str
    invoice_date: str
    customer: Optional[URLLink] = None


# Define a dictionary which will contain the invoice data
invoice_table = dict()

# Creating FastAPI instance
app = FastAPI()


########################################################################################################################


### Functions to create API methods

@app.get("/")
async def root() -> dict:
    '''
    Function to return message on base URL
    ...

    Parameters
    ----------
    None

    Returns
    -------
    Dictionary
    '''

    return {"message": "Hello World"}


@app.post("/customer")
async def create_customer(item: Customer) -> str:
    '''
    Function to add a new customer
    ...

    Parameters
    ----------
    Customer

    Returns
    -------
    JSON data
    '''

    # Encode the create customer item in JSON
    # and return it along with the status code 201
    json_compatible_item_data = jsonable_encoder(item)

    return JSONResponse(
                        content=json_compatible_item_data,
                        status_code=201
                    )


@app.get("/customer/{customer_id}")
async def read_customer(customer_id: str) -> str:
    '''
    Function to read data for a customer
    given a customer id
    ...

    Parameters
    ----------
    customer_id (str):
        ID of the customer

    Returns
    -------
    JSON data
    '''

    if customer_id == "12345":
        item = Customer(customer_id="12345", country="Germany")
        json_compatible_item_data = jsonable_encoder(item)
        return JSONResponse(
                            content=json_compatible_item_data,
                        )

    else:
        # Raise a 404 exception
        raise HTTPException(
                            status_code=404,
                            detail="Item not found"
                        )


@app.post("/customer/{customer_id}/invoice")
async def create_invoice(customer_id: str, invoice: Invoice) -> str:
    '''
    Function to create invoice for a customer
    ...

    Parameters
    ----------
    customer_id (str):
        ID of the customer
    invoice (object):
        object of type Invoice
    '''

    # Add the customer link to the invoice
    invoice.customer.url = "/customer/" + customer_id

    # Convert invoice instance into a JSON string
    json_invoice = jsonable_encoder(invoice)
    invoice_table[invoice.invoice_no] = json_invoice

    # Read the invoice from the store and return it
    ex_invoice = invoice_table[invoice.invoice_no]

    return JSONResponse(content=ex_invoice)


@app.get("/customer/{customer_id}/invoice")
async def get_invoices(customer_id: str) -> str:
    '''
    Function to get link of all the invoices
    given a customer id
    ...

    Parameters
    ----------
    customer_id (str):
        Unique identifier of the customer

    Returns
    -------
    JSON string containing list of all invoices
    '''

    # Create links to the actual invoice (get from database)
    ex_json = {
                "id_123456": "/invoice/123456",
                "id_789101": "/invoice/789101"
            }

    return JSONResponse(content=ex_json)


@app.get("/invoice/{invoice_no}")
async def read_invoice(invoice_no: str) -> str:
    '''
    Function to read invoice given
    a invoice number
    ...

    Parameters
    ----------
    invoice_no (str):
        ID of the invoice

    Returns
    -------
    JSON string containing invoice data
    '''

    ex_invoice = invoice_table[invoice_no]

    return JSONResponse(content=ex_invoice)


@app.get("/invoice/{invoice_no}/{stockcode}")
async def read_item(invoice_no: int, stockcode: str) -> str:
    '''
    Function to get stock based on code
    ...

    Parameters
    ----------
    invoice_no (int):
        Invoice number
    stockcode (str):
        Code of the invoice

    Returns
    -------
    JSON string containing the item data
    '''

    return {message: "Hello World"}


@app.post("/invoice/{invoice_no}/{stockcode}")
async def add_item(invoice_no: int, stockcode: str):
    '''
    Function to add item to the invoice
    ...

    Parameters
    ----------
    invoice_no (int):
        invoice number
    stockcode (str):
        code of the item

    Returns
    -------
    JSON string with added item data
    '''

    return {message: "Hello World"}
