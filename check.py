import os

# Carpetas que quieres ignorar (puedes agregar más si gustas)
EXCLUDE_DIRS = {'node_modules', '.git', 'build', 'dist', '.next', '.turbo', 'coverage'}

# Ruta base del proyecto
base_path = r"C:\Workspace\React\blog\blogapp"

def scan_directory(path):
    structure = {}

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            if entry in EXCLUDE_DIRS:
                continue  # ignorar carpetas
            sub_structure = scan_directory(full_path)
            if sub_structure:
                structure[entry] = sub_structure
        else:
            # Obtiene la carpeta contenedora relativa al path actual
            rel_path = os.path.relpath(path, base_path)
            structure.setdefault("", []).append(entry)

    return structure

# Ejecutar
result = scan_directory(base_path)

# Mostrar resultado de forma clara
import pprint
pprint.pprint(result, width=120)
