<<<<<<< HEAD
import flask_sqlalchemy.pagination
from database.createSQL import Book, Song, Author, PublishURL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
import flask_sqlalchemy

# エンジンを作成
engine = create_engine('sqlite:///onpuscores.db')

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()


page = 1
query = input()
print(query)
pagea = int(input())
books = session.query(Book).filter(Book.book_name.contains(query)).order_by(Book.book_name).paginate(page=pagea, per_page=3, error_out=False)
print(books.iter_pages())
=======
import flask_sqlalchemy.pagination
from database.createSQL import Book, Song, Author, PublishURL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
import flask_sqlalchemy

# エンジンを作成
engine = create_engine('sqlite:///onpuscores.db')

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()


page = 1
query = input()
print(query)
pagea = int(input())
books = session.query(Book).filter(Book.book_name.contains(query)).order_by(Book.book_name).paginate(page=pagea, per_page=3, error_out=False)
print(books.iter_pages())
>>>>>>> 5906a4ab66ba0d42e7d0ac461409b3aac70dc8c9
