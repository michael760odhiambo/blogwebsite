"""save this other changes

Revision ID: 009730fa2085
Revises: 
Create Date: 2019-09-23 18:53:17.462411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '009730fa2085'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=100), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('posts', sa.Column('blog', sa.String(length=255), nullable=True))
    op.add_column('posts', sa.Column('title', sa.String(length=255), nullable=True))
    op.drop_column('posts', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('posts', 'title')
    op.drop_column('posts', 'blog')
    op.drop_table('profile_photos')
    op.drop_table('comment')
    # ### end Alembic commands ###
