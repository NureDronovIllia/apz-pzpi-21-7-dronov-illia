"""add user table

Revision ID: 9cf85dd6ca55
Revises: 
Create Date: 2024-05-05 14:04:45.384492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cf85dd6ca55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('birth_data', sa.String(length=10), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('role', sa.Enum('EMPLOYEE', 'ADMIN', name='userrole', create_constraint=True), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('passport_number', sa.String(length=32), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
