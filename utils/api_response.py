from typing import Any

def ApiResponse(status:bool,message:str,data:Any):
    return {"status":status,"message":message,"data":data}