"""empty message

Revision ID: 1c12df6bf9fe
Revises: 4048d9dc6581
Create Date: 2023-10-18 15:15:33.954516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c12df6bf9fe'
down_revision = '4048d9dc6581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['public_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###