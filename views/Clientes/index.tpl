% include('_header.tpl')
  <h1>Clientes</h1>
  <label>{{mensaje}}</label>
  <table>
    <thead>
      <th>Nombre Completo</th>
      <th>Correo</th>
      <th>Teléfono</th>
      <th>Número de documento</th>
      <th>Tipo de documento</th>
    </thead>
    <tbody>
      % for g in Clientes:
      <tr>
        <td>{{g['nombre'] + ' ' + g['apellidopaterno'] + ' ' + g['apellidomaterno']}}</td>
        <td>{{g['correo']}}</td>
        <td>{{g['telefono']}}</td>
        <td>{{g['numerodocumento']}}</td>
        <td>{{g['tiposdocumento']}}</td>
        <td>
          <a class="btn" href="/Clientes/editar?id={{g['id']}}">Editar</a>
          <a class="btn" href="/Clientes/eliminar?id={{g['id']}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <br>
  <a href="/Clientes/crear">Agregar Nuevo Cliente</a>
  <br>
  <a href="/">Volver a la página principal</a>
</body>
</html>