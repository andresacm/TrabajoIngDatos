% include('_header.tpl')
  <h1>Plan</h1>
  <label>{{mensaje}}</label>
  <br>
  <table>
    <thead>
      <th>Cantidad de megas</th>
      <th>Precio Mensual</th>
      <th>Tipos de Planes</th>
    </thead>
    <tbody>
      % for g in Planes:
      <tr>
        <td>{{g['cantmegas']}}</td>
        <td>{{g['preciomensual']}}</td>
        <td>{{g['tiposplan']}}</td>
        <td>
          <a class="btn" href="/Planes/editar?id={{g['id']}}">Editar</a>
          <a class="btn" href="/Planes/eliminar?id={{g['id']}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <a href="/Planes/crear">Agregar Nuevo Plan</a>
  <br>
  <a href="/">Volver a la página principal</a>
  <br>
</body>
</html>
