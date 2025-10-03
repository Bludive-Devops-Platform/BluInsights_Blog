package main

import (
    "os"
    "github.com/gin-gonic/gin"
    "gorm.io/driver/sqlite"
    "gorm.io/gorm"
    "comment-service/models"
    "comment-service/routes"
    "log"
)

func main() {
    // Ensure folder exists
    os.MkdirAll("database", os.ModePerm)

    db, err := gorm.Open(sqlite.Open("database/comment.db"), &gorm.Config{})
    if err != nil {
        log.Fatal("Failed to connect database:", err)
    }

    db.AutoMigrate(&models.Comment{})

    router := gin.Default()
    router.Use(corsMiddleware())

    routes.CommentRoutes(router, db)

    router.Run(":5002") // Comment Service runs on port 5002
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
