from fastapi import APIRouter, Depends, HTTPException, status
from classes import schemas_dto
import uuid
from typing import List
from database.firebase import db
from routers.router_auth import get_current_user

router = APIRouter(
    prefix='/products',
    tags=['products']
)

#Ressource: /products
products = [
    schemas_dto.Product(id=str(uuid.uuid4()), 
                        category='Informatique', 
                        name='ASUS TUF F15-TUF507ZU4-LP144W PC', 
                        price=1099.99, 
                        description='ASUS TUF F15-TUF507ZU4-LP144W PC Portable Gaming 15,6" FHD (Ryzen 7 4800H, RAM 16G, 512G SSD PCIE, GTX 1650Ti 4G, Windows 10) Clavier AZERTY Français'
                        ),
    schemas_dto.Product(id=str(uuid.uuid4()), 
                        category='Bricolage', 
                        name='UHU Rollafix', 
                        price=3.39, 
                        description="Ruban adhésif d'emballage transparent, 66m x 50 mm"
                        ),
    schemas_dto.Product(id=str(uuid.uuid4()), 
                        category='Informatique', 
                        name='Microsoft 365 Personnel', 
                        price=43.99, 
                        description='Office 365 apps | 1 personne | 1 an ​| PC/MAC, tablette et smartphone | Téléchargement'
                        ),
    schemas_dto.Product(id=str(uuid.uuid4()), 
                        category='Maison',
                        name='VASAGLE Bibliothèque', 
                        price=49.99, 
                        description='Étagère à 8 Niveaux, Meuble de Rangement, en Forme d’Arbre, pour Salon, Bureau, Chambre, Marron Rustique LBC11BX'
                        ),
    schemas_dto.Product(id=str(uuid.uuid4()), 
                        category='Bricolage',
                        name='EZVIZ HP7 2K Visiophone Connecté Interphone Vidéo', 
                        price=299.99, 
                        description='7 Pouces Moniteur Tactile, Unlock à Distance, 2 Fils, Detection Humaine, Option RFID, Audio Bidirectionnel, Vision Nocturne, étanche, WiFi bi-Bande'
                        ),
]

@router.get('', response_model=List[schemas_dto.Product])
async def get_products_list(userData: int = Depends(get_current_user)):
    # Avec la base de données Firebase
    firebase_products = db.child("users").child(userData['uid']).child("products").get(userData['idToker']).val()
    resultArray = [value for value in firebase_products.values()]
    # return products
    return resultArray


@router.post('', response_model=schemas_dto.Product, status_code=201)
async def create_product(givenCategory: str, givenName: str, givenPrice: float ,givenDescription: str, userData: int = Depends(get_current_user)):
    newProduct = schemas_dto.Product(id=str(uuid.uuid4()),category=givenCategory, name=givenName, price=givenPrice, description=givenDescription)
    db.child("users").child(userData['uid']).child("products").child(str(uuid.uuid4())).set(newProduct.model_dump())
    return newProduct

@router.get('/{id}', response_model=schemas_dto.Product)
async def get_product_by_id(id: str, userData: int = Depends(get_current_user)):
    firebase_products = db.child("users").child(userData['uid']).child("products").child(id).get().val()
    if firebase_products is None:
        raise HTTPException(
        status_code=404, detail=f"Produit {id} not found."
        )
    else:
        return firebase_products

@router.put('/{id}', response_model=schemas_dto.Product)
async def update_product(id: str, givenCategory: str, givenName: str, givenPrice: float ,givenDescription: str):
    firebase_products = db.child("products").get().val()
    resultArray = [value for value in firebase_products.values()]
    for product in resultArray:
        if product['id'] == id:
            product['category'] = givenCategory
            product['name'] = givenName
            product['price'] = givenPrice
            product['description'] = givenDescription
            db.child("products").child(id).update(product)
            return db.child("products").child(id).update(product)
    raise HTTPException(
    status_code=404, detail=f"Produit {id} not found."
    )


@router.delete('/{id}', response_model=schemas_dto.Product)
async def delete_product(id: str):
    firebase_products = db.child("products").get().val()
    resultArray = [value for value in firebase_products.values()]
    for product in resultArray:
        if product['id'] == id:
            db.child("products").child(id).remove()
            return product
    raise HTTPException(
    status_code=404, detail=f"Produit {id} not found."
    )