import fastapi
import uvicorn 
from typing import Optional # for optional parameters

# create an instance of the FastAPI class
api = fastapi.FastAPI() 

# create a welcome endpoint
@api.get('/')
def index():
    body = '<html>' \
            '<body style="padding: 10px;">' \
                '<h1>Welcome to the API</h1>' \
                '<div>' \
                    "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
                '</div>' \
            '</body>' \
           '</html>'
    return fastapi.responses.HTMLResponse(content=body)

# create an endpoint
@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.Response(
            content='{"error": "ERROR: z cannot be zero"}',
            media_type='application/json',
            status_code=400
        )
    
    value = x + y

    if z is not None:
        value /= z
    
    # return a dictionary
    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }

# provide an external server
uvicorn.run(api, host="127.0.0.1", port=8000)