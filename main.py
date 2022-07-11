from fastapi import FastAPI

app = FastAPI(title="School/Institute Management Tool",
              description=(
                  "School Management app for every educational Institution"
                  " Project page: https://github.com/egbakou/coronavirus-tg-api."
              ),
              version="1.0.0")

