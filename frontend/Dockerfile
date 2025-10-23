# Use official Nginx image as base
FROM nginx:1.29.2-alpine
RUN apk upgrade --no-cache libxml2 libxslt expat

# Set working directory in container
WORKDIR /usr/share/nginx/html

# Remove default Nginx static files
RUN rm -rf ./*

# Copy frontend files to Nginx html directory
COPY . .

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]

