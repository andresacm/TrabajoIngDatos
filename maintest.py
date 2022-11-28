#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, template, static_file, request, redirect
from database import engine

app = Bottle()


@app.route('/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static')


@app.route('/', method='GET')
def home():
    return template('home')

### TiposPlan ###

@app.route('/TiposPlan', method='GET')
def TiposPlan():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un tipo de plan'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un tipo de plan'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposPlan
            """).format()
    TiposPlan = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposPlan': TiposPlan, 'mensaje': mensaje}
    return template('TiposPlan/index', locals)


@app.route('/TiposPlan/editar', method='GET')
def TiposPlan_editar():
    # parámetros
    TiposPlan_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información de TiposPlan
    stmt = ("""
            SELECT * FROM TiposPlan WHERE id={}
            """).format(TiposPlan_id)
    TiposPlan = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposPlan': TiposPlan, 'titulo': 'Editar Tipos de Plan'}
    return template('TiposPlan/detail', locals)


@app.route('/TiposPlan/crear', method='GET')
def TiposPlan_crear():
    # devolver datos a una vista
    locals = {
        'TiposPlan': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear TiposPlan'
    }
    # plantilla de views
    return template('TiposPlan/detail', locals)


@app.route('TiposPlan/grabar', method='POST')
def TiposPlan_grabar():
    # parámetros
    TiposPlan_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposPlan SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, TiposPlan_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposPlan?mensaje=editado')


@app.route('/TiposPlan/eliminar', method='GET')
def TiposPlan_eliminar():
    # parámetros
    TiposPlan_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposPlan WHERE id={}
            """).format(TiposPlan_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposPlan?,mensaje=eliminado')

### TiposVivienda ###

@app.route('/TiposVivienda', method='GET')
def TiposVivienda():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un tipo de vivienda'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un tipo de vivienda'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposVivienda
            """).format()
    TiposVivienda = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposVivienda': TiposVivienda, 'mensaje': mensaje}
    return template('TiposVivienda/index', locals)


@app.route('/TiposVivienda/editar', method='GET')
def TiposVivienda_editar():
    # parámetros
    TiposVivienda_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del tipo de vivienda
    stmt = ("""
            SELECT * FROM TiposVivienda WHERE id={}
            """).format(TiposVivienda_id)
    TiposVivienda = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposVivienda': TiposVivienda, 'titulo': 'Editar Tipo de Vivienda'}
    return template('TiposVivienda/detail', locals)


@app.route('/TiposVivienda/crear', method='GET')
def TiposVivienda_crear():
    # devolver datos a una vista
    locals = {
        'TiposVivienda': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Tipo de Vivienda'
    }
    # plantilla de views
    return template('TiposVivienda/detail', locals)


@app.route('TiposVivienda/grabar', method='POST')
def TiposVivienda_grabar():
    # parametros
    TiposVivienda_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposVivienda SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, TiposVivienda_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposVivienda?mensaje=editado')


@app.route('/TiposVivienda/eliminar', method='GET')
def TiposVivienda_eliminar():
    # parámetros
    TiposVivienda_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposVivienda WHERE id={}
            """).format(TiposVivienda_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposVivienda?,mensaje=eliminado')

### TiposPredio ###

@app.route('/TiposPredio', method='GET')
def TiposPredio():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un tipo de predio'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un tipo de predio'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposPredio
            """).format()
    TiposPredio = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposPredio': TiposPredio, 'mensaje': mensaje}
    return template('TiposPredio/index', locals)


@app.route('/TiposPredio/editar', method='GET')
def TiposPredio_editar():
    # parámetros
    TiposPredio_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del tipo de predio
    stmt = ("""
            SELECT * FROM TiposPredio WHERE id={}
            """).format(TiposPredio_id)
    TiposPredio = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposPredio': TiposPredio, 'titulo': 'Editar Tipo de Predio'}
    return template('TiposPredio/detail', locals)


@app.route('/TiposPredio/crear', method='GET')
def TiposPredio_crear():
    # devolver datos a una vista
    locals = {
        'TiposPredio': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Tipo de Predio'
    }
    # plantilla de views
    return template('TiposPredio/detail', locals)


@app.route('TiposPredio/grabar', method='POST')
def TiposPredio_grabar():
    # parámetros
    TiposPredio_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposPredio SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, TiposPredio_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposPredio?mensaje=editado')


@app.route('/TiposPredio/eliminar', method='GET')
def TiposPredio_eliminar():
    # parámetros
    TiposPredio_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposPredio WHERE id={}
            """).format(TiposPredio_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposPredio?,mensaje=eliminado')


### Distritos ###

@app.route('/Distritos', method='GET')
def Distritos():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Distritos'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Distritos'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Distritos': Distritos, 'mensaje': mensaje}
    return template('Distritos/index', locals)


@app.route('/Distritos/editar', method='GET')
def Distritos_editar():
    # parámetros
    Distritos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Distritos
    stmt = ("""
            SELECT * FROM Distritos WHERE id={}
            """).format(Distritos_id)
    Distritos = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Distritos': Distritos, 'titulo': 'Editar Distritos'}
    return template('Distritos/detail', locals)


@app.route('/Distritos/crear', method='GET')
def Distritos_crear():
    # devolver datos a una vista
    locals = {
        'Distritos': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Distritos'
    }
    # plantilla de views
    return template('Distritos/detail', locals)


@app.route('Distritos/grabar', method='POST')
def Distritos_grabar():
    # parámetros
    Distritos_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Distritos SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, Distritos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Distritos?mensaje=editado')


@app.route('/Distritos/eliminar', method='GET')
def Distritos_eliminar():
    # parámetros
    Distritos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Distritos WHERE id={}
            """).format(Distritos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Distritos?,mensaje=eliminado')

### Nacionalidades ###

@app.route('/Nacionalidades', method='GET')
def Nacionalidades():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Nacionalidades'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Nacionalidades'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Nacionalidades
            """).format()
    Nacionalidades = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Nacionalidades': Nacionalidades, 'mensaje': mensaje}
    return template('Nacionalidades/index', locals)


