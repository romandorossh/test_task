To implement this task I've decided to use DRF as an API backend. Django ORM was used to create models to store data for textual service.
It implements basic CRUD operations as requested. I've created textual_service.py as a module to hold logic responsible for processing/stroring texts. It relies on DBRepository as an abstraction to store data. Currently I use sqllite as a database but with this solution 
it can be easily switched to other more production ready databases. There is an other LanguageDetector class which is responsible for language detection. In future it can be moved into it's own API, but for this task it resides in a seperate module and is used in textual_service alongside DBRepository. I've used pytest to create integration tests. I've implemented this solution to work with Docker.
Instructions:

1) To run tests: 
    `docker-compose -f docker-compose-tests.yml up`
2) To run application in semi-production mode(API will be available on port 8001 over http ):
    `docker-compose up`
API will be available uder the link:
    `http://127.0.0.1:8001/snippets/`

For now semi-production mode it uses nginx as a reverse-proxy and gunicorn as a webserver for our textual API.
Current approach uses only http, but can be easily changed to work with https as well. The same goes for the Database.
Currently it uses sqllite but this can be changed to use a production ready database.

If we are talking about a full production mode I would use some kind of container orchestration tool like k8s to properly make use of multiple nodes/machines that are availabe.
Our Textual API would be one pod, database an other. We could also place LanguageDetector into its own API(or grpc in case if it's internal use only) and pod  

