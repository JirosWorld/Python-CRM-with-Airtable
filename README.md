# crm-course

CRM HTML

Start by cloning this repo

git clone https://github.com/skolo-online/crm-course.git

### Start

Install all the requirements

`$ virtualenv appenv`

    $ source appenv/bin/activate

`$ pip install flask`

`$ pip install requests`

`$ pip freeze`

### Create local config

To keep your API-key secret:

Add inside your file config.py, in the first class Config Object:
`AIRTABLE_KEY = 'keyiiiiaaaa'`

See your users table:
http://192.168.178.59:8888/users

## Youtube tutorials

part 1: https://www.youtube.com/watch?v=1hjC1J5FfQ0

part 2: https://www.youtube.com/watch?v=WKpWtZ7V79w

first create empty databases on Airtable.

Tool: https://www.uuidgenerator.net/

## Get Airtable API

CreateReadUpdateDelete
https://airtable.com/

Airtable generated documntation for these tables:

https://airtable.com/app4vQ4CtiTItA8Rn/api/docs#curl/metadata

## About this app

It's pure Python with Flask, without any Django

- Running on http://127.0.0.1:8888
- Running on http://192.168.178.59:8888

## Explanation about the data

The date is returned as a JSON object (becasue the GET method comes as a text object from the json.loads request method) with an array inside:

    {
    "records": [
        {
            "id": "recQBDSc7p2MuRhpJ",
            "createdTime": "2023-03-31T13:07:58.000Z",
            "fields": {
                "FirstName": "Big",
                "Priority": "1",
                "JobDescription": "CEO",

You can GET individual fields from the Records array like such:

`result['records'][0]['fields']['FirstName']`

### POST

For posting import 'request' from Flask

`from flask import Flask, render_template, redirect, url_for, request`

'request' without an 's' is an object from the Flask methods, which is very different from 'requests' with an s which is a library to perform the API calls.

-
