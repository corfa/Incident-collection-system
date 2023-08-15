from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy import text

from db.models import Problem
from shemas.search import SearchQuery



def insert_problem(db: Session, data: dict ) -> int:
    try:
        problem = Problem(headers = data['headers'], body = data['body'])
        db.add(problem)
        db.commit()
        db.refresh(problem)
        return problem.id
    except:
        raise Exception



def find_problems(db: Session, query: SearchQuery) -> list:
    key = query.key
    value = query.value
    
    query_string = text(
        """
        SELECT id, headers, body FROM problems 
        WHERE problems.headers ->> :key ILIKE :value 
        OR problems.body ->> :key ILIKE :value
        """
    )
    
    records = db.execute(query_string, {"key": key, "value": f"%{value}%"}).fetchall()

    return     [dict(record._asdict()) for record in records]



def get_problem_by_id(db: Session, id: int):
    problem = db.query(Problem).filter_by(id=id).with_entities(Problem.headers, Problem.body).first()
    if problem:
        headers, body = problem 
        problem_dict = {"headers": headers, "body": body}
        return problem_dict
    else:
        return None
