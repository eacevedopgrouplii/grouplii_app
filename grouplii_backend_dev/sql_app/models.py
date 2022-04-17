from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Barcode(Base):
    __tablename__ = "barcode_table"

    barcode_id = Column(Integer, primary_key=True, index=True)
    barcode = Column(Integer, index=True)
    barcode_use = Column(Boolean, default=True)

class InventoryTable(Base):
    __tablename__ = "inventory_table"

    inventory_id = Column(Integer, primary_key=True, index=True)
    inventory_process = Column(String, index=True)  
    clients_name = Column(String, index=True) 
    inventory_reference = Column(String, index=True)  
    inventory_origin = Column(String, index=True) 
    inventory_phone = Column(String, index=True) 
    inventory_email = Column(String, index=True) 
    inventory_destination = Column(String, index=True) 
    inventory_via = Column(String, index=True)
    status_inventory = Column(String, index=True)

class InventoryDetailTable(Base):
    __tablename__ = "inventory_detail_table"

    item_id = Column(Integer, primary_key=True, index=True) 
    inventory_id = Column(String, index=True) 
    barcode_id = Column(Integer, index=True) 
    item_number = Column(Integer, index=True) 
    packing_reference = Column(String, index=True) 
    articles = Column(String, index=True)
    condition_at_origin = Column(String, index=True) 
    exceptions_at_destination = Column(String, index=True)
    load_check = Column(Boolean, index=True)
    description_unload = Column(String, index=True)
    unload_check = Column(Boolean, index=True)
    description_load = Column(String, index=True)
    
        

class LoadUnloadTable(Base):

    __tablename__ = "load_unload_table"
    
    inventory_load_unload_id = Column(Integer, primary_key=True, index=True)
    container_type = Column(String, index=True)
    container_number = Column(Integer, index=True)
    tare = Column(String, index=True)
    hour_start = Column(DateTime, index=True)
    hour_end = Column(DateTime, index=True)
    space = Column(String, index=True)
    number_photos = Column(Integer, index=True)
    client_name = Column(String, index=True)
    inventory_reference =Column(String, index=True)
    inventory_date = Column(DateTime, index=True)
    total_pieces = Column(Integer, index=True)
    total_vans = Column(Integer, index=True)
    volume_m3 = Column(String, index=True)
    received_by = Column(String, index=True)
    delivered_by = Column(String, index=True)
    personnel = Column(String, index=True)
    packing = Column(String, index=True)
    personnel1 = Column(String, index=True)
    load_unload = Column(String, index=True)
    seals = Column(Integer, index=True)
    license_plate = Column(String, index=True)
    consolidated = Column(String, index=True)
    observations = Column(String, index=True) 
