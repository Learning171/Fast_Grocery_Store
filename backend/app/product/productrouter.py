from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.validations.productschema import ProductSchema
from app.config.database import get_db

from app.product.productservice import ProductService

router = APIRouter(prefix="/product", tags=["Products"])


@router.get("/")
def getallProduct(db: Session = Depends(get_db)):

    return ProductService.get_all_product(db=db)


@router.get("/recommendation")
def get_recommendation(db: Session = Depends(get_db)):
    return ProductService.recommend_products(db)


@router.post("/")
def createProduct(request: ProductSchema, db: Session = Depends(get_db)):
    return ProductService.create_product(request=request, db=db)


@router.get("/{productid}")
def showProduct(productid: int, db: Session = Depends(get_db)):
    return ProductService.show_product(productid=productid, db=db)


@router.put("/{productid}")
def updateProduct(
    productid: int, request: ProductSchema, db: Session = Depends(get_db)
):
    return ProductService.update_product(productid=productid, request=request, db=db)


@router.delete("/{productid}")
def deleteProduct(productid: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(productid=productid, db=db)
