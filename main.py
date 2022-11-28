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


@app.route('/TiposPlan/grabar', method='POST')
def TiposPlan_grabar():
    # parámetros
    TiposPlan_id = request.params.id
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    if TiposPlan_id == 'E':
        stmt = (f"""
                INSERT INTO TiposPlan (nombre)
                VALUES ('{nombre}')
                """)
        conn.execute(stmt)
    else:
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
    redirect('/TiposPlan?mensaje=eliminado')


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


@app.route('/TiposVivienda/grabar', method='POST')
def TiposVivienda_grabar():
    # parámetros
    TiposVivienda_id = request.params.id
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    if TiposVivienda_id == 'E':
        stmt = (f"""
                INSERT INTO TiposVivienda (nombre)
                VALUES ('{nombre}')
                """)
        conn.execute(stmt)
    else:
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
    redirect('/TiposVivienda?mensaje=eliminado')

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
    # obtener la información de TiposPredio
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
        'titulo': 'Crear TiposPredio'
    }
    # plantilla de views
    return template('TiposPredio/detail', locals)


@app.route('/TiposPredio/grabar', method='POST')
def TiposPredio_grabar():
    # parámetros
    TiposPredio_id = request.params.id
    nombre = request.params.nombre
    # acceso de db
    conn = engine.connect()
    if TiposPredio_id == 'E':
        stmt = (f"""
                INSERT INTO TiposPredio (nombre)
                VALUES ('{nombre}')
                """)
        conn.execute(stmt)
    else:
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
    redirect('/TiposPredio?mensaje=eliminado')


### Plan ###

