% include('_header.tpl')
  <h1>{{titulo}}</h1>
  <form action="/Colaboradores/grabar" method="post">
    <input type="hidden" name="id" value="{{Colaboradores['id']}}"><br>
    
    <label for="name">ID WIN:</label><br>
    <input type="text" id="id_Win" name="id_Win" value="{{Colaboradores['id_win']}}">
    <br>

    <label for="name">Nombres:</label><br>
    <input type="text" id="nombre" name="nombre" value="{{Colaboradores['nombre']}}">
    <br>

    <label for="name">Apellido Paterno:</label><br>
    <input type="text" id="ApellidoPaterno" name="ApellidoPaterno" value="{{Colaboradores['apellidopaterno']}}">
    <br>

    <label for="name">Apellido Materno:</label><br>
    <input type="text" id="ApellidoMaterno" name="ApellidoMaterno" value="{{Colaboradores['apellidomaterno']}}">
    <br>

    <label for="name">Correo:</label><br>
    <input type="text" id="Correo" name="Correo" value="{{Colaboradores['correo']}}">
    <br>

    <label for="name">Fecha Nacimiento:</label><br>
    <input type="text" id="FechaNacimiento" name="FechaNacimiento" value="{{Colaboradores['fechanacimiento']}}">
    <br>  

    <label for="name">Teléfono:</label><br>
    <input type="text" id="Telefono" name="Telefono" value="{{Colaboradores['telefono']}}">
    <br>

    <label for="name">Fecha de Ingreso:</label><br>
    <input type="text" id="FechaIngreso" name="FechaIngreso" value="{{Colaboradores['fechaingreso']}}">
    <br>

    <label for="name">Estado WIN:</label><br>
    <input type="text" id="EstadoWIN" name="EstadoWIN" value="{{Colaboradores['estadowin']}}">
    <br>

    <label for="name">Estado SUMMUN:</label><br>
    <input type="text" id="EstadoSUMMUN" name="EstadoSUMMUN" value="{{Colaboradores['estadosummun']}}">
    <br>

    <label for="name">Número de documento:</label><br>
    <input type="text" id="NumeroDocumento" name="NumeroDocumento" value="{{Colaboradores['numerodocumento']}}">
    <br>

    <label for="name">Genero:</label><br>
    <select name="Genero_id">
      % for s in Generos:
        % if Colaboradores['genero_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Equipo:</label><br>
    <select name="Equipo_id">
      % for s in Equipos:
        % if Colaboradores['equipo_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Tipo de documento:</label><br>
    <select name="TipoDocumento_id">
      % for s in TiposDocumento:
        % if Colaboradores['tipodocumento_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Tipo de comisión:</label><br>
    <select name="TipoComision_id">
      % for s in TiposComision:
        % if Colaboradores['tipocomision_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Tipo de contrato:</label><br>
    <select name="TipoContrato_id">
      % for s in TiposContrato:
        % if Colaboradores['tipocontrato_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Nacionalidad:</label><br>
    <select name="Nacionalidad_id">
      % for s in Nacionalidades:
        % if Colaboradores['nacionalidad_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Tipo colaborador:</label><br>
    <select name="TipoColaborador_id">
      % for s in TiposColaborador:
        % if Colaboradores['tipocolaborador_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Categoría:</label><br>
    <select name="Categoria_id">
      % for s in Categorias:
        % if Colaboradores['categoria_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>

    <label for="name">Distrito Provincia:</label><br>
    <select name="DistritoProvincia_id">
      % for s in DistritosProvincias:
        % if Colaboradores['distritoprovincia_id'] == s['id']: 
          <option selected value="{{s['id']}}">{{s['nombre']}}</option>
        % else:
          <option value="{{s['id']}}">{{s['nombre']}}</option>
        % end
      % end
    </select>
    <br>
    <br>
    <br>
    <button class="btn">Guardar Cambios</button>
  </form>
</body>
</html>