@app.route('/Nacionalidades/editar', method='GET')
def Nacionalidades_editar():
    # parámetros
    Nacionalidades_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Nacionalidades
    stmt = ("""
            SELECT * FROM Nacionalidades WHERE id={}
            """).format(Nacionalidades_id)
    Nacionalidades = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Nacionalidades': Nacionalidades, 'titulo': 'Editar Nacionalidades'}
    return template('Nacionalidades/detail', locals)


@app.route('/Nacionalidades/crear', method='GET')
def Nacionalidades_crear():
    # devolver datos a una vista
    locals = {
        'Nacionalidades': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Nacionalidades'
    }
    # plantilla de views
    return template('Nacionalidades/detail', locals)


@app.route('Nacionalidades/grabar', method='POST')
def Nacionalidades_grabar():
    # parámetros
    Nacionalidades_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Nacionalidades SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, Nacionalidades_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Nacionalidades?mensaje=editado')


@app.route('/Nacionalidades/eliminar', method='GET')
def Nacionalidades_eliminar():
    # parámetros
    Nacionalidades_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Nacionalidades WHERE id={}
            """).format(Nacionalidades_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Nacionalidades?,mensaje=eliminado')

### TiposContrato ###

@app.route('/TiposContrato', method='GET')
def TiposContrato():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un tipo de contrato'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un tipo de contrato'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposContrato
            """).format()
    TiposContrato = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposContrato': TiposContrato, 'mensaje': mensaje}
    return template('TiposContrato/index', locals)


@app.route('/TiposContrato/editar', method='GET')
def TiposContrato_editar():
    # parámetros
    TiposContrato_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del TiposContrato
    stmt = ("""
            SELECT * FROM TiposContrato WHERE id={}
            """).format(TiposContrato_id)
    TiposContrato = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposContrato': TiposContrato, 'titulo': 'Editar TiposContrato'}
    return template('TiposContrato/detail', locals)


@app.route('/TiposContrato/crear', method='GET')
def TiposContrato_crear():
    # devolver datos a una vista
    locals = {
        'TiposContrato': {
            'id': 'E',
            'nombre': '',
            'Descripcion':''
        },
        'titulo': 'Crear TiposContrato'
    }
    # plantilla de views
    return template('TiposContrato/detail', locals)


@app.route('TiposContrato/grabar', method='POST')
def TiposContrato_grabar():
    # parámetros
    TiposContrato_id = int(request.params.id)
    nombre = request.params.nombre
    Descripcion = request.params.Descripcion
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposContrato SET
                nombre='{}', Descripcion='{}'
                WHERE id={}
            """).format(nombre, TiposContrato_id, Descripcion)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposContrato?mensaje=editado')


@app.route('/TiposContrato/eliminar', method='GET')
def TiposContrato_eliminar():
    # parámetros
    TiposContrato_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposContrato WHERE id={}
            """).format(TiposContrato_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposContrato?,mensaje=eliminado')

### Categorias ###

@app.route('/Categorias', method='GET')
def Categorias():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado una categoría'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado una categoría'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Categorias
            """).format()
    Categorias = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Categorias': Categorias, 'mensaje': mensaje}
    return template('Categorias/index', locals)


@app.route('/Categorias/editar', method='GET')
def Categorias_editar():
    # parámetros
    Categorias_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Categorias
    stmt = ("""
            SELECT * FROM Categorias WHERE id={}
            """).format(Categorias_id)
    Categorias = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Categorias': Categorias, 'titulo': 'Editar Categorias'}
    return template('Categorias/detail', locals)


@app.route('/Categorias/crear', method='GET')
def Categorias_crear():
    # devolver datos a una vista
    locals = {
        'Categorias': {
            'id': 'E',
            'nombre': '',
            'Descripcion':''
        },
        'titulo': 'Crear Categorias'
    }
    # plantilla de views
    return template('Categorias/detail', locals)


@app.route('Categorias/grabar', method='POST')
def Categorias_grabar():
    # parámetros
    Categorias_id = int(request.params.id)
    nombre = request.params.nombre
    Descripcion = request.params.Descripcion
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Categorias SET
                nombre='{}', Descripcion='{}'
                WHERE id={}
            """).format(nombre, Categorias_id, Descripcion)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Categorias?mensaje=editado')


@app.route('/Categorias/eliminar', method='GET')
def Categorias_eliminar():
    # parámetros
    Categorias_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Categorias WHERE id={}
            """).format(Categorias_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Categorias?,mensaje=eliminado')

### TiposComision ###

@app.route('/TiposComision', method='GET')
def TiposComision():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un tipo de comision'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un tipo de comision'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposComision
            """).format()
    TiposComision = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposComision': TiposComision, 'mensaje': mensaje}
    return template('TiposComision/index', locals)


@app.route('/TiposComision/editar', method='GET')
def TiposComision_editar():
    # parámetros
    TiposComision_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del TiposComision
    stmt = ("""
            SELECT * FROM TiposComision WHERE id={}
            """).format(TiposComision_id)
    TiposComision = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposComision': TiposComision, 'titulo': 'Editar TiposComision'}
    return template('TiposComision/detail', locals)


@app.route('/TiposComision/crear', method='GET')
def TiposComision_crear():
    # devolver datos a una vista
    locals = {
        'TiposComision': {
            'id': 'E',
            'nombre': '',
            'Descripcion':''
        },
        'titulo': 'Crear TiposComision'
    }
    # plantilla de views
    return template('TiposComision/detail', locals)


