# Step 1: Use official Node.js LTS image
FROM node:18-alpine

# Step 2: Set working directory in container
WORKDIR /usr/src/app

# Step 3: Copy package.json and package-lock.json first (for caching)
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install --production

# Step 5: Copy source code
COPY ./src ./src
COPY .env ./

# Step 6: Expose port (match your .env PORT)
EXPOSE 5050

# Step 7: Start the service
CMD ["node", "src/app.js"]

