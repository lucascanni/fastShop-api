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
    schemas_dto.Product(id=uuid.uuid4(), 
                        category='Informatique', 
                        name='ASUS TUF F15-TUF507ZU4-LP144W PC', 
                        price=1099.99, 
                        description='ASUS TUF F15-TUF507ZU4-LP144W PC Portable Gaming 15,6" FHD (Ryzen 7 4800H, RAM 16G, 512G SSD PCIE, GTX 1650Ti 4G, Windows 10) Clavier AZERTY Français'
                        ),
    schemas_dto.Product(id=uuid.uuid4(), 
                        category='Bricolage', 
                        name='UHU Rollafix', 
                        price=3.39, 
                        description="Ruban adhésif d'emballage transparent, 66m x 50 mm"
                        ),
    schemas_dto.Product(id=uuid.uuid4(), 
                        category='Informatique', 
                        name='Microsoft 365 Personnel', 
                        price=43.99, 
                        description='Office 365 apps | 1 personne | 1 an ​| PC/MAC, tablette et smartphone | Téléchargement'
                        ),
    schemas_dto.Product(id=uuid.uuid4(), 
                        category='Maison',
                        name='VASAGLE Bibliothèque', 
                        price=49.99, 
                        description='Étagère à 8 Niveaux, Meuble de Rangement, en Forme d’Arbre, pour Salon, Bureau, Chambre, Marron Rustique LBC11BX'
                        ),
    schemas_dto.Product(id=uuid.uuid4(), 
                        category='Bricolage',
                        name='EZVIZ HP7 2K Visiophone Connecté Interphone Vidéo', 
                        price=299.99, 
                        description='7 Pouces Moniteur Tactile, Unlock à Distance, 2 Fils, Detection Humaine, Option RFID, Audio Bidirectionnel, Vision Nocturne, étanche, WiFi bi-Bande'
                        ),
]

@router.get('', response_model=List[schemas_dto.Product])
async def get_productsList():
    return products