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
from fastapi.encoders import 

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
        json_compatible_item_data = jsonable_sncoder(item)
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










