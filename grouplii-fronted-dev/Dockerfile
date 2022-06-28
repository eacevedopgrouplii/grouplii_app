FROM node:14.16 as build
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install --save vue-barcode-reader vue-stepper vuelidate 
COPY . ./
RUN npm run build

#FROM nginx:1.19
#COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
FROM nginx:alpine
COPY ./nginx/nginx.conf /etc/nginx/conf.d/configfile.template

COPY --from=build /app/dist /usr/share/nginx/html

ENV PORT 8080
ENV HOST 0.0.0.0
EXPOSE 8080
CMD sh -c "envsubst '\$PORT' < /etc/nginx/conf.d/configfile.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"


