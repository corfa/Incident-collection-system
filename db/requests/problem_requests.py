from sqlalchemy.orm import Session
from sqlalchemy import text

from db.models import Problem
from db.exceptions.problem_exception import ProblemNotFoundException



def insert_problem(db: Session, data: dict) -> int:
    try:
        problem = Problem(headers=data['headers'], body=data['body'])
        db.add(problem)
        db.commit()
        db.refresh(problem)
        return problem.id
    except Exception as e:
        raise e


def find_problems(db: Session, key: str, value: str) -> list:
    
    query_string = text(
        """
        SELECT id, headers, body
        FROM public.problems
        WHERE headers::jsonb @> jsonb_build_object(:key, :value) OR 
        body::jsonb @> jsonb_build_object(:key, :value);
        """
    )
    
    records = db.execute(query_string, {"key": key, "value": value}).fetchall()

    return [dict(record._asdict()) for record in records]
    


def get_problem_by_id(db: Session, id: int) -> dict:
    problem = db.query(Problem).filter_by(id=id).with_entities(Problem.headers, Problem.body).first()
    if problem:
        headers, body = problem 
        problem_dict = {"headers": headers, "body": body}
        return problem_dict
    else:
        raise ProblemNotFoundException
