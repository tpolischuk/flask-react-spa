from backend.database import (
    Column,
    DateTime,
    Model,
    String,
    Text,
    association_proxy,
    db,
    foreign_key,
    relationship,
    slugify,
)
from backend.utils.date import utcnow

class Standard(Model):
    full_code = Column(String(140), nullable=False)
    standard = Column(String(140), nullable=False)
    description = Column(Text, nullable=False)
    tag = Column(db.JSON(), nullable=False)
