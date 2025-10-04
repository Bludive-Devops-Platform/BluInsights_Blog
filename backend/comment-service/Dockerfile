# ----------------------
# Stage 1: Build the Go binary
# ----------------------
FROM golang:1.24.7-alpine3.21 AS builder

# Enable CGO and install build dependencies
ENV CGO_ENABLED=1
ENV GOOS=linux
ENV GOARCH=amd64

RUN apk add --no-cache gcc musl-dev

# Set working directory
WORKDIR /app

# Copy go.mod and go.sum first to leverage caching
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy the rest of the source code
COPY . .

# Build the Go binary
RUN go build -o comment-service main.go

# ----------------------
# Stage 2: Minimal runtime image
# ----------------------
FROM alpine:3.21

# Set working directory
WORKDIR /app

# Copy the built binary from builder
COPY --from=builder /app/comment-service .

# Expose port
EXPOSE 5002

# Command to run the service
CMD ["./comment-service"]
 
