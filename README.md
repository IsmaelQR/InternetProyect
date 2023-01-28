# API REST CON FLASK Y MYSQL

Crear entorno virtual

```bash
    virtualenv env
```
Instalar dependencias

```bash
    pip install -r requirements.txt
```

Credenciales .env

```bash
    SECRET_KEY="mysecret"
    FLASK_APP=main.py
    FLASK_DEBUG=1
    FLASK_ENV=FLASK_DEVELOPMENT
    SQLALCHEMY_DATABASE_URI= mysql://root@localhost/aula1_crud_flask
```


Metodo POST

```bash
    http://127.0.0.1:5000/salones

    {
    "aula":"Las orugas",
    "hora_entrada": "8:00"
    }
```

Metodo GET

```bash
    http://127.0.0.1:5000/ver-salones

```

Metodo DELETE

```bash
    http://127.0.0.1:5000/ver-salones

```

Metodo UPDATE

```bash
    http://127.0.0.1:5000/ver-salones

```


