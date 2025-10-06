package main

import (
    "os"
    "log"
    "fmt"

    "github.com/gin-gonic/gin"
    "gorm.io/driver/sqlite"
    "gorm.io/gorm"
    "github.com/joho/godotenv"

    "comment-service/models"
    "comment-service/routes"
)

func main() {
    // Load environment variables from .env file
    if err := godotenv.Load(); err != nil {
        log.Println("No .env file found, using defaults or system env")
    }

    // Get DB path and port from env or fallback
    dbPath := os.Getenv("DB_PATH")
    if dbPath == "" {
        dbPath = "./database/comment.db"
    }

    port := os.Getenv("PORT")
    if port == "" {
        port = "5002"
    }

    // Ensure database folder exists
    os.MkdirAll("database", os.ModePerm)

    // Connect to SQLite
    db, err := gorm.Open(sqlite.Open(dbPath), &gorm.Config{})
    if err != nil {
        log.Fatal("Failed to connect database:", err)
    }

    // Auto-migrate schema
    db.AutoMigrate(&models.Comment{})

    // Setup router and middleware
    router := gin.Default()
    router.Use(corsMiddleware())

    // Register routes
    routes.CommentRoutes(router, db)

    // Run server on specified port
    log.Printf("Comment Service running on port %s", port)
    router.Run(fmt.Sprintf(":%s", port))
}

// Simple CORS middleware
func corsMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
        c.Writer.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

        if c.Request.Method == "OPTIONS" {
            c.AbortWithStatus(200)
            return
        }

        c.Next()
    }
}
 
