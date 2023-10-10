FROM node:lts-alpine
WORKDIR /app
COPY ./djackets_vue /app
RUN npm install
RUN npm run serve

EXPOSE 8080
CMD [ "http-server", "dist" ]
