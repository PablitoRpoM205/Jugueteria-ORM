from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04c005510a3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add authentication fields to usuarios table
    op.add_column('usuarios', sa.Column('correo', sa.String(length=255), nullable=False))
    op.add_column('usuarios', sa.Column('hashed_password', sa.String(length=255), nullable=False))
    op.add_column('usuarios', sa.Column('rol', sa.String(length=50), nullable=False))


def downgrade():
    # Remove authentication fields from usuarios table
    op.drop_column('usuarios', 'correo')
    op.drop_column('usuarios', 'hashed_password')
    op.drop_column('usuarios', 'rol')