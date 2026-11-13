from networkx import truncated_cube_graph
import uvicorn
from fastapi import  APIRouter

from customer.config.config import Settings


if __name__== "__main__":
    uvicorn.run(app="customer.api.app.app",
                host=Settings.app_host,
                port=Settings.app_port,
                reload=True)