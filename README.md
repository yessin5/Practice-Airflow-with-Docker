# Practice-Airflow-with-Docker
In this github repository, I wanted to share with you python scripts that I wrote while I'm learning Apache Airflow fundamentals. 
The installation of Airflow was done with docker (the most recommanded by experts)
To start, you have to be familiar with docker fundamentals.


- We launch Docker (green point appears), then you can downlaod the docker-compose.yaml (provided in the files below) file from the official docker website. In my case I did some modifications on the file to keep only the necessary features.
- We create the necessary files manually with this command:
  mkdir ./dags ./logs ./plugins
- When launching airlfow for the first time, you have to create a user account with this command:
  docker-compose up airflow-init
- When the creation is completed successfuly, you will see "exited with code 0", you scroll below to get the username and password to login through Airflow.
- If you already have an account, you simply launch Apache Airflow with docker-compose with the following commmand:
  docker-compose up -d
- To check if your container is ready, type the following command to display all the container and their statuses:
  docker ps
- Click on this link to open the Airflow UI:
  http://0.0.0.0:8080/
- The rest is easy, you have to write the python script for each DAG, check if there's errors and run it on the Airflow UI.
