% include('_header.tpl')
  <h1>Tipos Plan</h1>
  <label>{{mensaje}}</label>
  <br>
  <table>
    <thead>
      <th>Nombre</th>
    </thead>
    <tbody>
      % for g in TiposPlan:
      <tr>
        <td>{{g['nombre']}}</td>
        <td>
          <a class="btn" href="/TiposPlan/editar?id={{g['id']}}">Editar</a>
          <a class="btn" href="/TiposPlan/eliminar?id={{g['id']}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <br>
  <a href="/TiposPlan/crear">Agregar Nuevo Tipo de Plan</a>
  <br>
  <a href="/">Volver a la página principal</a>
</body>
</html>