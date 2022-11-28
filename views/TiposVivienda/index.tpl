% include('_header.tpl')
  <h1>Tipos Vivienda</h1>
  <label>{{mensaje}}</label>
  <br>
  <table>
    <thead>
      <th>Nombre</th>
    </thead>
    <tbody>
      % for g in TiposVivienda:
      <tr>
        <td>{{g['nombre']}}</td>
        <td>
          <a class="btn" href="/TiposVivienda/editar?id={{g['id']}}">Editar</a>
          <a class="btn" href="/TiposVivienda/eliminar?id={{g['id']}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <br>
  <a href="/TiposVivienda/crear">Agregar Nuevo Tipo de Vivienda</a>
  <br>
  <a href="/">Volver a la página principal</a>
</body>
</html>