@app.route('TiposComision/grabar', method='POST')
def TiposComision_grabar():
    # parámetros
    TiposComision_id = int(request.params.id)
    nombre = request.params.nombre
    Descripcion = request.params.Descripcion
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposComision SET
                nombre='{}', Descripcion='{}'
                WHERE id={}
            """).format(nombre, TiposComision_id, Descripcion)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposComision?mensaje=editado')


@app.route('/TiposComision/eliminar', method='GET')
def TiposComision_eliminar():
    # parámetros
    TiposComision_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposComision WHERE id={}
            """).format(TiposComision_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposComision?,mensaje=eliminado')

### Equipos ###

@app.route('/Equipos', method='GET')
def Equipos():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Equipos'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Equipos'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Equipos
            """).format()
    Equipos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Equipos': Equipos, 'mensaje': mensaje}
    return template('Equipos/index', locals)


@app.route('/Equipos/editar', method='GET')
def Equipos_editar():
    # parámetros
    Equipos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Equipos
    stmt = ("""
            SELECT * FROM Equipos WHERE id={}
            """).format(Equipos_id)
    Equipos = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Equipos': Equipos, 'titulo': 'Editar Equipos'}
    return template('Equipos/detail', locals)


@app.route('/Equipos/crear', method='GET')
def Equipos_crear():
    # devolver datos a una vista
    locals = {
        'Equipos': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Equipos'
    }
    # plantilla de views
    return template('Equipos/detail', locals)


@app.route('Equipos/grabar', method='POST')
def Equipos_grabar():
    # parámetros
    Equipos_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Equipos SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, Equipos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Equipos?mensaje=editado')


@app.route('/Equipos/eliminar', method='GET')
def Equipos_eliminar():
    # parámetros
    Equipos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Equipos WHERE id={}
            """).format(Equipos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Equipos?,mensaje=eliminado')

### Bancos ###

@app.route('/Bancos', method='GET')
def Bancos():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Bancos'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Bancos'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Bancos
            """).format()
    Bancos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Bancos': Bancos, 'mensaje': mensaje}
    return template('Bancos/index', locals)


@app.route('/Bancos/editar', method='GET')
def Bancos_editar():
    # parámetros
    Bancos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Bancos
    stmt = ("""
            SELECT * FROM Bancos WHERE id={}
            """).format(Bancos_id)
    Bancos = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Bancos': Bancos, 'titulo': 'Editar Bancos'}
    return template('Bancos/detail', locals)


@app.route('/Bancos/crear', method='GET')
def Bancos_crear():
    # devolver datos a una vista
    locals = {
        'Bancos': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Bancos'
    }
    # plantilla de views
    return template('Bancos/detail', locals)


@app.route('Bancos/grabar', method='POST')
def Bancos_grabar():
    # parámetros
    Bancos_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Bancos SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, Bancos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Bancos?mensaje=editado')


@app.route('/Bancos/eliminar', method='GET')
def Bancos_eliminar():
    # parámetros
    Bancos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Bancos WHERE id={}
            """).format(Bancos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Bancos?,mensaje=eliminado')

### Bancos ###

@app.route('/Bancos', method='GET')
def Bancos():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Bancos'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Bancos'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Bancos
            """).format()
    Bancos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Bancos': Bancos, 'mensaje': mensaje}
    return template('Bancos/index', locals)


@app.route('/Bancos/editar', method='GET')
def Bancos_editar():
    # parámetros
    Bancos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Bancos
    stmt = ("""
            SELECT * FROM Bancos WHERE id={}
            """).format(Bancos_id)
    Bancos = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Bancos': Bancos, 'titulo': 'Editar Bancos'}
    return template('Bancos/detail', locals)


@app.route('/Bancos/crear', method='GET')
def Bancos_crear():
    # devolver datos a una vista
    locals = {
        'Bancos': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Bancos'
    }
    # plantilla de views
    return template('Bancos/detail', locals)


@app.route('Bancos/grabar', method='POST')
def Bancos_grabar():
    # parámetros
    Bancos_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Bancos SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, Bancos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Bancos?mensaje=editado')


@app.route('/Bancos/eliminar', method='GET')
def Bancos_eliminar():
    # parámetros
    Bancos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Bancos WHERE id={}
            """).format(Bancos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Bancos?,mensaje=eliminado')

### TiposDocumento ###

@app.route('/TiposDocumento', method='GET')
def TiposDocumento():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un TiposDocumento'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un TiposDocumento'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposDocumento
            """).format()
    TiposDocumento = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposDocumento': TiposDocumento, 'mensaje': mensaje}
    return template('TiposDocumento/index', locals)


@app.route('/TiposDocumento/editar', method='GET')
def TiposDocumento_editar():
    # parámetros
    TiposDocumento_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del TiposDocumento
    stmt = ("""
            SELECT * FROM TiposDocumento WHERE id={}
            """).format(TiposDocumento_id)
    TiposDocumento = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposDocumento': TiposDocumento, 'titulo': 'Editar TiposDocumento'}
    return template('TiposDocumento/detail', locals)


@app.route('/TiposDocumento/crear', method='GET')
def TiposDocumento_crear():
    # devolver datos a una vista
    locals = {
        'TiposDocumento': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear TiposDocumento'
    }
    # plantilla de views
    return template('TiposDocumento/detail', locals)


@app.route('TiposDocumento/grabar', method='POST')
def TiposDocumento_grabar():
    # parámetros
    TiposDocumento_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposDocumento SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, TiposDocumento_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposDocumento?mensaje=editado')


@app.route('/TiposDocumento/eliminar', method='GET')
def TiposDocumento_eliminar():
    # parámetros
    TiposDocumento_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposDocumento WHERE id={}
            """).format(TiposDocumento_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposDocumento?,mensaje=eliminado')

### TiposColaborador ###

@app.route('/TiposColaborador', method='GET')
def TiposColaborador():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un tipo de comision'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un tipo de comision'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM TiposColaborador
            """).format()
    TiposColaborador = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'TiposColaborador': TiposColaborador, 'mensaje': mensaje}
    return template('TiposColaborador/index', locals)


@app.route('/TiposColaborador/editar', method='GET')
def TiposColaborador_editar():
    # parámetros
    TiposColaborador_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del TiposColaborador
    stmt = ("""
            SELECT * FROM TiposColaborador WHERE id={}
            """).format(TiposColaborador_id)
    TiposColaborador = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'TiposColaborador': TiposColaborador, 'titulo': 'Editar TiposColaborador'}
    return template('TiposColaborador/detail', locals)


@app.route('/TiposColaborador/crear', method='GET')
def TiposColaborador_crear():
    # devolver datos a una vista
    locals = {
        'TiposColaborador': {
            'id': 'E',
            'nombre': '',
            'Descripcion':''
        },
        'titulo': 'Crear TiposColaborador'
    }
    # plantilla de views
    return template('TiposColaborador/detail', locals)


@app.route('TiposColaborador/grabar', method='POST')
def TiposColaborador_grabar():
    # parámetros
    TiposColaborador_id = int(request.params.id)
    nombre = request.params.nombre
    Descripcion = request.params.Descripcion
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE TiposColaborador SET
                nombre='{}', Descripcion='{}'
                WHERE id={}
            """).format(nombre, TiposColaborador_id, Descripcion)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposColaborador?mensaje=editado')


