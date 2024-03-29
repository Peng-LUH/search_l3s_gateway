"""empty message

Revision ID: f7320e7b59eb
Revises: 5611f1824ce4
Create Date: 2023-11-12 21:48:14.278296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7320e7b59eb'
down_revision = '5611f1824ce4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Document', schema=None) as batch_op:
        batch_op.drop_column('owner')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Document', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner', sa.VARCHAR(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
