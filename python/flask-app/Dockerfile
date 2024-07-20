# base image 
FROM python:3.11

#working directory 
WORKDIR /app

#copy code in to the container
COPY . /app

#required library
RUN pip install Flask

# run 
CMD ["python","app.py"]

