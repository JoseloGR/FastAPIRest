CLIENTS = [
  {'id': 1, 'nombre': 'Cliente_1', 'usuario_id': 1, 'activo': 1},
  {'id': 2, 'nombre': 'Cliente_2', 'usuario_id': 2, 'activo': 1}
]

USUARIOS = [
  {'id': 1, 'nombre': 'Usuario_1', 'equipo_id': '1234567890', 'activo': 1},
  {'id': 2, 'nombre': 'Usuario_3', 'equipo_id': '0987654321', 'activo': 2}
]

VENTAS = [
  { 'id': 1, 'fecha': '2021-05-03 12:30:00', 'monto': 35000, 'cliente_id': 1, 'cliente_nombre': 'Cliente_1', 'usuario_id': 1, 'usuario_nombre': 'Usuario_1', 'activo': 1, 'equipo_id': 1, 'equipo_nombre': 'Equipo_1' },
  { 'id': 2, 'fecha': '2021-05-04 12:30:00', 'monto': 20000, 'cliente_id': 1, 'cliente_nombre': 'Cliente_1', 'usuario_id': 2, 'usuario_nombre': 'Usuario_3', 'activo': 1, 'equipo_id': 2, 'equipo_nombre': 'Equipo_2' },
  { 'id': 3, 'fecha': '2021-05-05 12:30:00', 'monto': 25000, 'cliente_id': 2, 'cliente_nombre': 'Cliente_2', 'usuario_id': 1, 'usuario_nombre': 'Usuario_1', 'activo': 1, 'equipo_id': 1, 'equipo_nombre': 'Equipo_1' },
  { 'id': 4, 'fecha': '2021-05-06 12:30:00', 'monto': 11000, 'cliente_id': 2, 'cliente_nombre': 'Cliente_2', 'usuario_id': 2, 'usuario_nombre': 'Usuario_3', 'activo': 1, 'equipo_id': 2, 'equipo_nombre': 'Equipo_2' },
  { 'id': 5, 'fecha': '2021-06-05 12:30:00', 'monto': 40000, 'cliente_id': 1, 'cliente_nombre': 'Cliente_1', 'usuario_id': 1, 'usuario_nombre': 'Usuario_1', 'activo': 1, 'equipo_id': 1, 'equipo_nombre': 'Equipo_1' },
  { 'id': 6, 'fecha': '2021-07-06 12:30:00', 'monto': 10000, 'cliente_id': 2, 'cliente_nombre': 'Cliente_2', 'usuario_id': 2, 'usuario_nombre': 'Usuario_3', 'activo': 1, 'equipo_id': 2, 'equipo_nombre': 'Equipo_2' }
]

CAT_EQUIPOS = [
  {'id': 1, 'nombre': 'Equipo_1'},
  {'id': 2, 'nombre': 'Equipo_2'}
]

CAT_USUARIOS = [
  {'id': 1, 'nombre': 'Usuario_1', 'equipo_id': '1'},
  {'id': 2, 'nombre': 'Usuario_3', 'equipo_id': '2'}
]