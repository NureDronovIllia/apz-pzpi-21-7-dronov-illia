"""alter inspections table

Revision ID: a8d586483066
Revises: c67b0ac39e22
Create Date: 2024-05-26 11:46:42.903671

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a8d586483066'
down_revision = 'c67b0ac39e22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inspections', sa.Column('reason', sa.String(), nullable=False))
    op.add_column('inspections', sa.Column('start_time', sa.DateTime(), nullable=False))
    op.add_column('inspections', sa.Column('end_time', sa.DateTime(), nullable=True))
    op.alter_column('inspections', 'conclusion',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('inspections', 'created_at')
    op.alter_column('shifts', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shifts', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.add_column('inspections', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.alter_column('inspections', 'conclusion',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('inspections', 'end_time')
    op.drop_column('inspections', 'start_time')
    op.drop_column('inspections', 'reason')
    # ### end Alembic commands ###