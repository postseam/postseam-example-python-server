from sqlalchemy import create_engine

def get_engine():
    # TODO read these from the config
    engine = create_engine(
        "postgresql://user:password@localhost:5432/postseam", echo=True, future=True
    )
    return engine