@app.route('/TiposColaborador/eliminar', method='GET')
def TiposColaborador_eliminar():
    # parámetros
    TiposColaborador_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM TiposColaborador WHERE id={}
            """).format(TiposColaborador_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/TiposColaborador?,mensaje=eliminado')

### Generos ###

@app.route('/Generos', method='GET')
def Generos():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Generos'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Generos'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM Generos
            """).format()
    Generos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Generos': Generos, 'mensaje': mensaje}
    return template('Generos/index', locals)


@app.route('/Generos/editar', method='GET')
def Generos_editar():
    # parámetros
    Generos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Generos
    stmt = ("""
            SELECT * FROM Generos WHERE id={}
            """).format(Generos_id)
    Generos = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'Generos': Generos, 'titulo': 'Editar Generos'}
    return template('Generos/detail', locals)


@app.route('/Generos/crear', method='GET')
def Generos_crear():
    # devolver datos a una vista
    locals = {
        'Generos': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear Generos'
    }
    # plantilla de views
    return template('Generos/detail', locals)


@app.route('Generos/grabar', method='POST')
def Generos_grabar():
    # parámetros
    Generos_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE Generos SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, Generos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Generos?mensaje=editado')


@app.route('/Generos/eliminar', method='GET')
def Generos_eliminar():
    # parámetros
    Generos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Generos WHERE id={}
            """).format(Generos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Generos?,mensaje=eliminado')

### FormaContrato ###

@app.route('/FormaContrato', method='GET')
def FormaContrato():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un FormaContrato'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un FormaContrato'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT * FROM FormaContrato
            """).format()
    FormaContrato = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'FormaContrato': FormaContrato, 'mensaje': mensaje}
    return template('FormaContrato/index', locals)


@app.route('/FormaContrato/editar', method='GET')
def FormaContrato_editar():
    # parámetros
    FormaContrato_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del FormaContrato
    stmt = ("""
            SELECT * FROM FormaContrato WHERE id={}
            """).format(FormaContrato_id)
    FormaContrato = conn.execute(stmt).fetchone()
    # devolver datos a una vista
    locals = {'FormaContrato': FormaContrato, 'titulo': 'Editar FormaContrato'}
    return template('FormaContrato/detail', locals)


@app.route('/FormaContrato/crear', method='GET')
def FormaContrato_crear():
    # devolver datos a una vista
    locals = {
        'FormaContrato': {
            'id': 'E',
            'nombre': ''
        },
        'titulo': 'Crear FormaContrato'
    }
    # plantilla de views
    return template('FormaContrato/detail', locals)


@app.route('FormaContrato/grabar', method='POST')
def FormaContrato_grabar():
    # parámetros
    FormaContrato_id = int(request.params.id)
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            UPDATE FormaContrato SET
                nombre='{}'
                WHERE id={}
            """).format(nombre, FormaContrato_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/FormaContrato?mensaje=editado')


@app.route('/FormaContrato/eliminar', method='GET')
def FormaContrato_eliminar():
    # parámetros
    FormaContrato_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM FormaContrato WHERE id={}
            """).format(FormaContrato_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/FormaContrato?,mensaje=eliminado')

### Plan ###

@app.route('/Plan', method='GET')
def Plan():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Plan'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Plan'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT P.id, P.CantMegas, P.PrecioMensual,
            TP.nombre AS TipoPlan
            FROM Plan P
            INNER JOIN TipoPlan TP ON P.TipoPlan_id = TP.id            
            """).format()
    Plan = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Plan': Plan, 'mensaje': mensaje}
    return template('Plan/index', locals)


@app.route('/Plan/editar', method='GET')
def Plan_editar():
    # parámetros
    Plan_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del plan
    stmt = ("""
            SELECT * FROM Plan WHERE id={}
            """).format(Plan_id)
    Plan = conn.execute(stmt).fetchone()
    # obtener la información del tipo de plan
    stmt = ("""
            SELECT id,nombre FROM TipoPlan
            """).format()
    TipoPlan = [dict(r) for r in conn.execute(stmt)]
    # devolver datos en una vista
    locals = {
        'Plan': Plan,
        'titulo': 'Editar Plan',
        'TipoPlan': TipoPlan
    }
    return template('Plan/detail', locals)


@app.route('/Plan/eliminar', method='GET')
def Plan_eliminar():
    # pametros
    Plan_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
    DELETE FROM Plan WHERE id={}
  """).format(Plan_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Plan?mensaje=eliminado')


@app.route('/Plan/crear', method='GET')
def Plan_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la infromación del plan
    Plan = {}
    Plan['id'] = 'E'
    Plan['CantMegas'] = ''
    Plan['PrecioMensual'] = ''
    Plan['TipoPlan_id'] = 'E'
    # obtener el listado de los tipos de planes
    stmt = ("""
            SELECT id,nombre FROM TipoPlan
            """).format()
    TipoPlan = [dict(r) for r in conn.execute(stmt)]
    # devolver daos a una vista
    locals = {
        'Plan': Plan,
        'titulo': 'Agregar Plan',
        'TipoPlan': TipoPlan
    }
    return template('Plan/detail', locals)


@app.route('/Plan/grabar', method='POST')
def Plan_grabar():
    # parámetros
    Plan_id = request.params.id
    CantMegas = request.params.CantMegas
    PrecioMensual = request.params.PrecioMensual
    TipoPlan_id = request.params.TipoPlan_id
    # acceso de db
    conn = engine.connect()
    if Plan_id == 'E':
        stmt = ("""
                INSERT INTO Plan (CantMegas,PrecioMensual,
                TipoPlan_id)
                VALUES ('{}','{}',{})
                """).format(CantMegas,PrecioMensual,TipoPlan_id)
        conn.execute(stmt)
    else:
        Plan_id = int(request.params.id)
        stmt = ("""
                UPDATE Plan SET
                CantMegas='{}', PrecioMensual='{}',
                TipoPlan_id={}
                WHERE id={}
                """).format(CantMegas,PrecioMensual,TipoPlan_id,Plan_id)
        conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Plan?mensaje=editado')

### DestinosInstalacion ###

@app.route('/DestinosInstalacion', method='GET')
def DestinosInstalacion():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un destino de instalación'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un destino de instalación'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT DI.id, DI.Cobertura, DI.Direccion, DI.CodigoPostal,
            TP.nombre AS TiposPredio,
            TV.nombre AS TiposVivienda,
            D.nombre AS Distrito
            FROM DestinosInstalacion DI
            INNER JOIN TiposPredio TP ON DI.TipoPredio_id = TP.id
            INNER JOIN TiposVivienda TV ON DI.TipoVivienda_id = TV.id
            INNER JOIN Distritos D ON DI.Distrito_id = D.id
            """).format()
    DestinosInstalacion = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'DestinosInstalacion': DestinosInstalacion, 'mensaje': mensaje}
    return template('DestinosInstalacion/index', locals)


@app.route('/DestinosInstalacion/editar', method='GET')
def DestinosInstalacion_editar():
    # pametros
    DestinosInstalacion_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del destino de instalacion
    stmt = ("""
            SELECT * FROM DestinosInstalacion WHERE id={}
            """).format(DestinosInstalacion_id)
    DestinosInstalacion = conn.execute(stmt).fetchone()
    # obtener el listado de tipos de predio
    stmt = ("""
            SELECT id,nombre FROM TiposPredio
            """).format()
    TiposPredio = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de vivienda
    stmt = ("""
            SELECT id,nombre FROM TiposVivienda
            """).format()
    TiposVivienda = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de distritos
    stmt = ("""
            SELECT id,nombre FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'DestinosInstalacion': DestinosInstalacion,
        'titulo': 'Editar Destino de Instalacion',
        'TiposPredio': TiposPredio,
        'TiposVivienda': TiposVivienda,
        'Distritos': Distritos
    }
    return template('DestinosInstalacion/detail', locals)


