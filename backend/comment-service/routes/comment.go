package routes

import (
    "github.com/gin-gonic/gin"
    "gorm.io/gorm"
    "comment-service/controllers"
)

func CommentRoutes(router *gin.Engine, db *gorm.DB) {
    router.GET("/comments/:postId", controllers.GetComments(db))
    router.POST("/comments/:postId", controllers.AddComment(db))
}