# Get Base image 
FROM openjdk:17-jdk-alpine

#Working dir 
WORKDIR /app

#copy codeino the container
COPY src/main.java /app/Main.java

#compile code 
RUN javac Main.java

#Run 
CMD ["java","Main"]
