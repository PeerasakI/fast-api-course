from fastapi import FastAPI

app = FastAPI(title= "Rent a Room API",
              description="Book a stay in a room",
              version= "1.0.0",
              contact={"name":"Peerasak In",
                       "email":"xxxx@gmail.com"})

@app.get("/")
def home():
    return {'message': "Welcome to my homepage!"}