from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255))
    posts = relationship('Post', back_populates='author', uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = hash(kwargs.get('password'))

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def __str__(self):
        return self.username
    
    def check_password(self, password_guess):
        return str(hash(password_guess)) == self.password

    


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(String, nullable=False)
    date_created = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"

    def __str__(self):
        return f"""
        {self.id} - {self.title}
        By: {self.author}
        {self.body}
        """
    

from sqlalchemy import create_engine

engine = create_engine('sqlite:///example1.db', echo=True)

Session = sessionmaker(engine)

if __name__ == '__main__':
    with Session() as session:
        Base.metadata.create_all(engine)
