"""empty message

Revision ID: 71d160116614
Revises: ffec47b4e288
Create Date: 2021-06-05 16:24:00.249481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71d160116614'
down_revision = 'ffec47b4e288'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('venues', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
