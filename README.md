# O que foi feito?

Adicionamos a bibiloteca hoborequest (https://pypi.org/project/hoborequest/) visando utilizar a api para se conectar a hobo 
Além disso foi desenvolvida a [task](https://github.com/mffdsp/atividade-fotov-ECOM117/blob/38be61c4faf40b524f58cc91dd707563d03b33d6/backend/photovoltaic/tasks.py#LL16C5-L16C16) reponsável por utilizar os dados de tests para criar um arquivo sql que pode ser consumido pelo front-end, por exemplo:
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
3. Download one of the following files and place it in backend/photovoltiac/fixtures:
   - Test base (3 MB) - https://drive.google.com/file/d/1rPe2IlhOtALpPcjzeP-zLbujPSX8CWND/view?usp=sharing
   <!-- - All years (795 MB) - https://drive.google.com/file/d/1Ne9b_Mv0qp1ImplhGeUuO4pvkTM0-J6P/view?usp=sharing
   - 2021 (286 MB) - https://drive.google.com/file/d/1iTPnPmYXK7hf_k4qasRIPR1ih7nu6j6w/view?usp=sharing -->
4. Load backup data, run ```python manage.py loaddata base_name.json``` to load it into your database.

You can run a task to simulate the input of PV data in the Django admin page
1. Go to http://localhost:8000/admin 
2. In Periodic tasks click on the Add button
3. Put a name of your choice and select "photovoltaic.tasks.simulate_input" in Task (registered)
4. Create a 1-minute Interval Schedule
5. Lastly, save

# Obtendo dados da estação

Além disso, também foram feitas requisições dos dados da estação por meio do estudo da documentação do webservice e uso do playground disponível para testes (https://webservice.hobolink.com/ws/data/info/index.html#). Abaixo segue um passo a passo de como conseguimos obter esses dados:

- Primeiro, obtivemos o access_token necessário para a requisição usando o seguinte comando: ```curl -i -H "Content-type: application/x-www-form-urlencoded" -H "Accept: application/json" -d "grant_type=client_credentials&client_id=PUT-HERE-YOUR-CLIENT-ID&client_secret=PUT-HERE-THE-CLIENT-SECRET" -X POST https://webservice.hobolink.com/ws/auth/token```

- Depois, acesse o link do playground acima e insira os parâmetros necessários para a sua requisição. A figura abaixo ilustra uma requisição bem sucedida:

Request:

![image](https://github.com/mffdsp/atividade-fotov-ECOM117/assets/45469441/c6d13aff-7a01-439d-87e0-3b76290e6622)

Response:

![image](https://github.com/mffdsp/atividade-fotov-ECOM117/assets/45469441/2665d639-bc75-4d2f-8249-a8695a81b8b1)

