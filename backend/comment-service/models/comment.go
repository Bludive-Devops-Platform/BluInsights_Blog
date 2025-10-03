package models

import "time"

type Comment struct {
    ID        int       `json:"id" gorm:"primaryKey;autoIncrement"`
    PostID    int       `json:"post_id"`
    UserID    string    `json:"user_id"`
    Text      string    `json:"text"`
    CreatedAt time.Time `json:"created_at"`
}