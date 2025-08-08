import os

# Liste as pastas onde quer criar __init__.py
folders = [
    "models",
    "schemas",
    "usecases",
    "routes",
    "core",
    "db",
]

for folder in folders:
    path = os.path.join(os.getcwd(), folder)
    if os.path.isdir(path):
        init_file = os.path.join(path, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                pass  # cria arquivo vazio
            print(f"Arquivo criado: {init_file}")
        else:
            print(f"Arquivo já existe: {init_file}")
    else:
        print(f"Pasta não encontrada: {path}")
