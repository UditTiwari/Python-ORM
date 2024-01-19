from main import engine
from models.base import Model
from models.users import *

Model.metadata.create_all(engine)