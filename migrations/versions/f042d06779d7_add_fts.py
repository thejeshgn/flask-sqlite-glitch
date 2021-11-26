"""Add FTS

Revision ID: f042d06779d7
Revises: 87fbccb0e18f
Create Date: 2021-11-11 01:32:07.319584

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = 'f042d06779d7'
down_revision = '87fbccb0e18f'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    sql = text("""CREATE VIRTUAL TABLE article_search 
            USING fts5(title, content, content=article, 
            content_rowid=article_id, tokenize="porter unicode61");""")
    conn.execute(sql)

def downgrade():
    op.drop_table("article_search")

