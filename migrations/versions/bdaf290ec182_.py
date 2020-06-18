"""empty message

Revision ID: bdaf290ec182
Revises: d2f9eacd780d
Create Date: 2020-06-16 20:51:17.714516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdaf290ec182'
down_revision = 'd2f9eacd780d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=280), nullable=True),
    sa.Column('user', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    # ### end Alembic commands ###