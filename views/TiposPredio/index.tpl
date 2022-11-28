% include('_header.tpl')
  <h1>Tipos Predio</h1>
  <label>{{mensaje}}</label>
  <br>
  <table>
    <thead>
      <th>Nombre</th>
    </thead>
    <tbody>
      % for g in TiposPredio:
      <tr>
        <td>{{g['nombre']}}</td>
        <td>
          <a class="btn" href="/TiposPredio/editar?id={{g['id']}}">Editar</a>
          <a class="btn" href="/TiposPredio/eliminar?id={{g['id']}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <br>
  <a href="/TiposPredio/crear">Agregar Nuevo Tipo de Predio</a>
  <br>
  <a href="/">Volver a la página principal</a>
</body>
</html>