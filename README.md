# Microservicio de Gestión de Reservas

## Descripción del Proyecto

Este proyecto es un microservicio web desarrollado con **FastAPI** y **Pydantic** que permite registrar y consultar reservas de salas utilizadas en actividades académicas. El servicio recibe y devuelve información en formato JSON, implementa validación automática de datos mediante Pydantic y utiliza almacenamiento temporal en memoria.

## Instrucciones de Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/valentinazapata310066/Actividad1.git
cd actividad1
```

### 2. Crear el Entorno Virtual

**En Windows:**
```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

## Instrucciones de Ejecución

### Iniciar el Servidor
```bash
uvicorn main:app --reload
```

### Acceder a la Aplicación

- **URL Base:** http://127.0.0.1:8000
- **Documentación Interactiva:** http://127.0.0.1:8000/docs
- **Documentación Alternativa:** http://127.0.0.1:8000/redoc

## Ejemplos de Uso de los Endpoints

### 1. GET / - Obtener Información de Bienvenida

**Solicitud:**
```bash
curl -X GET "http://127.0.0.1:8000/"
```

**Respuesta:**
```json
{
  "mensaje": "Bienvenido al Microservicio de Gestión de Reservas",
  "version": "1.0.0",
  "endpoints": {
    "GET /reservas": "Obtener todas las reservas",
    "GET /reservas/{id_reserva}": "Obtener una reserva específica",
    "POST /reservas": "Crear una nueva reserva"
  }
}
```

---

### 2. POST /reservas - Crear una Nueva Reserva

**Solicitud:**
```bash
curl -X POST "http://127.0.0.1:8000/reservas" \
  -H "Content-Type: application/json" \
  -d '{
    "id_reserva": 1,
    "id_sala": 101,
    "id_usuario": 5,
    "fecha": "2026-03-10",
    "hora_inicio": "09:00",
    "hora_fin": "11:00",
    "personas": 15,
    "estado": "confirmada"
  }'
```

**Respuesta Exitosa (201 Created):**
```json
{
  "mensaje": "Reserva creada exitosamente",
  "reserva": {
    "id_reserva": 1,
    "id_sala": 101,
    "id_usuario": 5,
    "fecha": "2026-03-10",
    "hora_inicio": "09:00",
    "hora_fin": "11:00",
    "personas": 15,
    "estado": "confirmada"
  }
}
```

**Respuesta de Error (si el ID ya existe):**
```json
{
  "error": "Ya existe una reserva con ID 1"
}
```

---

### 3. GET /reservas - Obtener Todas las Reservas

**Solicitud:**
```bash
curl -X GET "http://127.0.0.1:8000/reservas"
```

**Respuesta:**
```json
{
  "total": 2,
  "reservas": [
    {
      "id_reserva": 1,
      "id_sala": 101,
      "id_usuario": 5,
      "fecha": "2026-03-10",
      "hora_inicio": "09:00",
      "hora_fin": "11:00",
      "personas": 15,
      "estado": "confirmada"
    },
    {
      "id_reserva": 2,
      "id_sala": 102,
      "id_usuario": 6,
      "fecha": "2026-03-11",
      "hora_inicio": "14:00",
      "hora_fin": "16:00",
      "personas": 20,
      "estado": "confirmada"
    }
  ]
}
```

---

### 4. GET /reservas/{id_reserva} - Obtener una Reserva por ID

**Solicitud:**
```bash
curl -X GET "http://127.0.0.1:8000/reservas/1"
```

**Respuesta Exitosa:**
```json
{
  "id_reserva": 1,
  "id_sala": 101,
  "id_usuario": 5,
  "fecha": "2026-03-10",
  "hora_inicio": "09:00",
  "hora_fin": "11:00",
  "personas": 15,
  "estado": "confirmada"
}
```

**Respuesta de Error (si no existe):**
```json
{
  "error": "Reserva con ID 999 no encontrada"
}
```

---

## Estructura del Proyecto
```
actividad1/
├── venv/                    # Entorno virtual
├── main.py                  # Código fuente del microservicio
├── datos_reservas.json      # Archivo JSON con datos de prueba
├── requirements.txt         # Dependencias del proyecto
├── .gitignore              # Archivos ignorados por Git
├── README.md               # Este archivo
└── .git/                   # Repositorio Git
```

## Tecnologías Utilizadas

- **Python 3.10+**
- **FastAPI** - Framework moderno para crear APIs
- **Pydantic** - Validación de datos y modelos
- **Uvicorn** - Servidor ASGI
- **Git** - Control de versiones


## Validación de Datos

Pydantic valida automáticamente:

- **Tipos de datos:** Todos los campos deben ser del tipo especificado
- **Campos requeridos:** Todos los campos deben estar presentes
- **Formato JSON:** Los datos deben ser enviados en formato JSON válido

Si se envían datos inválidos, la API devuelve un error 422 con detalles de validación.

## Archivos Incluidos

- **main.py** - Código fuente del microservicio con todos los endpoints
- **datos_reservas.json** - Archivo con ejemplos de datos válidos e inválidos para pruebas
- **requirements.txt** - Todas las dependencias necesarias
- **README.md** - Este documento

## Autor

**Juan Carlos Morales Guerra**
**Valentina Zapata Alvarez**

## Versión

1.0.0

## Fecha

2026-03-07