@app.route('/DestinosInstalacion/eliminar', method='GET')
def DestinosInstalacion_eliminar():
    # pametros
    DestinosInstalacion_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
    DELETE FROM DestinosInstalacions WHERE id={}
  """).format(DestinosInstalacion_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/DestinosInstalacion?mensaje=eliminado')


@app.route('/DestinosInstalacion/crear', method='GET')
def DestinosInstalacion_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la información del destino de instalación
    DestinosInstalacion = {}
    DestinosInstalacion['id'] = 'E'
    DestinosInstalacion['Cobertura'] = ''
    DestinosInstalacion['Direccion'] = ''
    DestinosInstalacion['CodigoPostal'] = ''
    DestinosInstalacion['TipoPredio_id'] = 'E'
    DestinosInstalacion['TipoVivienda_id'] = 'E'
    DestinosInstalacion['Distrito_id'] = 'E'
    # obtener el listado de los tipos de predio
    stmt = ("""
            SELECT id,nombre FROM TiposPredio
            """).format()
    TiposPredio = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de vivienda
    stmt = ("""
            SELECT id,nombre FROM TiposVivienda
            """).format()
    TiposVivienda = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de distritos
    stmt = ("""
            SELECT id,nombre FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'DestinosInstalacion': DestinosInstalacion,
        'titulo': 'Crear Destino de Instalacion',
        'TiposPredio': TiposPredio,
        'TiposVivienda': TiposVivienda,
        'Distritos': Distritos
    }
    return template('DestinosInstalacion/detail', locals)


@app.route('/DestinosInstalacion/grabar', method='POST')
def DestinosInstalacion_grabar():
    # parámetros
    DestinosInstalacion_id = request.params.id
    Cobertura = request.params.Cobertura
    Direccion = request.params.Direccion
    CodigoPostal = request.params.CodigoPostal
    TipoPredio_id = request.params.TipoPredio_id
    TipoVivienda_id = request.params.TipoVivienda_id
    Distrito_id = request.params.Distrito_id

    # acceso de db
    conn = engine.connect()
    if DestinosInstalacion_id == 'E':
        stmt = ("""
            INSERT INTO DestinosInstalacion (Cobertura,Direccion,CodigoPostal,TipoPredio_id,TipoVivienda_id,Distrito_id)
            VALUES ('{}','{}','{}',{},{},{})
            """).format(Cobertura,Direccion,CodigoPostal,TipoPredio_id,TipoVivienda_id,Distrito_id)
        conn.execute(stmt)
    else:
        DestinosInstalacion_id = int(request.params.id)
        stmt = ("""
                UPDATE DestinosInstalacion SET Cobertura='{}', Direccion='{}',CodigoPostal='{}',TipoPredio_id={},TipoVivienda_id={},Distrito_id={}
                WHERE id={}
                """).format(Cobertura,Direccion,CodigoPostal,TipoPredio_id,TipoVivienda_id,Distrito_id,DestinosInstalacion_id)
        conn.execute(stmt)
        # devolver datos a una vista
    redirect('/DestinosInstalacion?mensaje=editado')

### Provincias ###

@app.route('/Provincias', method='GET')
def Provincias():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un destino de instalación'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un destino de instalación'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT P.id, P.nombre,
            D.nombre as Distritos
            FROM Provincias P
            INNER JOIN Distritos D ON P.Distrito_id = D.id
            """).format()
    Provincias = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Provincias': Provincias, 'mensaje': mensaje}
    return template('Provincias/index', locals)

@app.route('/Provincias/editar', method='GET')
def Provincias_editar():
    # parámetros
    Provincias_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información de provincias
    stmt = ("""
            SELECT * FROM Provincias WHERE id={}
            """).format(Provincias_id)
    Provincias = conn.execute(stmt).fetchone()
    # obtener el listado de los distritos
    stmt = ("""
            SELECT id,nombre FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    locals = {
        'Provincias': Provincias,
        'titulo': 'Editar Provincias',
        'Distritos': Distritos
    }
    return template('Provincias/detail', locals)


