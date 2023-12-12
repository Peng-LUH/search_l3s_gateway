"""empty message

Revision ID: 59361b2c257e
Revises: 73d024849942
Create Date: 2023-10-18 15:37:59.480854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59361b2c257e'
down_revision = '73d024849942'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=256), server_default='58ef1ab8-7255-4204-a6cc-6564c6d4b484', nullable=True))
        batch_op.create_unique_constraint(None, ['public_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('public_id')

    # ### end Alembic commands ###