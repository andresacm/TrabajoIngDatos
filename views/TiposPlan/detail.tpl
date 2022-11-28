% include('_header.tpl')
  <h1>{{titulo}}</h1>
  <form action="/TiposPlan/grabar" method="post">
    <input type="hidden" name="id" value="{{TiposPlan['id']}}"><br>
    <label for="name">Nombre:</label><br>
    <input type="text" id="nombre" name="nombre" value="{{TiposPlan['nombre']}}">
    <br><br>
    <button class="btn">Guardar Cambios</button>
  </form>
</body>
</html>