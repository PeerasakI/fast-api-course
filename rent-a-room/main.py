from fastapi import FastAPI, status, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI(title= "Rent a Room API",
              description="Book a stay in a room",
              version= "1.0.0",
              contact={"name":"Peerasak In",
                       "email":"xxxx@gmail.com"})
rooms = [{"id": 1, "type": 'Delux', "price":2500},
        {"id": 2, "type": 'Graden-view', "price":3000},
        {"id": 3, "type": 'Sea-view', "price":3500},
        {"id": 4, "type": 'Family', "price":5000}
        ]

app.mount("/assess", StaticFiles(directory="assess"), name="assess")
@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {'message': "Welcome to my homepage!"}

@app.get("/room/{id}", status_code=status.HTTP_200_OK)
def get_room(id:int):
    for r in rooms:        
        if r["id"] == id:
            return r
            
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                        detail= "No room")    
    
    