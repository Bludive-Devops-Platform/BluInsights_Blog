from sqlalchemy.orm import Session
from . import models, schemas

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.BlogPost(
        title=blog.title,
        content=blog.content,
        tags=blog.tags,
        author=blog.author,
        image_url=blog.image_url
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.BlogPost).order_by(models.BlogPost.created_at.desc()).offset(skip).limit(limit).all()

def get_blog(db: Session, blog_id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == blog_id).first()

def update_blog(db: Session, blog_id: int, blog_update: schemas.BlogUpdate):
    blog = db.query(models.BlogPost).filter(models.BlogPost.id == blog_id).first()
    if not blog:
        return None
    if blog_update.title is not None:
        blog.title = blog_update.title
    if blog_update.content is not None:
        blog.content = blog_update.content
    if blog_update.tags is not None:
        blog.tags = blog_update.tags
    if blog_update.image_url is not None:
        blog.image_url = blog_update.image_url
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.BlogPost).filter(models.BlogPost.id == blog_id).first()
    if not blog:
        return None
    db.delete(blog)
    db.commit()
    return True
