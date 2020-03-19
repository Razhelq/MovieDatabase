To run the application you basically need to clone the repository and run 

    docker-compose up

To run in locally, install packages listed in requirements.txt and run

    python manage.py runserver
    
The application will be available under localhost:8000 URL


This app provides to logged users a possibility to search for movies and add/remove them to/from favourites.
It also gives a possibility to log in using facebook and google (only while running locally at the moment).
