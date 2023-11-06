from fastapi import APIRouter

router = APIRouter(prefix="/products", # El prefix sirve para que se escriba la palabra "products" en las operaciones 
                    tags=["products"], #Esto solo es para que se ordene mejor en la documentacion generada por fastAPI
                    responses={404: {"message": "No encontrado"}})


products_list = ["Product 1", "Product 2", "Product 3", "Product 4"]


@router.get("/")
async def root():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]