@app.route('/Planes', method='GET')
def Planes():
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
            TP.nombre AS TiposPlan
            FROM Planes P
            INNER JOIN TiposPlan TP ON P.TipoPlan_id = TP.id            
            """).format()
    Planes = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {'Planes': Planes, 'mensaje': mensaje}
    return template('Planes/index', locals)


@app.route('/Planes/editar', method='GET')
def Planes_editar():
    # parámetros
    Planes_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    # obtener la información del Planes
    stmt = ("""
            SELECT * FROM Planes WHERE id={}
            """).format(Planes_id)
    Planes = [dict(r) for r in conn.execute(stmt)][0]
    # obtener la información del tipo de Planes
    stmt = ("""
            SELECT id,nombre FROM TiposPlan
            """).format()
    TiposPlan = [dict(r) for r in conn.execute(stmt)]
    print(TiposPlan)
    # devolver datos en una vista
    locals = {
        'Planes': Planes,
        'titulo': 'Editar Plan',
        'TiposPlan': TiposPlan
    }
    return template('Planes/detail', locals)


@app.route('/Planes/eliminar', method='GET')
def Planes_eliminar():
    # pametros
    Planes_id = int(request.params.id)
    # acceso de db
    conn = engine.connect()
    stmt = ("""
    DELETE FROM Planes WHERE id={}
  """).format(Planes_id)
    conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Planes?mensaje=eliminado')


@app.route('/Planes/crear', method='GET')
def Planes_crear():
    # acceso de db
    conn = engine.connect()
    # obtener la infromación del Planes
    Planes = {}
    Planes['id'] = 'E'
    Planes['cantmegas'] = ''
    Planes['preciomensual'] = ''
    Planes['tipoplan_id'] = 'E'
    # obtener el listado de los tipos de Planeses
    stmt = ("""
            SELECT id,nombre FROM TiposPlan
            """).format()
    TiposPlan = [dict(r) for r in conn.execute(stmt)]
    # devolver daos a una vista
    locals = {
        'Planes': Planes,
        'titulo': 'Agregar Plan',
        'TiposPlan': TiposPlan
    }
    return template('Planes/detail', locals)


@app.route('/Planes/grabar', method='POST')
def Planes_grabar():
    # parámetros
    Planes_id = request.params.id
    CantMegas = request.params.CantMegas
    PrecioMensual = request.params.PrecioMensual
    TipoPlan_id = request.params.TipoPlan_id
    # acceso de db
    conn = engine.connect()
    if Planes_id == 'E':
        stmt = ("""
                INSERT INTO Planes (CantMegas,PrecioMensual,
                TipoPlan_id)
                VALUES ('{}','{}',{})
                """).format(CantMegas,PrecioMensual,TipoPlan_id)
        conn.execute(stmt)
    else:
        Planes_id = int(request.params.id)
        stmt = ("""
                UPDATE Planes SET
                CantMegas='{}', PrecioMensual='{}',
                TipoPlan_id={}
                WHERE id={}
                """).format(CantMegas,PrecioMensual,TipoPlan_id,Planes_id)
        conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Planes?mensaje=editado')

### Clientes ###

@app.route('/Clientes', method='GET')
def Clientes():
    # parámetros
    mensaje = request.params.mensaje
    if mensaje != '' and mensaje == 'editado':
        mensaje = 'Se ha editado un cliente'
    elif mensaje == 'eliminado':
        mensaje = 'Se ha eliminado un cliente'
    # acceso de db
    conn = engine.connect()
    stmt = ("""
            SELECT C.id, C.nombre, C.ApellidoPaterno, C.ApellidoMaterno, C.Correo, C.Telefono, C.NumeroDocumento,
            TD.nombre AS TiposDocumento
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
            DELETE FROM Clientes WHERE id={}
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
    Clientes['apellidopaterno'] = ''
    Clientes['apellidomaterno'] = ''
    Clientes['correo'] = ''
    Clientes['telefono'] = ''
    Clientes['numerodocumento'] = ''
    Clientes['tipodocumento_id'] = 'E'
    # obtener el listado de tipos de documento
    stmt = ("""
            SELECT id,nombre FROM TiposDocumento
            """).format()
    TiposDocumento = [dict(r) for r in conn.execute(stmt)]
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
    NumeroDocumento = request.params.NumeroDocumento
    TipoDocumento_id = request.params.TipoDocumento_id
    # acceso de db
    conn = engine.connect()
    if Clientes_id == 'E':
        stmt = ("""
                INSERT INTO Clientes (nombre, ApellidoPaterno, ApellidoMaterno, Correo, Telefono, NumeroDocumento, TipoDocumento_id)
                VALUES ('{}','{}','{}','{}','{}','{}',{})
                """).format(nombre, ApellidoPaterno, ApellidoMaterno, Correo, Telefono, NumeroDocumento, TipoDocumento_id)
        conn.execute(stmt)
    else:
        stmt = ("""
                UPDATE Clientes SET
                nombre='{}',ApellidoPaterno='{}',ApellidoMaterno='{}',Correo='{}',Telefono='{}',NumeroDocumento='{}',
                TipoDocumento_id={}
                WHERE id={}
                """).format(nombre, ApellidoPaterno, ApellidoMaterno, Correo, Telefono, NumeroDocumento, TipoDocumento_id,Clientes_id)
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
            SELECT CO.id, CO.id_Win, CO.nombre, CO.ApellidoPaterno, CO.ApellidoMaterno, CO.Correo, CO.FechaNacimiento, CO.Telefono, CO.FechaIngreso, CO.EstadoWIN, CO.EstadoSUMMUN, CO.NumeroDocumento,
            GE.nombre AS Generos, EQ.nombre AS Equipos, TD.nombre AS TiposDocumento, TCOM.nombre AS TiposComision, TCON.nombre AS TiposContrato, NA.nombre AS Nacionalidades, TCOL.nombre AS TiposColaborador, CA.nombre AS Categorias, DI.nombre AS DistritosProvincias
            FROM Colaboradores CO
            INNER JOIN Generos GE ON CO.Genero_id = GE.id
            INNER JOIN Equipos EQ ON CO.Equipo_id = EQ.id
            INNER JOIN TiposDocumento TD ON CO.TipoDocumento_id = TD.id
            INNER JOIN TiposComision TCOM ON CO.TipoComision_id = TCOM.id
            INNER JOIN TiposContrato TCON ON CO.TipoContrato_id = TCON.id
            INNER JOIN Nacionalidades NA ON CO.Nacionalidad_id = NA.id
            INNER JOIN TiposColaborador TCOL ON CO.TipoColaborador_id = TCOL.id
            INNER JOIN Categorias CA ON CO.Categoria_id = CA.id
            INNER JOIN DistritosProvincias DI ON CO.DistritoProvincia_id = DI.id
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
    # obtener el listado de distritos y provincias
    stmt = ("""
            SELECT id,nombre FROM DistritosProvincias
            """).format()
    DistritosProvincias = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Colaboradores': Colaboradores,
        'titulo': 'Editar Colaborador',
        'Generos': Generos,
        'Equipos': Equipos,
        'TiposDocumento': TiposDocumento,
        'TiposComision': TiposComision,
        'TiposContrato': TiposContrato,
        'Nacionalidades': Nacionalidades,
        'TiposColaborador': TiposColaborador,
        'Categorias': Categorias,
        'DistritosProvincias': DistritosProvincias
    }
    return template('Colaboradores/detail', locals)


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
    Colaboradores['id_win'] = ''
    Colaboradores['nombre'] = ''
    Colaboradores['apellidopaterno'] = ''
    Colaboradores['apellidomaterno'] = ''
    Colaboradores['correo'] = ''
    Colaboradores['fechanacimiento'] = ''
    Colaboradores['telefono'] = ''
    Colaboradores['fechaingreso'] = ''
    Colaboradores['estadowin'] = ''
    Colaboradores['estadosummun'] = ''
    #Colaboradores['Feedback'] = ''
    Colaboradores['numerodocumento'] = ''
    Colaboradores['genero_id'] = 'E'
    Colaboradores['equipo_id'] = 'E'
    Colaboradores['tipodocumento_id'] = 'E'
    Colaboradores['tipocomision_id'] = 'E'
    Colaboradores['tipocontrato_id'] = 'E'
    Colaboradores['nacionalidad_id'] = 'E'
    Colaboradores['tipocolaborador_id'] = 'E'
    Colaboradores['categoria_id'] = 'E'
    Colaboradores['distritoprovincia_id'] = 'E'
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
    # obtener el listado de distritos y provincias
    stmt = ("""
            SELECT id,nombre FROM DistritosProvincias
            """).format()
    DistritosProvincias = [dict(r) for r in conn.execute(stmt)]
    # devolver datos a una vista
    locals = {
        'Colaboradores': Colaboradores,
        'titulo': 'Agregar Colaborador',
        'Generos': Generos,
        'Equipos': Equipos,
        'TiposDocumento': TiposDocumento,
        'TiposComision': TiposComision,
        'TiposContrato': TiposContrato,
        'Nacionalidades': Nacionalidades,
        'TiposColaborador': TiposColaborador,
        'Categorias': Categorias,
        'DistritosProvincias': DistritosProvincias,
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
    #Feedback = request.params.Feedback
    NumeroDocumento = request.params.NumeroDocumento
    Genero_id = request.params.Genero_id
    Equipo_id = request.params.Equipo_id
    TipoDocumento_id = request.params.TipoDocumento_id
    TipoComision_id = request.params.TipoComision_id
    TipoContrato_id = request.params.TipoContrato_id
    Nacionalidad_id = request.params.Nacionalidad_id
    TipoColaborador_id = request.params.TipoColaborador_id
    Categoria_id = request.params.Categoria_id
    DistritoProvincia_id = request.params.DistritoProvincia_id
    # acceso de db
    conn = engine.connect()
    if Colaboradores_id == 'E':
        stmt = ("""
                INSERT INTO Colaboradores (id_Win,nombre,ApellidoPaterno,ApellidoMaterno,Correo,FechaNacimiento,Telefono,FechaIngreso,EstadoWIN,EstadoSUMMUN,NumeroDocumento,Genero_id,Equipo_id,TipoDocumento_id,TipoComision_id,TipoContrato_id,Nacionalidad_id,TipoColaborador_id,Categoria_id,DistritoProvincia_id)
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},{})
                """).format(id_Win,nombre,ApellidoPaterno,ApellidoMaterno,Correo,FechaNacimiento,Telefono,FechaIngreso,EstadoWIN,EstadoSUMMUN,NumeroDocumento,Genero_id,Equipo_id,TipoDocumento_id,TipoComision_id,TipoContrato_id,Nacionalidad_id,TipoColaborador_id,Categoria_id,DistritoProvincia_id)
        conn.execute(stmt)
    else:
        stmt = ("""
                UPDATE Colaboradores SET
                id_Win='{}',nombre='{}',ApellidoPaterno='{}',ApellidoMaterno='{}',Correo='{}',FechaNacimiento='{}',Telefono='{}',FechaIngreso='{}',EstadoWIN='{}',EstadoSUMMUN='{}',NumeroDocumento='{}',
                Genero_id={},Equipo_id={},TipoDocumento_id={},TipoComision_id={},TipoContrato_id={},Nacionalidad_id={},TipoColaborador_id={},Categoria_id={},DistritoProvincia_id={}
                WHERE id={}
                """).format(id_Win,nombre,ApellidoPaterno,ApellidoMaterno,Correo,FechaNacimiento,Telefono,FechaIngreso,EstadoWIN,EstadoSUMMUN,NumeroDocumento,Genero_id,Equipo_id,TipoDocumento_id,TipoComision_id,TipoContrato_id,Nacionalidad_id,TipoColaborador_id,Categoria_id,DistritoProvincia_id,Colaboradores_id)
        conn.execute(stmt)
    # devolver datos a una vista
    redirect('/Colaboradores?mensaje=editado')


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8081, debug=True, reloader=True)