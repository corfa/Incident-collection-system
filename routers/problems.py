
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from routers.depends import get_db
from starlette.requests import Request
from db.requests.problem_requests import insert_problem
from db.requests.hash_record_requests import insert_hash_record 
from helper.hash import create_hash

router = APIRouter()



@router.post("/problems/", tags=["problems"])
async def create_problem(request: Request, db: Session = Depends(get_db)):
   try:
      headers = dict(request.headers)
      body = await request.json()

      data = {"headers": headers, "body": body}
      hash = create_hash(data) 
      
      id_problem = insert_problem(db, data)
      insert_hash_record(db, hash, id_problem)
      
      return {"hash" : hash}
   except:
         raise HTTPException(status_code=400,detail="Something went wrong")