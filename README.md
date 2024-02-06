# Word Search using Djanog Rest Framework

This project is a Django-based web application that allows users to manage paragraphs of text and perform interactive searches within them. Users can register, log in, and create/search paragraphs. The application uses Docker for easy deployment and scalability.


## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker Engine: [Install Docker](https://docs.docker.com/get-docker/)

## Getting Started

To run this project locally using Docker, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
2. Build Docker Images:
   ```bash
   docker-compose build
3. Start the Docker containers:
   ```bash
   docker-compose up
4. The database migrations will automatically done by the docker itself.
5. Now we have to create superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
6. Now it will ask for the username, name and password:
   ```bash
   PS C:\projects\django\textsearch> docker-compose exec web python manage.py createsuperuser
   Email: admin@gmail.com
   Name: admin
   Password: ******
   Password (again):*****
   Creating superuser with password: demo@123
   Creating admin  with password: demo@123
7. now we can log in to the admin panel by using the end point  [http://localhost:8000/admin/](url):
8. The application should now be accessible at http://localhost:8000/.:
9. To stop the containers use:
   ```bash
   docker-compose down
   
