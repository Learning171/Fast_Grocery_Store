import uvicorn
from fastapi import FastAPI
from app.config.database import engine
from app.config.database import Base
from app.auth import authrouter
from app.users import usersrouter
from app.review import reviewrouter
from app.product import productrouter
from app.order import orderrouter
from app.models import ordermodels, productmodels, reviewmodels, usermodels
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/static", StaticFiles(directory="static"), name="static")

usermodels.Base.metadata.create_all(bind=engine)
reviewmodels.Base.metadata.create_all(bind=engine)
productmodels.Base.metadata.create_all(bind=engine)
ordermodels.Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return "Hello"


app.include_router(authrouter.router, prefix="/api")
app.include_router(usersrouter.router, prefix="/api")
app.include_router(reviewrouter.router, prefix="/api")
app.include_router(productrouter.router, prefix="/api")
app.include_router(orderrouter.router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
