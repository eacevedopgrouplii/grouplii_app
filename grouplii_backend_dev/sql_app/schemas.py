from datetime import date, datetime
from typing import List, Optional, Dict, Any

from pydantic import BaseModel,EmailStr

class EmailSchema(BaseModel):
    email: List[EmailStr]
    body: Dict[str, Any]
    subject: str

class InventoryTable(BaseModel):

    inventory_id : int
    inventory_process : str
    clients_name : str 
    inventory_reference : str  
    inventory_origin : str 
    inventory_phone : str 
    inventory_email : str 
    inventory_destination : str 
    inventory_via : str 
    status_inventory : str

    class Config:
        orm_mode = True

class InventoryDetailTable(BaseModel):

    item_id : int
    inventory_id : str 
    barcode_id : int  
    item_number : int  
    packing_reference : str  
    articles : str 
    condition_at_origin : str  
    exceptions_at_destination : str 
    load_check : bool
    description_unload: str
    unload_check : bool
    description_load: str

    class Config:
        orm_mode = True

class LoadUnloadTable(BaseModel):

    inventory_load_unload_id : int
    container_type : str
    container_number : int
    tare : str 
    hour_start : str
    hour_end : str
    space : str
    number_photos : int
    client_name : str
    inventory_reference : str 
    inventory_date : str
    total_pieces : int  
    total_vans : int  
    volume_m3 : str 
    received_by : str
    delivered_by : str
    personnel : str
    packing : str
    personnel1 : str 
    load_unload :str 
    seals : int  
    license_plate : str
    consolidated : str
    observations : str

    class Config:
        orm_mode = True


class Users(BaseModel):

    id_user: Optional[int]
    username: str
    email: Optional[str]
    password: str
    role: Optional[str]   

    class Config:
        orm_mode = True

class Login(BaseModel):
	username: str
	password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

