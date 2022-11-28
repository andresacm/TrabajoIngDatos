from bottle import Bottle, run, template

app = Bottle()

@app.route('/', method='GET')
def home():
  return template('home')

@app.route('/ventas', method='GET')
def ventas():
  return template('ventas')

@app.route('/ventas/colaboradores', method='GET')
def colaboradores():
  return template('colaboradores')

@app.route('/ventas/destinosinstalacion', method='GET')
def destinosinstalacion():
  return template('destinosinstalacion')



if __name__ == '__main__':
  run(
    app, 
    host='0.0.0.0', 
    port=8081, 
    debug=True, 
    reloader=True
  )