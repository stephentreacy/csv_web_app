FROM node:latest
COPY package*.json ./
RUN npm install
RUN npm install axios
COPY . .
EXPOSE 8080