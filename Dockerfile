# Use an official Python runtime as a parent image
FROM python:3

#STEP1 Install required packages
RUN pip install numpy
RUN pip install pandas


# Copy the python script into the container at /app
COPY OEC_Main.py /usr/src/app/

# Set the working directory to /app
WORKDIR /usr/src/app


# Make port 8585 vailable to the world outside this container
EXPOSE 8585


# Run application  when the container launches
CMD ["python","OEC_Main.py"]
