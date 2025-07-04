from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import List

app = FastAPI()

engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)

Base.metadata.create_all(bind=engine)

class ProductModel(BaseModel):
    id: int
    name: str
    price: int
    
@app.get("/products/", response_class=HTMLResponse)
async def read_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return templates.TemplateResponse("index.html", {"request": {"products": products}})

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")