from .database import db
from flask_security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))    

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    authors = db.relationship("User", secondary="article_authors")

class ArticleAuthors(db.Model):
    __tablename__ = 'article_authors'
    user_id = db.Column(db.Integer,   db.ForeignKey("user.id"), primary_key=True, nullable=False)
    article_id = db.Column(db.Integer,  db.ForeignKey("article.article_id"), primary_key=True, nullable=False) 


class ArticleSearch(db.Model):
    __tablename__ = 'article_search'
    __table_args__ = {'info': dict(is_virtual=True)}
    rowid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    slug = db.Column(db.String, unique=True)

class ArticleCategories(db.Model):
    __tablename__ = 'article_categories'    
    article_id = db.Column(db.Integer, db.ForeignKey("article.article_id"), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"), primary_key=True)