@app.route('/Provincias/eliminar', method='GET')
def Provincias_eliminar():
    # parámetros
    Provincias_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Provincias WHERE id={}
            """).format(Provincias_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Provincias?mensaje=eliminado')


@app.route('/Provincias/crear', method='GET')
def Provincias_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la información del Provincias
    Provincias = {}
    Provincias['id'] = 'E'
    Provincias['nombre'] = ''
    Provincias['Distrito_id'] = 'E'
    # obtener el listado de distritos
    stmt = ("""
            SELECT id,nombre FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Provincias': Provincias, 
        'titulo': 'Agregar Provincias',
        'Distritos': Distritos
    }
    return template('Provincias/detail', locals)


@app.route('/Provincias/grabar', method='POST')
def Provincias_grabar():
    # parámetros
    Provincias_id = request.params.id
    nombre = request.params.nombre
    Distrito_id = request.params.Distrito_id
    # acceso de db
    conn = engine.connect()
    if Provincias_id == 'E':
        stmt = ("""
                INSERT INTO Provincias (nombre,Distrito_id)
                VALUES ('{}',{})
                """).format(nombre,Distrito_id)
        conn.execute(stmt)
    else:
        Provincias_id = int(request.params.id)
        stmt = ("""
                UPDATE Provincias SET
                nombre='{}', Distrito_id={}
                WHERE id={}
                """).format(nombre,Distrito_id,Provincias_id)
        conn.execute(stmt)
    redirect('/Provincias?mensaje=editado')

### Departamentos ###

@app.route('/Departamentos', method='GET')
def Departamentos():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Departamentos'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Departamentos'
    
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT D.id, D.nombre,
            P.nombre as Provincias,
            INNER JOIN Provincias P ON D.Provincia_ip = P.id
            """).format()
    Departamentos = [dict(r) for r in conn.execute(stmt)]

    # devolver datos a una vista
    locals = {'Departamentos': Departamentos, 'mensaje': mensaje}
    return template('Departamentos/index', locals)

@app.route('/Departamentos/editar', method='GET')
def Departamentos_editar():
    # parámetros
    Departamentos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Departamentos
    stmt = ("""
            SELECT * FROM Departamentos WHERE id={}
            """).format(Departamentos_id)
    Departamentos = conn.execute(stmt).fetchone()
    # obtener la información de Provincias
    stmt = ("""
            SELECT DE.id,DE.nombre,
            P.nombre as Provincias, D.nombre as Distritos
            FROM Departamentos
            INNER JOIN Provincias P ON DE.Provincia_id = P.id
            INNER JOIN Distritos D ON P.Distrito_id = D.id
            """).format()
    Provincias = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Departamentos': Departamentos,
        'titulo': 'Editar Departamentos',
        'Provincias': Provincias
    }
    return template('Departamentos/eliminar', method='GET')


@app.route('/Departamentos/eliminar', method='GET')
def Departamentos_eliminar():
    # parámetros
    Departamentos_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Departamentoss WHERE id={}
            """).format(Departamentos_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Departamentos?mensaje=eliminado')

@app.route('/Departamentos/crear', method='GET')
def Departamentos_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la información del Departamentos
    Departamentos = {}
    Departamentos['id'] = 'E'
    Departamentos['nombre'] = ''
    Departamentos['Pronvincia_id'] = 'E'
    # obtener la información de Provincias
    stmt = ("""
            SELECT DE.id,DE.nombre,
            P.nombre as Provincias, D.nombre as Distritos
            FROM Departamentos
            INNER JOIN Provincias P ON DE.Provincia_id = P.id
            INNER JOIN Distritos D ON P.Distrito_id = D.id
            """).format()
    Provincias = [dict(r) for r in conn.execute(stmt)]
    # devolver datos en una vista
    locals = {
        'Departamentos': Departamentos,
        'titulo': 'Agregar Departamento',
        'Provincias': Provincias
    }
    return template('Departamentos/detail', locals)


@app.route('/Departamentos/grabar', method='POST')
def Departamentos_grabar():
    # parámetros
    Departamentos_id = request.params.id
    nombre = request.params.nombre
    Provincia_id = request.params.Provincia_id
    # acceso de db
    conn = engine.connect()
    if Departamentos_id == 'E':
        stmt = ("""
                INSERT INTO Departamentos (nombre,Provincia_id)
                VALUES ('{}',{})
                """).format(nombre,Provincia_id)
        conn.execute(stmt)
    else:
        Departamentos_id = int(request.params.id)
        stmt = ("""
                UPDATE Departamentos SET
                nombre='{}', Provincia_id={}
                WHERE id={}
                """).format(nombre,Provincia_id,Departamentos_id)
        conn.execute(stmt)
    # devolver daots  una vista
    redirect('/Departamentos?mensaje=editado')


### Clientes ###

@app.route('/Clientes', method='GET')
def Clientes():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un Clientes'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un Clientes'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT C.id, C.nombre, C.ApellidoPaterno, C.ApellidoMaterno, C.Correo, C.Telefono,
            TD.TiposDocumento
            FROM Clientes C
            INNER JOIN TiposDocumento TD ON C.TipoDocumento_id = TD.id
            """).format()
    Clientes = [dict(r) for r in conn.execute(stmt)]
    print(Clientes)
    # devolver datos a una vista
    locals = {'Clientes': Clientes, 'mensaje': mensaje}
    return template('Clientes/index', locals)


@app.route('/Clientes/editar', method='GET')
def Clientes_editar():
    # parámetros
    Clientes_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Clientes
    stmt = ("""
            SELECT * FROM Clientes WHERE id={}
            """).format(Clientes_id)
    Clientes = conn.execute(stmt).fetchone()
    # obtener el listado de los tipos de documento
    stmt = ("""
            SELECT id,nombre FROM TiposDocumento
            """).format()
    TiposDocumento = [dict(r) for r in conn.execute(stmt)]
    # devolver datos en una vista
    locals = {
        'Clientes': Clientes,
        'titulo': 'Editar Cliente',
        'TiposDocumento': TiposDocumento
    }
    return template('Clientes/detail', locals)


@app.route('/Clientes/eliminar', method='GET')
def Clientes_eliminar():
    # pametros
    Clientes_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
    DELETE FROM Clientess WHERE id={}
  """).format(Clientes_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Clientes?mensaje=eliminado')


@app.route('/Clientes/crear', method='GET')
def Clientes_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la información del Clientes
    Clientes = {}
    Clientes['id'] = 'E'
    Clientes['nombre'] = ''
    Clientes['ApellidoPaterno'] = ''
    Clientes['ApellidoMaterno'] = ''
    Clientes['Correo'] = ''
    Clientes['Telefono'] = ''
    Clientes['TipoDocumento_id'] = 'E'
    # obtener el listado de tipos de documento
    stmt = ("""
            SELECT id,nombre FROM TiposDocumento
            """).format()
    sangres = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Clientes': Clientes,
        'titulo': 'Agregar Cliente',
        'TiposDocumento': TiposDocumento
    }
    return template('Clientes/detail', locals)


