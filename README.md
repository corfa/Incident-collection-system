# Incident collection system


## Endpoints
### POST /problems
- Description: Save data to the database including headers and JSON body. Only headers and body will be provided.
### POST /find
- Description: Search for records in the database based on provided key-value pairs in the JSON body.
### GET /find2?h=hash
- Description: Retrieve records from the database that match the provided hash value.

## Running the Service
1) Create file ``` .env ``` from ``` .template.env ```
2) Run commnad ``` sudo docker-compose up --build ```