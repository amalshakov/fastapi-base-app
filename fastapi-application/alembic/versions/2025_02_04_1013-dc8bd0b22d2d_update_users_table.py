"""update users table

Revision ID: dc8bd0b22d2d
Revises: a3f4a5d7dfef
Create Date: 2025-02-04 10:13:10.168337

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "dc8bd0b22d2d"
down_revision: Union[str, None] = "a3f4a5d7dfef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_foo_bar"), "users", ["foo", "bar"]
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
