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







