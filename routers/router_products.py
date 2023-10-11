from fastapi import APIRouter, Depends, HTTPException, status
from classes import schemas_dto
import uuid
from typing import List

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
async def get_products_list():
    return products

@router.post('', response_model=schemas_dto.Product, status_code=201)
async def create_product(givenCategory: str, givenName: str, givenPrice: float ,givenDescription: str):
    # création de l'object/dict Product avec les données reçues
    newProduct = schemas_dto.Product(id=str(uuid.uuid4()),category=givenCategory, name=givenName, price=givenPrice, description=givenDescription)
    # Ajout du nouveau Student dans la List/Array
    products.append(newProduct)
    # Réponse définit par le Student avec son ID
    return newProduct

@router.get('/{id}', response_model=schemas_dto.Product)
async def get_product_by_id(id: str):
    #On parcours chaque produit de la liste
    for product in products:
        # Si l'ID correspond, on retourne le produit trouvé
        if product.id == id:
            return product
        # pas de "else" car si on ne l'a pas trouvé, on continue avec le prochain student
    # Si on arrive ici, c'est que la boucle sur la liste "produits" n'a rien trouvé
    # On lève donc un HTTP Exception avec un message d'erreur
    raise HTTPException(
 status_code=404, detail=f"Produit {id} not found."
 )
