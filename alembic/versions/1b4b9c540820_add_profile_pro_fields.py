"""add profile + pro fields

Revision ID: 1b4b9c540820
Revises: 25d814bc83ed
Create Date: 2025-08-11 07:03:58.361527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "1b4b9c540820"
down_revision: Union[str, None] = "25d814bc83ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# revision identifiers, used by Alembic
def upgrade() -> None:
    op.execute('ALTER TABLE users ADD COLUMN IF NOT EXISTS location VARCHAR(255);')

def downgrade() -> None:
    op.execute('ALTER TABLE users DROP COLUMN IF EXISTS location;')
