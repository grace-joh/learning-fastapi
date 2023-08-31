import fastapi
import uvicorn 

# create an instance of the FastAPI class
api = fastapi.FastAPI() 

# create an endpoint
@api.get('/api/calculate')
def calculate():
    value = 2 + 2
    
    # return a dictionary
    return {
        'value': value
    }

# provide an external server
uvicorn.run(api, host="127.0.0.1, port=8000")