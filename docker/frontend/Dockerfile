# Use the official Node.js image as the base image
FROM node:18

# Set the working directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY frontend/package*.json ./

RUN npm ci

# Bundle app source
COPY . .