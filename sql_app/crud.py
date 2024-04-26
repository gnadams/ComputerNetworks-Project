from sqlalchemy.orm import Session
from . import models, schemas

def get_bw(db: Session, s_id: int):
    return db.query(models.Bandwidth).filter(models.Bandwidth.id == s_id)

def get_all_bw(db: Session):
    return db.query(models.Bandwidth).offset(0).limit(20).all()

def get_num_rows(db: Session):
    return db.query(models.Bandwidth).count()

def create_bw(db: Session, item: schemas.ItemBase):
    db_item = models.Bandwidth(id = None,
                               upload = 55,
                                download=44,
                               time = item.time,
                               )
    db.add(db_item)
    db.commit()
    return db_item
def mod_bw(db: Session, s_id: int):
    bw = db.query(models.Bandwidth).filter(models.Bandwidth.id == s_id)