## Notes: Modern APIs with FastAPI

TalkPython Training Course: [Modern APIs with FastAPI and Python](https://training.talkpython.fm/courses/details/modern-apis-with-fastapi-and-python)

### Chapter 3 - Building your first API with FastAPI

- To create a web project that uses FastAPI (depends on external libraries), 
  - Create a virtual environment
    - `python3 -m venv <name of virtual environment>`
  - Activate the virtual environment
    - `source venv/bin/activate` (for Mac and Linux)
    - To deactivate: `deactivate`
  - Update pip
    - `python3 -m pip install --upgrade pip`
    - To see packages installed: `pip list`

- Create `main.py`
  - Run `main` to make sure everything is working
  - To use fastapi
    - 'import fastapi'
    - Create `requirements.txt` file
      - `fastapi`
    - Run `pip install -r requirements.txt` with the virtual environment activated to get all of its dependencies.

- Minimal API endpoint:
  - import `fastapi` to use FastAPI
  - import `uvicorn` to have a server to run the app
  - create an instance of the `FastAPI` object
  - create a function and decorate with HTTP verbs `@app.get` to create a route
    - we have a 'calculate' function that handles requests to `api/calculate`
    - response is automatically returned as JSON
      -`return {'value': value}`
  - use an external server to run the app
    - `uvicorn.run(fastapi_instance, host="127.0.0.1", port=8000)`

- To pass parameters to the endpoint:
  - Pass parameters to the function
    - Use type hints to specify the type of the parameter (default is string)
      - `def calculate(x: int, y: int, z: int):`
    - Add default values if needed
      - `def calculate(x: int, y: int, z: int = 10):`
      - x and y are called concrete types
    - Add optional integers
      - `def calculate(x: int, y: int, z: Optional[int] = None):`
  - Add parameters in the URI
    - `api/calculate?x=1&y=2&z=3`

- For the case when z is 0, we can return a response with a status code:
  - ```return fastapi.Response(
      content='{"error": "ERROR: z cannot be zero"}',
      media_type='application/json',
      status_code=400)
  - ```return fastapi.response.JSONResponse(
      content={"error": "ERROR: z cannot be zero"},
      status_code=400)
- By default, FastAPI returns errors that are not controlled by you as JSON.
