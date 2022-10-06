class Alumno: 
  nombre = None
  calificacion = 0
  def __init__(self, nombre, calificacion):

    self.nombre=nombre
    self.calificacion=calificacion
    
    if calificacion < 6:
      print("la calificación de",self.nombre, "es", self.calificacion,"por lo tanto NO ha aprobado")
    else: 
       print("la calificación de",self.nombre, "es", self.calificacion,"por lo tanto SI ha aprobado")


nuevoAlumno= Alumno("Juan",5)
      

  