from application.database import db
from application.models import User, Article, ArticleAuthors
from bs4 import BeautifulSoup

class TestArticlesByAuthor:
    def test_without_login(self, client, init_database):
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

        response = client.get('/articles_by/testUser', follow_redirects=True)
        assert response.status_code == 200
        soup = BeautifulSoup(response.data, "html.parser")
        heading = soup.find_all("h1")
        assert heading[0].string == "Login"

    def test_with_login(self, client, init_database):
        response = client.post('/login', data=dict(email='test@example.com', password="password"), follow_redirects=False)
        response = client.get('/articles_by/testUser', follow_redirects=True)
        assert b"Logout" in response.data
        assert b"testUser" in response.data