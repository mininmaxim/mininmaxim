from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from datetime import datetime

app = FastAPI()

app.mount("/www", StaticFiles(directory="www"), name="www")
@app.get("/currentTime")
async def currentTime():
    results = {"timeValue": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return results

@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Loading..</title>
        </head>
        <body>
            <p></p>
            <script>
                window.location='/www/index.html'
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)