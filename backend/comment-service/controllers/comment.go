package controllers

import (
    "net/http"
    "strconv"
    "time"

    "github.com/gin-gonic/gin"
    "gorm.io/gorm"
    "comment-service/models"
)

// Capitalized: GetComments → exported
func GetComments(db *gorm.DB) gin.HandlerFunc {
    return func(c *gin.Context) {
        postID := c.Param("postId")
        postIDInt, err := strconv.Atoi(postID)
        if err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid post ID"})
            return
        }

        var comments []models.Comment
        if err := db.Where("post_id = ?", postIDInt).Order("created_at desc").Find(&comments).Error; err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusOK, comments)
    }
}

func AddComment(db *gorm.DB) gin.HandlerFunc {
    return func(c *gin.Context) {
        postID := c.Param("postId")
        var input struct {
            UserID string `json:"user_id" binding:"required"`
            Text   string `json:"text" binding:"required"`
        }
        if err := c.ShouldBindJSON(&input); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }

        postIDInt, err := strconv.Atoi(postID)
        if err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid post ID"})
            return
        }

        comment := models.Comment{
            PostID:    postIDInt,
            UserID:    input.UserID,
            Text:      input.Text,
            CreatedAt: time.Now(),
        }
        if err := db.Create(&comment).Error; err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }

        c.JSON(http.StatusOK, comment)
    }
}