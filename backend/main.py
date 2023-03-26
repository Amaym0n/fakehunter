from starlette.responses import RedirectResponse

from core.config import settings
from db import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


import os
import importlib
from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor


def generate_root_routes(app: FastAPI) -> None:
    api_path = "rest_apis"
    modules = []
    module_names = []

    with ThreadPoolExecutor() as executor:
        # получаем список всех файлов в папке rest_apis и всех ее подпапках
        for root, dirs, files in os.walk(api_path):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    module_name = f"{root.replace('/', '.')}.{file[:-3]}"
                    module_names.append(module_name)
                    # импортируем модуль асинхронно
                    future_module = executor.submit(importlib.import_module, module_name)
                    modules.append(future_module)

    # ждем, пока все модули не импортируются
    for future_module in modules:
        future_module.result()

    # регистрируем роутеры для каждого модуля с префиксом, соответствующим пути к файлу
    for module_name in module_names:
        module = importlib.import_module(module_name)
        if hasattr(module, "router"):
            prefix = f"/{os.path.relpath(os.path.dirname(module.__file__), api_path).replace('/', '.')}"
            app.include_router(module.router, prefix=prefix)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    generate_root_routes(app=app)
    return app


App = start_application()


# Delete this after testing
@App.get(path='/', response_class=RedirectResponse)
def redirecting():
    return 'docs'
