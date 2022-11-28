% include('_header.tpl')
  <h1>Colaboradores</h1>
  <label>{{mensaje}}</label>
  <table>
    <thead>
      <th>ID WIN</th>
      <th>Nombre Completo</th>
      <th>Correo</th>
      <th>Fecha de nacimiento</th>
      <th>Teléfono</th>
      <th>Fecha de Ingreso</th>
      <th>Estado WIN</th>
      <th>Estado SUMMUN</th>
      <th>Número de documento</th>
      <th>Género</th>
      <th>Equipo</th>
      <th>Tipo de documento</th>
      <th>Tipo comisión</th>
      <th>Tipo contrato</th>
      <th>Nacionalidad</th>
      <th>Tipo colaborador</th>
      <th>Categoria</th>
      <th>DistritoProvincia</th>
    </thead>
    <tbody>
      % for g in Colaboradores:
      <tr>
        <td>{{g['id_win']}}</td>
        <td>{{g['nombre'] + ' ' + g['apellidopaterno'] + ' ' + g['apellidomaterno']}}</td>
        <td>{{g['correo']}}</td>
        <td>{{g['fechanacimiento']}}</td>
        <td>{{g['telefono']}}</td>
        <td>{{g['fechaingreso']}}</td>
        <td>{{g['estadowin']}}</td>
        <td>{{g['estadosummun']}}</td>
        <td>{{g['numerodocumento']}}</td>
        <td>{{g['generos']}}</td>
        <td>{{g['equipos']}}</td>
        <td>{{g['tiposdocumento']}}</td>
        <td>{{g['tiposcomision']}}</td>
        <td>{{g['tiposcontrato']}}</td>
        <td>{{g['nacionalidades']}}</td>
        <td>{{g['tiposcolaborador']}}</td>
        <td>{{g['categorias']}}</td>
        <td>{{g['distritosprovincias']}}</td>

        <td>
          <a class="btn" href="/Colaboradores/editar?id={{g['id']}}">Editar</a>
          <a class="btn" href="/Colaboradores/eliminar?id={{g['id']}}">Eliminar</a>
        </td>
      </tr>
      % end
    </tbody>
  </table>
  <a href="/Colaboradores/crear">Agregar Nuevo Colaborador</a>
  <br>
  <a href="/">Volver a la página principal</a>
  <br>
</body>
</html>