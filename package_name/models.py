from sqlalchemy import Column, Integer, String

from package_name.db import Base

class Card(Base):
    __tablename__ = 'card'
    card_id = Column(Integer, primary_key=True)
    word = Column(String)
    definition = Column(String)

    def __init__(self, word=None, definition=None):
        self.word = word
        self.definition = definition

    def __repr__(self):
        return "<Card(word='%s')>" % (self.word)
