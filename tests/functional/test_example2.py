import pytest
from main import app
from application.database import db
from application.models import User, Article, ArticleAuthors
from bs4 import BeautifulSoup


def test_no_articles_home(client, init_database):
    print("RUNNING")
    ## Act
    response = client.get('/')

    ## Assert
    assert b"<title>All Articles</title>" in response.data


def test_check_one_article_home(client, init_database):
    ## Insert User
    u = User(username='testUser', email='test@example.com', password="password", active=1)
    db.session.add(u)
    db.session.commit()

    ## Insert Article
    a = Article(title="My Aricle", content="My Content")
    db.session.add(a)
    db.session.commit()

    ## Author
    aa = ArticleAuthors(user_id=u.id, article_id=a.article_id)
    db.session.add(aa)
    db.session.commit()

    response = client.get('/')
    assert b"<title>All Articles</title>" in response.data
    assert b"like-icon" in response.data 

    soup = BeautifulSoup(response.data, "html.parser")
    # ratings = soup.find_all("i", {"class": "like-icon"})
    # assert len(ratings) == 1

    h2_heading = soup.find_all("h2")
    assert len(h2_heading) == 1
    assert h2_heading[0].string == "My Aricle"
