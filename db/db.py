from sqlmodel import create_engine, SQLModel, Session, select
from models.models import Item, Product

conf = {
    'host': "postgresql.natanmb.svc.cluster.local",
    'port':'5432',
    'database': "postgres",
    'user': "mydatabase1",
    'password': "1a2b3c4d"
}


engine = create_engine("postgresql://{user}:{password}@{host}:{port}/{database}".format(**conf))


def create_tables():
    SQLModel.metadata.create_all(engine)
    
def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
    
def get_product(barcode: str):
    with Session(engine) as session:
        statement = select(Product).where(Product.barcode == barcode)
        result = session.exec(statement)
        return result.first()

def get_all_products():
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement)
        return results.all()

def add_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item    
    
def get_all_items():
    with Session(engine) as session:
        statement = select(Item)
        results = session.exec(statement)
        return results.all()
    
def get_num_items():
    with Session(engine) as session:
        statement = select(Item)
        results = session.exec(statement)
        return len(results.all())
    
def get_num_products():
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement)
        return len(results.all())

def drop_tables():
    SQLModel.metadata.drop_all(engine)
