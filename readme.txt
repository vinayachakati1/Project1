This project includes 3 files:
1. OEC_Main.py
   Python code to solve three questions asked in the assignment	
2. Dockerfile
   Dockerfile with Python3 as the base image.
   Application is configured on this image.
3. docker-compose.yml
   Builds the docker image and starts the application OEC_Main.py

Instructions for executing the project:

1. To run the script as a stand-alone application.
	python OEC_Main.py
2. To start the docker container and run the application.
	docker-compose up
3. To create the docker image
	docker build .


