# Final Project Dicoding Belajar Back-End Pemula dengan Python: OpenShop RESTful API
This project is a final submission for dicoding bootcamp in learning back end using python.

## Case Study
As a Back-End Developer, you have decided to join the TSC (Technical Steering Committee) team in developing an e-commerce platform called OpenShop. As the name suggests, OpenShop will be a sales platform that is easily accessible to anyone and will allow sellers from various product categories to offer their goods online.

This application will be developed in stages, starting with basic features such as adding products, managing inventory, and creating product categories. In the future, OpenShop is expected to include features such as allowing users to create wishlists, filter product searches, and compare prices across stores. The application is designed to become one of the best sales platforms in the world!

In the first phase, the TSC team is responsible for building the core API for OpenShop. At this stage, the API will handle product management in the database, including features to add, delete, and update product information.

Your task is to design and build the API for OpenShop according to the criteria that will be explained in the following materials.

## Criteria
Please Check [Notion](https://www.notion.so/Kriteria-Submission-21fd83fecd5280dd8862ea4149bf7c59?source=copy_link)

## Run The Project

Clone the project

```bash
git clone https://github.com/Toru45/OpenShop-Submission-Dicoding-Django.git
```

Go to the project directory

```bash
cd OpenShop-Django-REST-API
```

### Run on local machine without docker

Install dependencies 

```bash
pip install -r requirements.txt
```

run database migration

```bash
python manage.py migrate
```

start the server:

```bash
python manage.py runserver
```

### Run With Docker

Build and run with docker compose:

```bash
docker-compose up --build
```

Go to [http://localhost:8000](http://localhost:8000)

## API Documentation
Kindly check the OpenAPI: [OpenAPI.yaml](./OpenAPI.yaml)

## Postman Testing
view the Postman collection here: [743 OpenShop API Test With Soft Delete.postman_collection.json](./postman/[743]%20OpenShop%20API%20Test%20With%20Soft%20Delete.postman_collection.json)
