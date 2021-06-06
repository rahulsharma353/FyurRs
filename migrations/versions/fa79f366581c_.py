"""empty message

Revision ID: fa79f366581c
Revises: 
Create Date: 2021-06-01 21:58:23.464020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa79f366581c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('venue')
    op.drop_table('artist')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('city', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('state', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('phone', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('genres', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('image_link', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('website', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_description', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('venue',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('city', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('state', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('address', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('phone', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('genres', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('image_link', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('website', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_description', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.drop_table('venues')
    op.drop_table('artists')
    # ### end Alembic commands ###
