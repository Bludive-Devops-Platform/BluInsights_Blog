from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models, schemas, crud
import shutil, os

# App setup
app = FastAPI(title="BluInsights Blog Service")

# Serve images
os.makedirs("../images", exist_ok=True)
app.mount("/images", StaticFiles(directory="../images"), name="images")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/blogs", response_model=schemas.BlogResponse)
async def create_blog(
    title: str = Form(...),
    content: str = Form(...),
    tags: str = Form(None),
    author: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    image_url = None
    if image:
        images_dir = "../images"
        os.makedirs(images_dir, exist_ok=True)
        image_path = f"{images_dir}/{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_url = f"http://localhost:5001/images/{image.filename}"
    blog = schemas.BlogCreate(title=title, content=content, tags=tags, author=author, image_url=image_url)
    return crud.create_blog(db, blog)

# Read all
@app.get("/blogs", response_model=list[schemas.BlogResponse])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_blogs(db, skip=skip, limit=limit)

# Read one
@app.get("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

# Update
@app.put("/blogs/{blog_id}", response_model=schemas.BlogResponse)
async def update_blog(
    blog_id: int = Path(...),
    title: str = Form(None),
    content: str = Form(None),
    tags: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    blog = crud.get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    image_url = blog.image_url
    if image:
        images_dir = "../images"
        os.makedirs(images_dir, exist_ok=True)
        image_path = f"{images_dir}/{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_url = f"http://localhost:5001/images/{image.filename}"

    updated_blog = schemas.BlogUpdate(title=title, content=content, tags=tags, image_url=image_url)
    return crud.update_blog(db, blog_id, updated_blog)

# Delete
@app.delete("/blogs/{blog_id}", response_model=dict)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_blog(db, blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"detail": "Blog deleted successfully"}
