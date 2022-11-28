% include('_header.tpl')
  <h1>{{titulo}}</h1>
  <form action="/Clientes/grabar" method="post">
    <input type="hidden" name="id" value="{{Clientes['id']}}"><br>
    
    <label for="name">Nombre:</label><br>
    <input type="text" id="nombre" name="nombre" value="{{Clientes['nombre']}}">
    <br>

    <label for="name">Apellido Paterno:</label><br>
    <input type="text" id="ApellidoPaterno" name="ApellidoPaterno" value="{{Clientes['apellidopaterno']}}">
    <br>

    <label for="name">Apellido Materno:</label><br>
    <input type="text" id="ApellidoMaterno" name="ApellidoMaterno" value="{{Clientes['apellidomaterno']}}">
    <br>

    <label for="name">Correo:</label><br>
    <input type="text" id="Correo" name="Correo" value="{{Clientes['correo']}}">
    <br>
    
    <label for="name">Teléfono:</label><br>
    <input type="text" id="Telefono" name="Telefono" value="{{Clientes['telefono']}}">
    <br>
    
    <label for="name">Número de documento:</label><br>
    <input type="text" id="NumeroDocumento" name="NumeroDocumento" value="{{Clientes['numerodocumento']}}">
    <br>

    <label for="name">Tipo de documento</label><br>
    <select name="TipoDocumento_id">
      % for s in TiposDocumento:
        % if Clientes['tipodocumento_id'] == s['id']: 
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