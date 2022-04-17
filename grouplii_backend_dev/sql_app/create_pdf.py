#sejda
from fillpdf import fillpdfs

def create_dict_inventory(body_dict, initial_dict):    
    via_initial = {'air': 'Off', 'sea': 'Off','truck': 'Off'}
    value_via_body = body_dict["info_general_inventory"].get("via","").lower()

    if  value_via_body in via_initial.keys(): 
        via_initial[value_via_body] = "Yes"
        initial_dict.update(via_initial)      

    for index, article in enumerate(body_dict["info_detail"]):    
        for article_detail in article:
            if article_detail != "barcode":            
                initial_dict[article_detail+str(index+1)] = article[article_detail]
    return initial_dict

def create_dict_load_unload(body_dict, initial_dict):
    initial_checkbox = {'packing': 'Off','unpacking': 'Off','load': 'Off','unload': 'Off','20': 'Off','40': 'Off','HC': 'Off'}  
    value_container_body = body_dict["info_general_load_unload"].get("container_type","") 
    value_pack_body = body_dict["info_general_load_unload"].get("packing","")
    value_load_body = body_dict["info_general_load_unload"].get("load_unload","")

    list_to_evalue = [value_container_body, value_pack_body, value_load_body]
    
    for checkbox in list_to_evalue:
        if checkbox in initial_checkbox.keys():
            initial_checkbox[checkbox] = "Yes"
            initial_dict.update(initial_checkbox)

    for index, article in enumerate(body_dict["info_items"]):            
        if article["load_check"]:                           
                initial_dict["article_"+str(index+1)] = "Yes"
                print(initial_dict)

    return initial_dict
     

def fill_pdf(body_dict):    
    path_input_pdf = ""
    path_output_pdf = ""
    dict_finally = {}

    if "info_general_inventory" in body_dict.keys():
        initial_dict = {
            'clients_name': body_dict["info_general_inventory"].get("clientname",""),
            'reference': body_dict["info_general_inventory"].get("reference",""),
            'origin': body_dict["info_general_inventory"].get("origin",""),
            'phone': body_dict["info_general_inventory"].get("phone",""),
            'email': body_dict["info_general_inventory"].get("email",""),
            'destination': body_dict["info_general_inventory"].get("destination","")
        }
        path_input_pdf = r"./static/inventario_1.0.pdf"
        path_output_pdf = "./static/inventario_filled" + body_dict["info_general_inventory"].get('reference','') + ".pdf"
        dict_finally = create_dict_inventory(body_dict, initial_dict)   

    elif "info_general_load_unload" in body_dict.keys():        
        initial_dict = {
            'container_number': body_dict["info_general_load_unload"].get("container_number",""),
            'tare': body_dict["info_general_load_unload"].get("tare",""),
            'hour_start': body_dict["info_general_load_unload"].get("hour_start",""),
            'hour_end1': body_dict["info_general_load_unload"].get("hour_end",""),
            'space': body_dict["info_general_load_unload"].get("space",""),
            'number_photos': body_dict["info_general_load_unload"].get("number_photos",""),
            'client_name': body_dict["info_general_load_unload"].get("client_name",""),
            'inventory_reference': body_dict["info_general_load_unload"].get("inventory_reference",""),
            'inventory_date': body_dict["info_general_load_unload"].get("inventory_date",""),
            'total_pieces': body_dict["info_general_load_unload"].get("total_pieces",""),
            'total_vans': body_dict["info_general_load_unload"].get("total_vans",""),
            'volume_m3': body_dict["info_general_load_unload"].get("volume_m3",""),
            'received_by': body_dict["info_general_load_unload"].get("received_by",""),
            'delivered_by': body_dict["info_general_load_unload"].get("delivered_by",""),
            'personnel1': body_dict["info_general_load_unload"].get("personnel",""),
            'personnel2': body_dict["info_general_load_unload"].get("personnel1",""),
            'seals': body_dict["info_general_load_unload"].get("seals",""),
            'license_plate': body_dict["info_general_load_unload"].get("license_plate",""),
            'observations': body_dict["info_general_load_unload"].get("observations","")
        }

        path_input_pdf = r"./static/TARJETA_DE_CHEQUEO_1.0.pdf"
        path_output_pdf = "./static/TARJETA_DE_CHEQUEO" + body_dict["info_general_load_unload"].get('inventory_reference','') + ".pdf"
        dict_finally = create_dict_load_unload(body_dict, initial_dict)       
            


    fillpdfs.write_fillable_pdf(path_input_pdf, path_output_pdf, dict_finally, flatten=True)    

    return path_output_pdf

