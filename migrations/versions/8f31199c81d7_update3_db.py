"""update3 db

Revision ID: 8f31199c81d7
Revises: 3b2f2014733a
Create Date: 2017-11-05 11:02:19.370133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f31199c81d7'
down_revision = '3b2f2014733a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_content', sa.String(length=255), nullable=True))
    op.drop_column('comments', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment_content')
    # ### end Alembic commands ###