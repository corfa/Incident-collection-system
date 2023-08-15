from sqlalchemy.orm import Session

from db.models import HashRecord


def insert_hash_record(db: Session, hash: str, problem_id: int):
    try:
        hash_record = HashRecord(hash = hash, problem_id = problem_id)
        db.add(hash_record)
        db.commit()
        db.refresh(hash_record)
        return hash_record.id
    except:
        raise Exception

def find_problem_id_by_hash(db: Session, hash: str):
    hash_record = db.query(HashRecord).filter_by(hash=hash).first()
    return hash_record.problem_id