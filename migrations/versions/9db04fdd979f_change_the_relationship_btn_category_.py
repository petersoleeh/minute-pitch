"""change the relationship btn category and pitch

Revision ID: 9db04fdd979f
Revises: 7fe91a620571
Create Date: 2017-11-01 10:42:55.469356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9db04fdd979f'
down_revision = '7fe91a620571'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('username', sa.String(length=255), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.drop_constraint('users_comment_id_fkey', 'users', type_='foreignkey')
    op.drop_constraint('users_user_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'comment_id')
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_user_id_fkey', 'users', 'users', ['user_id'], ['id'])
    op.create_foreign_key('users_comment_id_fkey', 'users', 'comments', ['comment_id'], ['id'])
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'username')
    op.drop_column('comments', 'user_id')
    op.drop_table('categories')
    # ### end Alembic commands ###
