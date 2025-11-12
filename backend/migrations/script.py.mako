# filepath: /home/pablito/Documentos/Jugueteria-ORM/migrations/script.py.mako
# Este archivo es una plantilla para generar scripts de migración.

from sqlalchemy import MetaData

revision = '${rev}'
down_revision = '${down_rev}'
branch_labels = ${branch_label}
depends_on = ${depends_on}

def upgrade():
    # Código para aplicar la migración
    pass

def downgrade():
    # Código para revertir la migración
    pass