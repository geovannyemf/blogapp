import os

# Ruta base en tu computadora
base_path = r"C:\Workspace\React\blog\blogapp"  # Cambia esta ruta según tu proyecto

# Nueva estructura que deseas tener
new_structure = {
    "client": {
        "public": [
            "favicon.ico", "index.html", "logo192.png", "logo512.png", "manifest.json", "robots.txt"
        ],
        "src": {
            "components": {
                "post": ["PostCard.js", "PostDetail.js"]
            },
            "features": {
                "redux": ["store.js"]
            },
            "hooks": ["useFetchData.js"],
            "pages": [
                "HomePage.js", "PostDetailPage.js", "PostListPage.js"
            ],
            "styles": ["global.css", "theme.js"],
            "utils": ["helpers.js"],
            "App.js": "index.js"
        },
        "package.json": [],
        "yarn.lock": [],
        "README.md": []
    },
    "data": {
        "posts": ["mi-primer-post.md"]
    },
    "server": {
        "config": ["database.js"],
        "controllers": ["postController.js"],
        "middleware": ["auth.js"],
        "models": ["Post.js"],
        "routes": ["posts.js"],
        "server.js": [],
        "package.json": [],
        "yarn.lock": [],
        "README.md": []
    },
    ".gitignore": [],
    "README.md": []
}

# Función para crear la estructura
def create_structure(base, struct):
    for name, content in struct.items():
        current_path = os.path.join(base, name) if name else base
        if isinstance(content, list):
            # Crear archivos
            for file in content:
                file_path = os.path.join(current_path, file)
                if not os.path.exists(file_path):  # Solo crear si no existe
                    open(file_path, 'w').close()
        elif isinstance(content, dict):
            # Crear carpetas
            if not os.path.exists(current_path):
                os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, content)

# Función para eliminar archivos y carpetas no necesarias
def remove_unwanted_structure(base, struct):
    for name, content in struct.items():
        current_path = os.path.join(base, name) if name else base
        if isinstance(content, list):
            for file in content:
                file_path = os.path.join(current_path, file)
                # Eliminar el archivo si ya existe en la estructura no deseada
                if os.path.exists(file_path):
                    os.remove(file_path)
        elif isinstance(content, dict):
            # Eliminar carpetas si están vacías
            if os.path.exists(current_path):
                remove_unwanted_structure(current_path, content)
                # Si la carpeta está vacía, eliminarla
                if not os.listdir(current_path):
                    os.rmdir(current_path)

# Crear la estructura
create_structure(base_path, new_structure)

# Eliminar archivos y carpetas que sobran en la estructura actual
remove_unwanted_structure(base_path, {
    'client': {
        'public': [],
        'src': {
            'components': {},
            'features': {},
            'hooks': {},
            'pages': {},
            'styles': {},
            'utils': {},
        },
        '': ['package.json', 'README.md', 'yarn.lock'],
    },
    'server': {
        '': ['package.json', 'README.md', 'yarn.lock'],
        'config': {},
        'controllers': {},
        'middleware': {},
        'models': {},
        'routes': {},
    },
    'public': [],
    'src': [],
    'data': []
})
