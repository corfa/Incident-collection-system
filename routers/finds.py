from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from routers.depends import get_db
from shemas.search import SearchQuery
from db.requests.problem_requests import find_problems, get_problem_by_id
from db.requests.hash_record_requests import find_problem_id_by_hash

router = APIRouter()



@router.post('/find/', tags=['finds'])
async def find_problem(json_data: dict, db: Session = Depends(get_db)):
    try:
        if len(json_data) != 1:
            raise HTTPException(status_code=400, detail="JSON should contain exactly one key-value pair")
        
        key, value = next(iter(json_data.items()))
        data = find_problems(db, key, value)
        return {"result": data}
    except:
        raise HTTPException(status_code=400,detail="Something went wrong")

@router.get('/find2/', tags=['finds'])  
def find_problem_by_hash(hash: str, db: Session = Depends(get_db)):
    try:
        id_problem = find_problem_id_by_hash(db, hash)
        problem = get_problem_by_id(db, id_problem)
        return {"problem": dict(problem)}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Problem not found")