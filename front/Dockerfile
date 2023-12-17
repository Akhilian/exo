FROM node:18-alpine as builder
ENV NODE_ENV=production

WORKDIR /app
COPY package*.json ./

RUN npm install --omit=dev

COPY . .

RUN npm run build

FROM nginx:stable-alpine-slim as production
ENV NODE_ENV=production

WORKDIR /usr/share/nginx/html

COPY --from=builder /app/build .

