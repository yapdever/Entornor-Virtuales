import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3]


@app.get("/contacto", response_class=HTMLResponse)
def get_list():
    return """
        <h1> HOLA SOY UNA PAGINA DE CONTACTO </h1>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()