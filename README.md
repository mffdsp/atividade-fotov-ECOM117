# Softex - Photovoltaic forecaster
This repository contains everything needed to deploy and run the project.  
  
## Development  
To run the application in a development environment, simply use the command:  
  
```  
docker-compose up  
```  
If the images for the containers aren't created already, the ```up``` command will create them automatically. Changes like new requirements or changes in the build process (Dockerfile) require a rebuild, for that you should use the ```docker-compose build``` command.
  
If this is your first time deploying the project, you should follow the steps below in order to setup your database and Django application:  
1. Run the command ```docker-compose run --rm backend /bin/bash```.
2. Migrate the database, run the command ```python manage.py migrate```. 
2. Create a superuser, run the ```python manage.py createsuperuser``` command to create one.  
3. Load backup data, run ```python manage.py loaddata json_base.json``` to load it into your database.  