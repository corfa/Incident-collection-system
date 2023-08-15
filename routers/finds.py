
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers.depends import get_db
from shemas.search import SearchQuery
from db.requests.problem_requests import find_problems, get_problem_by_id
from db.requests.hash_record_requests import find_problem_id_by_hash
router = APIRouter()



@router.post('/find/', tags=['finds'])
async def find_problem(query: SearchQuery, db: Session = Depends(get_db)):
    data = find_problems(db, query)
    return {"result": data}


@router.get('/find2/')  
def find_problem_by_hash(hash: str, db: Session = Depends(get_db)):
    id_problem = find_problem_id_by_hash(db, hash)
    problem = get_problem_by_id(db, id_problem)
    return {"problem": dict(problem)}
    