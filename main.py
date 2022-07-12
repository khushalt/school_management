from fastapi import FastAPI
from config import Configuration


def create_app():
    school_app = FastAPI(title="School/Institute Management Tool",
                         description=(
                             "School Management app for every educational Institution"
                             " Project page: https://github.com/khushalt/school_management.git."
                         ),
                         version="1.0.0")
    return school_app


app = create_app()