@app.route('/Clientes/grabar', method='POST')
def Clientes_grabar():
    # pametros
    Clientes_id = request.params.id
    nombre = request.params.nombre
    ApellidoPaterno = request.params.ApellidoPaterno
    ApellidoMaterno = request.params.ApellidoMaterno
    Correo = request.params.Correo
    Telefono = request.params.Telefono
    TipoDocumento_id = request.params.TipoDocumento_id
    # acceso de db
    conn = engine.connect()
    if Clientes_id == 'E':
        stmt = ("""
                INSERT INTO Clientes (nombre, ApellidoPaterno, ApellidoMaterno, Correo, Telefono, TipoDocumento_id)
                VALUES ('{}','{}','{}','{}','{}',{})
                """).format(nombre, ApellidoPaterno, ApellidoMaterno, Correo, Telefono, TipoDocumento_id)
        conn.execute(stmt)
    else:
        Clientes_id = int(request.params.id)
        stmt = ("""
                UPDATE Clientes SET
                nombre='{}',ApellidoPaterno='{}',ApellidoMaterno='{}',Correo='{}',Telefono='{}',
                TipoDocumento={}
                WHERE id={}
                """).format(nombre, ApellidoPaterno, ApellidoMaterno, Correo, Telefono, TipoDocumento_id,Clientes_id)
        conn.execute(stmt)
        # devolver datos a una vista
    redirect('/Clientes?mensaje=editado')

### Colaboradores ###

@app.route('/Colaboradores', method='GET')
def Colaboradores():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un ciudadano'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un ciudadano'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT CO.id, CO.id_Win, CO.nombre, CO.ApellidoPaterno, CO.ApellidoMaterno, CO.Correo, CO.FechaNacimiento, CO.Telefono, CO.FechaIngreso, CO.EstadoWIN, CO.EstadoSUMMUN, CO.Feedback, CO.NumeroDocumento,
            GE.nombre AS Generos, EQ.nombre AS Equipos, TD.nombre AS TiposDocumento, TCOM.nombre AS TiposComision, TCON.nombre AS TiposContrato, NA.nombre AS Nacionalidades, TCOL.nombre AS TiposColaborador, CA.nombre AS Categorias, DI.nombre AS Distritos
            FROM Colaboradores CO
            INNER JOIN Generos GE ON CO.Genero_id = GE.id
            INNER JOIN Equipos EQ ON CO.Equipo_id = EQ.id
            INNER JOIN TiposDocumento TD ON CO.TipoDocumento_id = TD.id
            INNER JOIN TiposComision TCOM ON CO.TipoComision_id = TCOM.id
            INNER JOIN TiposContrato TCON ON CO.TipoContrato_id = TCON.id
            INNER JOIN Nacionalidades NA ON CO.Nacionalidad_id = NA.id
            INNER JOIN TiposColaborador TCOL ON CO.TipoColaborador_id = TCOL.id
            INNER JOIN Categorias CA ON CO.Categoria_id = CA.id
            INNER JOIN Distritos DI ON CO.Distrito_id = DI.id
            """).format()
    Colaboradores = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Colaboradores': Colaboradores, 'mensaje': mensaje}
    return template('Colaboradores/index', locals)


@app.route('/Colaboradores/editar', method='GET')
def Colaboradores_editar():
    # parámetros
    Colaboradores_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del colaborador
    stmt = ("""
            SELECT * FROM Colaboradores WHERE id={}
            """).format(Colaboradores_id)
    Colaboradores = conn.execute(stmt).fetchone()
    # obtener el listado de géneros
    stmt = ("""
            SELECT id,nombre FROM Generos
            """).format()
    Generos = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de equipos
    stmt = ("""
            SELECT id,nombre FROM Equipos
            """).format()
    Equipos = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de documento
    stmt = ("""
            SELECT id,nombre FROM TiposDocumento
            """).format()
    TiposDocumento = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de comisión
    stmt = ("""
            SELECT id,nombre FROM TiposComision
            """).format()
    TiposComision = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de contrato
    stmt = ("""
            SELECT id,nombre FROM TiposContrato
            """).format()
    TiposContrato = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de nacionalidades
    stmt = ("""
            SELECT id,nombre FROM Nacionalidades
            """).format()
    Nacionalidades = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de colaborador
    stmt = ("""
            SELECT id,nombre FROM TiposColaborador
            """).format()
    TiposColaborador = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de categorías
    stmt = ("""
            SELECT id,nombre FROM Categorias
            """).format()
    Categorias = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de distritos
    stmt = ("""
            SELECT id,nombre FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Colaboradores': Colaboradores,
        'titulo': 'Editar Colaborador',
        'Generos': Generos,
        'Equipos': Equipos,
        'TiposDocumento': TiposDocumento,
        'TiposComision': TiposComision,
        'TiposContrato': TiposContrato,
        'TiposColaborador': TiposColaborador,
        'Categorias': Categorias,
        'Distritos': Distritos
    }
    return template('Colaboradores/eliminar', locals)


