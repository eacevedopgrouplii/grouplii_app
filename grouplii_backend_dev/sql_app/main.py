from typing import List

from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from . import models, schemas, send_email, create_pdf
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create_inventory', response_model=schemas.InventoryTable)
def create_inventory(input:schemas.InventoryTable, db:Session=Depends(get_db)):
    inventory = models.InventoryTable(
                                     inventory_process = input.inventory_process,
                                     clients_name = input.clients_name,
                                     inventory_reference = input.inventory_reference,
                                     inventory_origin = input.inventory_origin,
                                     inventory_phone = input.inventory_phone,
                                     inventory_email = input.inventory_email,
                                     inventory_destination = input.inventory_destination,
                                     inventory_via = input.inventory_via,
                                     status_inventory = input.status_inventory)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory


@app.post('/create_inventory_detail', response_model=schemas.InventoryDetailTable)
def create_inventor_detail(input:schemas.InventoryDetailTable, db:Session=Depends(get_db)):
    inventory = models.InventoryDetailTable(                                     
                                     inventory_id = input.inventory_id,
                                     barcode_id = input.barcode_id,
                                     item_number = input.item_number,
                                     packing_reference = input.packing_reference,
                                     articles = input.articles,
                                     condition_at_origin = input.condition_at_origin,
                                     exceptions_at_destination = input.exceptions_at_destination,
                                     load_check = input.load_check, 
                                     description_unload = input.load_check,
                                     unload_check = input.load_check,
                                     description_load = input.load_check
                                     )
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory
    
@app.post('/load_unload', response_model=schemas.LoadUnloadTable)
def create_inventor_detail(input:schemas.LoadUnloadTable, db:Session=Depends(get_db)):
    inventory = models.LoadUnloadTable(                                     
                                     inventory_load_unload_id =input.inventory_load_unload_id,
                                     container_type =input.container_type,
                                     container_number =input.container_number,
                                     tare =input.tare,
                                     hour_start =input.hour_start,
                                     hour_end =input.hour_end,
                                     space =input.space,
                                     number_photos =input.number_photos,
                                     client_name =input.client_name,
                                     inventory_reference =input.inventory_reference,
                                     inventory_date =input.inventory_date,
                                     total_pieces =input.total_pieces,
                                     total_vans =input.total_vans,
                                     volume_m3 =input.volume_m3,
                                     received_by =input.received_by,
                                     delivered_by =input.delivered_by,
                                     personnel =input.personnel,
                                     packing =input.packing,
                                     personnel1 =input.personnel1,
                                     load_unload =input.load_unload,
                                     seals =input.seals,
                                     license_plate =input.license_plate,
                                     consolidated =input.consolidated,
                                     observations =input.observations)
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory


@app.get("/get_inventory/{barcode}", response_model= List[schemas.InventoryTable])
def get_inventory(barcode: int, db: Session = Depends(get_db)):
    db_inventory_detail = db.query(models.InventoryDetailTable).filter(models.InventoryDetailTable.barcode_id == barcode).first()        
    db_inventory = db.query(models.InventoryTable).filter(models.InventoryTable.inventory_reference == db_inventory_detail.inventory_id).offset(0).limit(100).all()

    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@app.get("/get_inventory_detail/{barcode}", response_model= List[schemas.InventoryDetailTable])
def get_inventory_detail(barcode: str, db: Session = Depends(get_db)):
    db_inventory_detail = db.query(models.InventoryDetailTable).filter(models.InventoryDetailTable.inventory_id == barcode).all()  

    if db_inventory_detail is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory_detail


@app.put("/update_items/{barcode_id}")
def update_items(barcode_id: str, input: schemas.InventoryDetailTable, db: Session = Depends(get_db)):
    db_inventory_detail = db.query(models.InventoryDetailTable).filter(models.InventoryDetailTable.barcode_id == barcode_id).first()

    if db_inventory_detail:
        db_inventory_detail.load_check = input.load_check
        db_inventory_detail.description_load = input.description_load
        db_inventory_detail.unload_check = input.unload_check
        db_inventory_detail.description_unload = input.description_unload
        db.commit()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not db_inventory_detail:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    
    db.refresh(db_inventory_detail)
    return db_inventory_detail


@app.put("/update_inventory/{inventory_reference}")
def update_items(inventory_reference: str, status: str,  db: Session = Depends(get_db)):
    db_inventory = db.query(models.InventoryTable).filter(models.InventoryTable.inventory_reference == inventory_reference).first()

    if db_inventory:
        db_inventory.status_inventory = status
        db.commit()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not db_inventory:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    
    db.refresh(db_inventory)
    return db_inventory


app.mount("/static", StaticFiles(directory="static"), name="static")
@app.post("/email")
async def send_with_template(email: schemas.EmailSchema) -> JSONResponse:
    
    file_to_attachment = create_pdf.fill_pdf(email.dict().get("body"))    

    message = MessageSchema(
        subject=email.dict().get("subject"),
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        template_body=email.dict().get("body"),
        attachments=[file_to_attachment]
        )

    fm = FastMail(send_email.conf)
    await fm.send_message(message, template_name="email.html") 
    return JSONResponse(status_code=200, content={"message": "email has been sent"})