# Import du framework
from fastapi import FastAPI

# Import des routers
import routers.router_products
import routers.router_category
import routers.router_auth

# Import de la description de l'API
from documentation.description import api_description

# Création de l'application
app = FastAPI(
    title='FastShop',
    description=api_description,
)

# Ajout des routers
app.include_router(routers.router_products.router)
app.include_router(routers.router_category.router)
app.include_router(routers.router_auth.router)