FROM node:16
WORKDIR /app
COPY ./djackets_vue /app
WORKDIR /app/djackets_vue
RUN npm install
CMD ["npm", "run", "serve"]

EXPOSE 8080
