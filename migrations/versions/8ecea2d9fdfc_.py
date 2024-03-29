"""empty message

Revision ID: 8ecea2d9fdfc
Revises: bce4710bbb16
Create Date: 2023-10-19 10:16:52.366916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8ecea2d9fdfc'
down_revision = 'bce4710bbb16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site_user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=1024), autoincrement=False, nullable=True),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('context_tags', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('content_tags', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('owner', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('entity_type', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('entity_id', sa.VARCHAR(length=225), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='site_user_pkey'),
    sa.UniqueConstraint('content', name='site_user_content_key'),
    sa.UniqueConstraint('entity_id', name='site_user_entity_id_key'),
    sa.UniqueConstraint('title', name='site_user_title_key')
    )
    # ### end Alembic commands ###
