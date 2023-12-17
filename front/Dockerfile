FROM node:18-alpine as builder

WORKDIR /app
COPY package*.json ./

RUN npm install --omit=dev

COPY . .
RUN npm run build

FROM nginx:stable-alpine-slim as production
WORKDIR /usr/share/nginx/html
COPY --from=builder /app/build .

