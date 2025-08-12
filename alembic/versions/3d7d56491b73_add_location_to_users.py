"""add location to users

Revision ID: 3d7d56491b73
Revises: 1b4b9c540820
Create Date: 2025-08-11 12:13:22.534420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d7d56491b73'
down_revision: Union[str, None] = '1b4b9c540820'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
