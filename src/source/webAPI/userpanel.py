from .request import Request

def get_full_usr(url,pageinf:dict):
  return Request('GET',url,pageinf)

def delete_user(url,id):
  return Request('POST',url,{'manager_id':id})

def rst_user(url,id):
  return Request('POST',url,{'manager_id':id})