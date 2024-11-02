# Mini Address Book API
This API provides endpoints for storing, retrieving, updating, and deleting addresses.
## Getting Started
### Prerequisites
- Docker must be installed on your system
### Set Up
The following are done in the terminal.
1. **Clone the repository into a folder:**
```
git clone https://github.com/komronm8/myRateAPI.git
cd myRateAPI
```
2. **Build and run the Docker container:**
```
docker-compose up --build
```
3. **Verify the application is running**
After the container is running, you can verify the app by visiting [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger). This should direct you to the API's Swagger documentation.

### Using the API
The API documentation allows you to interact with the individual available endpoints and their request formats as well as their responses. Therefore you can test the API directly and get detailed information from the API documentation. Initially, in the database, two dummy address entries are available.

## Exploring the Endpoints
The Swagger UI displays all available endpoints, including:
* POST /address - Creates a new address
* GET /address/all - List of all addresses currently stored
* GET /address/{id} - Retrieves detail of address by ID
* PUT /address/{id} - Updates address detail by ID
* DELETE /address/{id} - Deletes the address entry by ID