@app.route('/Colaboradores/eliminar', method='GET')
def Colaboradores_eliminar():
    # pametros
    Colaboradores_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            DELETE FROM Colaboradores WHERE id={}
            """).format(Colaboradores_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Colaboradores?mensaje=eliminado')


@app.route('/Colaboradores/crear', method='GET')
def Colaboradores_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la información del Colaboradores
    Colaboradores = {}
    Colaboradores['id'] = 'E'
    Colaboradores['id_Win'] = ''
    Colaboradores['nombre'] = ''
    Colaboradores['ApellidoPaterno'] = ''
    Colaboradores['ApellidoMaterno'] = ''
    Colaboradores['Correo'] = ''
    Colaboradores['FechaNacimiento'] = ''
    Colaboradores['Telefono'] = ''
    Colaboradores['FechaIngreso'] = ''
    Colaboradores['EstadoWIN'] = ''
    Colaboradores['EstadoSUMMUN'] = ''
    Colaboradores['Feedback'] = ''
    Colaboradores['NumeroDocumento'] = ''
    Colaboradores['Genero_id'] = 'E'
    Colaboradores['Equipo_id'] = 'E'
    Colaboradores['TipoDocumento_id'] = 'E'
    Colaboradores['TipoComision_id'] = 'E'
    Colaboradores['TipoContrato_id'] = 'E'
    Colaboradores['Nacionalidad_id'] = 'E'
    Colaboradores['TipoColaborador_id'] = 'E'
    Colaboradores['Categoria_id'] = 'E'
    Colaboradores['Distrito_id'] = 'E'
    # obtener el listado de géneros
    stmt = ("""
            SELECT id,nombre FROM Generos
            """).format()
    Generos = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de equipos
    stmt = ("""
            SELECT id,nombre FROM Equipos
            """).format()
    Equipos = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de documento
    stmt = ("""
            SELECT id,nombre FROM TiposDocumento
            """).format()
    TiposDocumento = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de comisión
    stmt = ("""
            SELECT id,nombre FROM TiposComision
            """).format()
    TiposComision = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de contrato
    stmt = ("""
            SELECT id,nombre FROM TiposContrato
            """).format()
    TiposContrato = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de nacionalidades
    stmt = ("""
            SELECT id,nombre FROM Nacionalidades
            """).format()
    Nacionalidades = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de tipos de colaborador
    stmt = ("""
            SELECT id,nombre FROM TiposColaborador
            """).format()
    TiposColaborador = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de categorías
    stmt = ("""
            SELECT id,nombre FROM Categorias
            """).format()
    Categorias = [dict(r) for r in conn.execute(stmt)]
    # obtener el listado de distritos
    stmt = ("""
            SELECT id,nombre FROM Distritos
            """).format()
    Distritos = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Colaboradores': Colaboradores,
        'titulo': 'Agregar Colaborador',
        'Generos': Generos,
        'Equipos': Equipos,
        'TiposDocumento': TiposDocumento,
        'TiposComision': TiposComision,
        'TiposColaborador': TiposColaborador,
        'Categorias': Categorias,
        'Distritos': Distritos,
    }
    return template('Colaboradores/detail', locals)


@app.route('/Colaboradores/grabar', method='POST')
def Colaboradores_grabar():
    # parámetros
    Colaboradores_id = request.params.id
    id_Win = request.params.id_Win
    nombre = request.params.nombre
    ApellidoPaterno = request.params.ApellidoPaterno
    ApellidoMaterno = request.params.ApellidoMaterno
    Correo = request.params.Correo
    FechaNacimiento = request.params.FechaNacimiento
    Telefono = request.params.Telefono
    FechaIngreso = request.params.FechaIngreso
    EstadoWIN = request.params.EstadoWIN
    EstadoSUMMUN = request.params.EstadoSUMMUN
    Feedback = request.params.Feedback
    NumeroDocumento = request.params.NumeroDocumento
    Genero_id = request.params.Genero_id
    Equipo_id = request.params.Equipo_id
    TipoDocumento_id = request.params.TipoDocumento_id
    TipoComision_id = request.params.TipoComision_id
    TipoContrato_id = request.params.TipoContrato_id
    Nacionalidad_id = request.params.Nacionalidad_id
    TipoColaborador_id = request.params.TipoColaborador_id
    Categoria_id = request.params.Categoria_id
    Distrito_id = request.params.Distrito_id
    # acceso de db
    conn = engine.connect()
    if Colaboradores_id == 'E':
        stmt = ("""
                INSERT INTO Colaboradores (id_Win,nombre,ApellidoPaterno,ApellidoMaterno,Correo,FechaNacimiento,Telefono,FechaIngreso,EstadoWIN,EstadoSUMMUN,Feedback,NumeroDocumento,Genero_id,Equipo_id,TipoDocumento_id,TipoComision_id,TipoContrato_id,Nacionalidad_id,TipoColaborador_id,Categoria_id,Distrito_id)
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{})
                """).format(id_Win,nombre,ApellidoPaterno,ApellidoMaterno,Correo,FechaNacimiento,Telefono,FechaIngreso,EstadoWIN,EstadoSUMMUN,Feedback,NumeroDocumento,Genero_id,Equipo_id,TipoDocumento_id,TipoComision_id,TipoContrato_id,Nacionalidad_id,TipoColaborador_id,Categoria_id,Distrito_id)
        conn.execute(stmt)
    else:
        Colaboradores_id = int(request.params.id)
        stmt = ("""
                UPDATE Colaboradores SET
                id_Win='{}',nombre='{}',ApellidoPaterno='{}',ApellidoMaterno='{}',Correo='{}',FechaNacimiento='{}',Telefono='{}',FechaIngreso='{}',EstadoWIN='{}',EstadoSUMMUN='{}',Feedback='{}',NumeroDocumento='{}',
                Genero_id={},Equipo_id={},TipoDocumento_id={},TipoComision_id={},TipoContrato_id={},Nacionalidad_id={},TipoColaborador_id={},Categoria_id={},Distrito_id={}
                WHERE id={}
                """).format(id_Win,nombre,ApellidoPaterno,ApellidoMaterno,Correo,FechaNacimiento,Telefono,FechaIngreso,EstadoWIN,EstadoSUMMUN,Feedback,NumeroDocumento,Genero_id,Equipo_id,TipoDocumento_id,TipoComision_id,TipoContrato_id,Nacionalidad_id,TipoColaborador_id,Categoria_id,Distrito_id,Colaboradores_id)
        conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Colaboradores?mensaje=editado')



    