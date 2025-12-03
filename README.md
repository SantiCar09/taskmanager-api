# TaskManager API

API REST simple para gestión de tareas.

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python app.py
```

## Endpoints
- GET / - Estado de la API
- GET /tasks - Listar tareas
- POST /tasks - Crear tarea
```

**Paso 3: Crear .gitignore**

**`.gitignore`**:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Environment variables
.env