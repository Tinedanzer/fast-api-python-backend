"""
create base tables

Revision ID: fdf8821871d7
Revises:
Create Date: 2019-09-22 01:36:44.791880
"""
from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func


revision = "fdf8821871d7"
down_revision = None
branch_labels = None
depends_on = None


tables = [
    "foo",
    "widgets",
]


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_datetime",
            sa.DateTime(),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "updated_datetime",
            sa.DateTime(),
            nullable=False,
            server_default=func.now(),
            onupdate=func.utc_timestamp(),
        ),
    )


def create_foo_table() -> None:
    op.create_table(
        "foo",
        sa.Column("foo_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("bar", sa.String(50), nullable=False, index=True),
        *timestamps(),
    )


def create_widgets_table() -> None:
    op.create_table(
        "widgets",
        sa.Column("widget_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("whizz", sa.String(50), nullable=False, index=False),
        sa.Column("bang", sa.Integer, nullable=False, index=False),
        *timestamps(),
    )


def upgrade() -> None:
    create_foo_table()
    create_widgets_table()


def downgrade() -> None:
    for table in tables:
        op.drop_table(table)
