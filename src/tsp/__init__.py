# src/tsp/__init__.py

"""
Pacote tsp.
Exposes core TSP domain entities: City, Route, and InstanceLoader.
"""

from .city import City
from .route import Route
from .instance_loader import InstanceLoader

__all__ = [
    'City',
    'Route',
    'InstanceLoader'
]