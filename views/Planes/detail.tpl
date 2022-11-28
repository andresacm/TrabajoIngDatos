% include('_header.tpl')
  <h1>{{titulo}}</h1>
  <form action="/Planes/grabar" method="post">
    <input type="hidden" name="id" value="{{Planes['id']}}"><br>
    <label for="name">Cantidad Megas:</label><br>
    <input type="text" id="CantMegas" name="CantMegas" value="{{Planes['cantmegas']}}">
    <br>
    <label for="name">Precio Mensual:</label><br>
    <input type="text" id="PrecioMensual" name="PrecioMensual" value="{{Planes['preciomensual']}}">
    <br>
    <label for="name">Tipo Plan:</label><br>
    <select name="TipoPlan_id">
      % for s in TiposPlan:
        % if Planes['tipoplan_id'] == s['id']: 
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