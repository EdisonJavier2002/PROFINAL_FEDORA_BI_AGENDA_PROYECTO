from django.shortcuts import render, redirect, get_object_or_404
from .models import Anio, AyudaMemoria, Evento, Modalidad, Notificacion, Direccion, Usuario, Unidad, Tipo, Poa, ObjetivoCantonal, ObjetivoDesarrollo, ObjetivoNacional, ObjetivoPdyot, Parroquia, Prioridad, Proyecto, Vocativo, Delegado
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Para los dashboard
from django.db.models import Count

# Home
def home(request):
    return render(request,"home.html")

# Dashboard
def dashboard(request):
    return render(request,"dashboard.html")
# --------------------------------------AÑO--------------------------------------------------------
# Listado de Años
def listadoAnios(request):
    anios = Anio.objects.all()
    return render(request, "listadoAnios.html", {'anios': anios})

# Eliminar Año
def eliminarAnio(request, id):
    anioEliminar = Anio.objects.get(codigo_ani=id)
    anioEliminar.delete()
    messages.success(request, "Año eliminado exitosamente.")
    return redirect('listadoAnios')

# Formulario Nuevo Año
def nuevoAnio(request):
    return render(request, 'nuevoAnio.html')

# Guardar Nuevo Año
def guardarAnio(request):
    nombre_ani = request.POST["nombre_ani"]
    Anio.objects.create(
        nombre_ani=nombre_ani
    )
    messages.success(request, "Año registrado exitosamente.")
    return redirect('listadoAnios')

# Vista para editar Año
def editarAnio(request, id):
    anioEditar = Anio.objects.get(codigo_ani=id)
    return render(request, 'editarAnio.html', {'anioEditar': anioEditar})

# Actualizar Año
def procesarActualizacionAnio(request):
    codigo_ani = request.POST['codigo_ani']
    nombre_ani = request.POST['nombre_ani']

    # Actualizar el año
    anio = Anio.objects.get(codigo_ani=codigo_ani)
    anio.nombre_ani = nombre_ani
    anio.save()

    messages.success(request, "Año actualizado exitosamente.")
    return redirect('listadoAnios')


# --------------------------------------AYUDA MEMORIA--------------------------------------------------------
# Listado de AyudaMemoria
def listadoAyudaMemoria(request):
    ayuda_memorias = AyudaMemoria.objects.all()
    eventos = Evento.objects.all()  # Asumiendo que tienes un modelo Evento
    return render(request, "listadoAyudaMemoria.html", {'ayuda_memorias': ayuda_memorias, 'eventos': eventos})

# Eliminar AyudaMemoria
def eliminarAyudaMemoria(request, id):
    ayuda_memoriaEliminar = AyudaMemoria.objects.get(codigo_am=id)
    ayuda_memoriaEliminar.delete()
    messages.success(request, "Ayuda memoria eliminada exitosamente.")
    return redirect('listadoAyudaMemoria')

# Formulario Nueva AyudaMemoria
def nuevaAyudaMemoria(request):
    eventos = Evento.objects.all()  # Obtener todos los eventos
    return render(request, 'nuevaAyudaMemoria.html', {'eventos': eventos})

# Guardar Nueva AyudaMemoria
def guardarAyudaMemoria(request):
    inversion_proyecto = request.POST["inversion_proyecto_am"]
    inversion_global = request.POST["inversion_global_am"]
    beneficiarios = request.POST["beneficiarios_am"]
    descripcion = request.POST["descripcion_am"]
    lugar = request.POST["lugar_am"]
    codigo_eve = request.POST["codigo_eve"]
    evento = Evento.objects.get(codigo_eve=codigo_eve)

    AyudaMemoria.objects.create(
        inversion_proyecto_am=inversion_proyecto,
        inversion_global_am=inversion_global,
        beneficiarios_am=beneficiarios,
        descripcion_am=descripcion,
        lugar_am=lugar,
        codigo_eve=evento
    )
    messages.success(request, "Ayuda memoria registrada exitosamente.")
    return redirect('listadoAyudaMemoria')

# Vista para editar AyudaMemoria
def editarAyudaMemoria(request, id):
    ayuda_memoriaEditar = AyudaMemoria.objects.get(codigo_am=id)
    eventos = Evento.objects.all()
    return render(request, 'editarAyudaMemoria.html', {'ayuda_memoriaEditar': ayuda_memoriaEditar, 'eventos': eventos})

# Actualizar AyudaMemoria
def procesarActualizacionAyudaMemoria(request):
    codigo_am = request.POST['codigo_am']
    inversion_proyecto = request.POST['inversion_proyecto_am']
    inversion_global = request.POST['inversion_global_am']
    beneficiarios = request.POST['beneficiarios_am']
    descripcion = request.POST['descripcion_am']
    lugar = request.POST['lugar_am']
    codigo_eve = request.POST['codigo_eve']

    evento = Evento.objects.get(codigo_eve=codigo_eve)
    
    ayuda_memoria = AyudaMemoria.objects.get(codigo_am=codigo_am)
    ayuda_memoria.inversion_proyecto_am = inversion_proyecto
    ayuda_memoria.inversion_global_am = inversion_global
    ayuda_memoria.beneficiarios_am = beneficiarios
    ayuda_memoria.descripcion_am = descripcion
    ayuda_memoria.lugar_am = lugar
    ayuda_memoria.codigo_eve = evento
    ayuda_memoria.save()

    messages.success(request, "Ayuda memoria actualizada exitosamente.")
    return redirect('listadoAyudaMemoria')

# --------------------------------------MODALIDAD--------------------------------------------------------
# Listado de Modalidades
def listadoModalidades(request):
    modalidades = Modalidad.objects.all()
    return render(request, "listadoModalidades.html", {'modalidades': modalidades})

# Eliminar Modalidad
def eliminarModalidad(request, codigo):
    modalidadEliminar = Modalidad.objects.get(codigo_mod=codigo)
    modalidadEliminar.delete()
    messages.success(request, "Modalidad eliminada exitosamente.")
    return redirect('listadoModalidades')

# Formulario Nueva Modalidad
def nuevaModalidad(request):
    return render(request, 'nuevoModalidad.html')

# Guardar Nueva Modalidad
def guardarModalidad(request):
    nombre = request.POST["nombre_mod"]
    Modalidad.objects.create(
        nombre_mod=nombre
    )
    messages.success(request, "Modalidad registrada exitosamente.")
    return redirect('listadoModalidades')


# Vista para editar modalidad
def editarModalidad(request, codigo):
    modalidadEditar = Modalidad.objects.get(codigo_mod=codigo)
    return render(request, 'editarModalidad.html', {'modalidadEditar': modalidadEditar})

# Actualizar Modalidad
def procesarActualizacionModalidad(request):
    codigo_mod = request.POST['codigo_mod']
    nombre = request.POST['nombre_mod']

    modalidad = Modalidad.objects.get(codigo_mod=codigo_mod)
    modalidad.nombre_mod = nombre
    modalidad.save()

    messages.success(request, "Modalidad actualizada exitosamente.")
    return redirect('listadoModalidades')

# --------------------------------------NOTIFICACIONES--------------------------------------------------------
# Listado de Notificaciones
def listadoNotificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, "listadoNotificaciones.html", {'notificaciones': notificaciones})

# Eliminar Notificación
def eliminarNotificacion(request, id):
    notificacionEliminar = Notificacion.objects.get(codigo_not=id)
    notificacionEliminar.delete()
    messages.success(request, "Notificación eliminada exitosamente.")
    return redirect('listadoNotificaciones')

# Formulario Nueva Notificación
def nuevaNotificacion(request):
    return render(request, 'nuevaNotificacion.html')

# Guardar Nueva Notificación
def guardarNotificacion(request):
    mensaje = request.POST["mensaje_not"]
    emisor = request.POST["emisor_not"]
    receptor = request.POST["receptor_not"]
    estado = request.POST["estado_not"]
    fecha = request.POST["fecha_not"]
    codigo_eve = request.POST["codigo_eve"]
    push_not = request.POST["push_not"]
    
    Notificacion.objects.create(
        mensaje_not=mensaje,
        emisor_not=emisor,
        receptor_not=receptor,
        estado_not=estado,
        fecha_not=fecha,
        codigo_eve=codigo_eve,
        push_not=push_not
    )
    messages.success(request, "Notificación registrada exitosamente.")
    return redirect('listadoNotificaciones')

# Vista para editar notificación
def editarNotificacion(request, id):
    notificacionEditar = Notificacion.objects.get(codigo_not=id)
    return render(request, 'editarNotificacion.html', {'notificacionEditar': notificacionEditar})

# Actualizar Notificación
def procesarActualizacionNotificacion(request):
    codigo_not = request.POST['codigo_not']
    mensaje = request.POST['mensaje_not']
    emisor = request.POST['emisor_not']
    receptor = request.POST['receptor_not']
    estado = request.POST['estado_not']
    fecha = request.POST['fecha_not']
    codigo_eve = request.POST['codigo_eve']
    push_not = request.POST['push_not']
    
    notificacion = Notificacion.objects.get(codigo_not=codigo_not)
    notificacion.mensaje_not = mensaje
    notificacion.emisor_not = emisor
    notificacion.receptor_not = receptor
    notificacion.estado_not = estado
    notificacion.fecha_not = fecha
    notificacion.codigo_eve = codigo_eve
    notificacion.push_not = push_not
    notificacion.save()

    messages.success(request, "Notificación actualizada exitosamente.")
    return redirect('listadoNotificaciones')

# --------------------------------------DIRECCIONES--------------------------------------------------------

# Listado de Direcciones
def listadoDirecciones(request):
    direcciones = Direccion.objects.all()
    return render(request, "listadoDirecciones.html", {'direcciones': direcciones})

# Eliminar Dirección
def eliminarDireccion(request, id):
    direccionEliminar = Direccion.objects.get(codigo_dir=id)
    direccionEliminar.delete()
    messages.success(request, "Dirección eliminada exitosamente.")
    return redirect('listadoDirecciones')

# Formulario Nueva Dirección
def nuevaDireccion(request):
    return render(request, 'nuevaDireccion.html')

# Guardar Nueva Dirección
def guardarDireccion(request):
    nombre = request.POST["nombre_dir"]
    color = request.POST["color_dir"]
    Direccion.objects.create(
        nombre_dir=nombre,
        color_dir=color
    )
    messages.success(request, "Dirección registrada exitosamente.")
    return redirect('listadoDirecciones')


# Vista para editar dirección
def editarDireccion(request, id):
    direccionEditar = Direccion.objects.get(codigo_dir=id)
    return render(request, 'editarDireccion.html', {'direccionEditar': direccionEditar})

# Actualizar Dirección
def procesarActualizacionDireccion(request):
    codigo_dir = request.POST['codigo_dir']
    nombre = request.POST['nombre_dir']
    color = request.POST['color_dir']

    # Actualizar la dirección
    direccion = Direccion.objects.get(codigo_dir=codigo_dir)
    direccion.nombre_dir = nombre
    direccion.color_dir = color
    direccion.save()

    messages.success(request, "Dirección actualizada exitosamente.")
    return redirect('listadoDirecciones')

# --------------------------------------USUARIOS--------------------------------------------------------
# Listado de Usuarios
def listadoUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "listadoUsuarios.html", {'usuarios': usuarios})

# Eliminar Usuario
def eliminarUsuario(request, id):
    usuarioEliminar = Usuario.objects.get(codigo_usu=id)
    usuarioEliminar.delete()
    messages.success(request, "Usuario eliminado exitosamente.")
    return redirect('listadoUsuarios')

# Formulario Nuevo Usuario
def nuevoUsuario(request):
    return render(request, 'nuevoUsuario.html')

# Guardar Nuevo Usuario
def guardarUsuario(request):
    nombre = request.POST["nombre_usu"]
    email = request.POST["email_usu"]
    perfil = request.POST["perfil_usu"]
    estado = request.POST["estado_usu"]
    delegado = request.POST["es_delegado"]
    Usuario.objects.create(
        nombre_usu=nombre,
        email_usu=email,
        perfil_usu=perfil,
        estado_usu=estado,
        es_delegado=delegado
    )
    messages.success(request, "Usuario registrado exitosamente.")
    return redirect('listadoUsuarios')

# Vista para editar usuario
def editarUsuario(request, id):
    usuarioEditar = Usuario.objects.get(codigo_usu=id)
    return render(request, 'editarUsuario.html', {'usuarioEditar': usuarioEditar})

# Actualizar Usuario
def procesarActualizacionUsuario(request):
    codigo_usu = request.POST['codigo_usu']
    nombre = request.POST['nombre_usu']
    email = request.POST['email_usu']
    perfil = request.POST['perfil_usu']
    estado = request.POST['estado_usu']
    delegado = request.POST['es_delegado']

    usuario = Usuario.objects.get(codigo_usu=codigo_usu)
    usuario.nombre_usu = nombre
    usuario.email_usu = email
    usuario.perfil_usu = perfil
    usuario.estado_usu = estado
    usuario.es_delegado = delegado
    usuario.save()

    messages.success(request, "Usuario actualizado exitosamente.")
    return redirect('listadoUsuarios')


# --------------------------------------UNIDADES--------------------------------------------------------
# Listado de Unidades
def listadoUnidades(request):
    unidades = Unidad.objects.all()
    return render(request, "listadoUnidades.html", {'unidades': unidades})

# Eliminar Unidad
def eliminarUnidad(request, codigo):
    unidadEliminar = Unidad.objects.get(codigo_uni=codigo)
    unidadEliminar.delete()
    messages.success(request, "Unidad eliminada exitosamente.")
    return redirect('listadoUnidades')

# Formulario Nueva Unidad
def nuevaUnidad(request):
    return render(request, 'nuevaUnidad.html')

# Guardar Nueva Unidad
def guardarUnidad(request):
    nombre = request.POST["nombre_uni"]
    codigo_dir = request.POST["codigo_dir"]
    Unidad.objects.create(
        nombre_uni=nombre,
        codigo_dir=codigo_dir
    )
    messages.success(request, "Unidad registrada exitosamente.")
    return redirect('listadoUnidades')

# Vista para editar unidad
def editarUnidad(request, codigo):
    unidadEditar = Unidad.objects.get(codigo_uni=codigo)
    return render(request, 'editarUnidad.html', {'unidadEditar': unidadEditar})

# Actualizar Unidad
def procesarActualizacionUnidad(request):
    codigo_uni = request.POST['codigo_uni']
    nombre = request.POST['nombre_uni']
    codigo_dir = request.POST['codigo_dir']

    # Actualizar la unidad
    unidad = Unidad.objects.get(codigo_uni=codigo_uni)
    unidad.nombre_uni = nombre
    unidad.codigo_dir = codigo_dir
    unidad.save()

    messages.success(request, "Unidad actualizada exitosamente.")
    return redirect('listadoUnidades')


# --------------------------------------TIPOS--------------------------------------------------------
# Listado de Tipos
def listadoTipos(request):
    tipos = Tipo.objects.all()
    return render(request, "listadoTipos.html", {'tipos': tipos})

# Eliminar Tipo
def eliminarTipo(request, codigo):
    tipoEliminar = Tipo.objects.get(codigo_tip=codigo)
    tipoEliminar.delete()
    messages.success(request, "Tipo eliminado exitosamente.")
    return redirect('listadoTipos')

# Formulario Nuevo Tipo
def nuevoTipo(request):
    return render(request, 'nuevoTipo.html')

# Guardar Nuevo Tipo
def guardarTipo(request):
    nombre = request.POST["nombre_tip"]
    color = request.POST["color_tip"]
    Tipo.objects.create(
        nombre_tip=nombre,
        color_tip=color
    )
    messages.success(request, "Tipo registrado exitosamente.")
    return redirect('listadoTipos')

# Vista para editar tipo
def editarTipo(request, codigo):
    tipoEditar = Tipo.objects.get(codigo_tip=codigo)
    return render(request, 'editarTipo.html', {'tipoEditar': tipoEditar})

# Actualizar Tipo
# Vista para procesar la actualización de tipo
def procesarActualizacionTipo(request):
    codigo_tip = request.POST['codigo_tip']
    nombre = request.POST['nombre_tip']
    color = request.POST['color_tip']

    tipo = Tipo.objects.get(codigo_tip=codigo_tip)
    tipo.nombre_tip = nombre
    tipo.color_tip = color
    tipo.save()

    messages.success(request, "Tipo actualizado exitosamente.")
    return redirect('listadoTipos')


# --------------------------------------POA--------------------------------------------------------
# Listado de POA
def listadoPoa(request):
    poas = Poa.objects.all()
    return render(request, "listadoPoa.html", {'poas': poas})

# Eliminar POA
def eliminarPoa(request, codigo_poa):
    poaEliminar = Poa.objects.get(codigo_poa=codigo_poa)
    poaEliminar.delete()
    messages.success(request, "POA eliminado exitosamente.")
    return redirect('listadoPoa')

# Formulario Nuevo POA
def nuevoPoa(request):
    return render(request, 'nuevoPoa.html')

# Guardar Nuevo POA
def guardarPoa(request):
    anio = request.POST["anio_poa"]
    descripcion = request.POST["descripcion_poa"]
    codigo_dir = request.POST["codigo_dir"]
    
    Poa.objects.create(
        anio_poa=anio,
        descripcion_poa=descripcion,
        codigo_dir=codigo_dir
    )
    messages.success(request, "POA registrado exitosamente.")
    return redirect('listadoPoa')

# Vista para editar POA
def editarPoa(request, codigo_poa):
    poaEditar = Poa.objects.get(codigo_poa=codigo_poa)
    return render(request, 'editarPoa.html', {'poaEditar': poaEditar})

# Actualizar POA
def procesarActualizacionPoa(request):
    codigo_poa = request.POST['codigo_poa']
    anio = request.POST['anio_poa']
    descripcion = request.POST['descripcion_poa']
    codigo_dir = request.POST['codigo_dir']

    poa = Poa.objects.get(codigo_poa=codigo_poa)
    poa.anio_poa = anio
    poa.descripcion_poa = descripcion
    poa.codigo_dir = codigo_dir
    poa.save()

    messages.success(request, "POA actualizado exitosamente.")
    return redirect('listadoPoa')


# --------------------------------------OBJETIVO CANTONAL--------------------------------------------------------
# Listado de Objetivos Cantonales
def listadoObjetivosCantonal(request):
    objetivos = ObjetivoCantonal.objects.all()
    return render(request, "listadoObjetivosCantonal.html", {'objetivos': objetivos})

# Eliminar Objetivo Cantonal
def eliminarObjetivoCantonal(request, codigo_oc):
    objetivo = ObjetivoCantonal.objects.get(codigo_oc=codigo_oc)
    objetivo.delete()
    messages.success(request, "Objetivo Cantonal eliminado exitosamente.")
    return redirect('listadoObjetivosCantonal')

# Formulario Nuevo Objetivo Cantonal
def nuevoObjetivoCantonal(request):
    return render(request, 'nuevoObjetivoCantonal.html')

# Guardar Nuevo Objetivo Cantonal
def guardarObjetivoCantonal(request):
    descripcion = request.POST["descripcion_oc"]
    ObjetivoCantonal.objects.create(descripcion_oc=descripcion)
    messages.success(request, "Objetivo Cantonal registrado exitosamente.")
    return redirect('listadoObjetivosCantonal')

# Vista para editar Objetivo Cantonal
def editarObjetivoCantonal(request, codigo_oc):
    objetivoEditar = ObjetivoCantonal.objects.get(codigo_oc=codigo_oc)
    return render(request, 'editarObjetivoCantonal.html', {'objetivoEditar': objetivoEditar})

# Procesar Actualización Objetivo Cantonal
def procesarActualizacionObjetivoCantonal(request):
    codigo_oc = request.POST['codigo_oc']
    descripcion = request.POST['descripcion_oc']

    objetivo = ObjetivoCantonal.objects.get(codigo_oc=codigo_oc)
    objetivo.descripcion_oc = descripcion
    objetivo.save()

    messages.success(request, "Objetivo Cantonal actualizado exitosamente.")
    return redirect('listadoObjetivosCantonal')

# --------------------------------------OBJETIVO DESAROLLO--------------------------------------------------------
def listadoObjetivosDesarrollo(request):
    objetivos = ObjetivoDesarrollo.objects.all()
    return render(request, "listadoObjetivosDesarrollo.html", {'objetivos': objetivos})

def eliminarObjetivoDesarrollo(request, codigo_od):
    objetivo = ObjetivoDesarrollo.objects.get(codigo_od=codigo_od)
    objetivo.delete()
    messages.success(request, "Objetivo de Desarrollo eliminado exitosamente.")
    return redirect('listadoObjetivosDesarrollo')

def nuevoObjetivoDesarrollo(request):
    return render(request, 'nuevoObjetivoDesarrollo.html')

def guardarObjetivoDesarrollo(request):
    descripcion = request.POST["descripcion_od"]
    ObjetivoDesarrollo.objects.create(descripcion_od=descripcion)
    messages.success(request, "Objetivo de Desarrollo registrado exitosamente.")
    return redirect('listadoObjetivosDesarrollo')

def editarObjetivoDesarrollo(request, codigo_od):
    objetivoEditar = ObjetivoDesarrollo.objects.get(codigo_od=codigo_od)
    return render(request, 'editarObjetivoDesarrollo.html', {'objetivoEditar': objetivoEditar})

def procesarActualizacionObjetivoDesarrollo(request):
    codigo_od = request.POST['codigo_od']
    descripcion = request.POST['descripcion_od']
    
    objetivo = ObjetivoDesarrollo.objects.get(codigo_od=codigo_od)
    objetivo.descripcion_od = descripcion
    objetivo.save()

    messages.success(request, "Objetivo de Desarrollo actualizado exitosamente.")
    return redirect('listadoObjetivosDesarrollo')


# --------------------------------------OBJETIVO NACIONAL--------------------------------------------------------
def listadoObjetivosNacional(request):
    objetivos = ObjetivoNacional.objects.all()
    return render(request, "listadoObjetivosNacional.html", {'objetivos': objetivos})

def eliminarObjetivoNacional(request, codigo_on):
    objetivo = ObjetivoNacional.objects.get(codigo_on=codigo_on)
    objetivo.delete()
    messages.success(request, "Objetivo Nacional eliminado exitosamente.")
    return redirect('listadoObjetivosNacional')

def nuevoObjetivoNacional(request):
    return render(request, 'nuevoObjetivoNacional.html')

def guardarObjetivoNacional(request):
    descripcion = request.POST["descripcion_on"]
    ObjetivoNacional.objects.create(descripcion_on=descripcion)
    messages.success(request, "Objetivo Nacional registrado exitosamente.")
    return redirect('listadoObjetivosNacional')

def editarObjetivoNacional(request, codigo_on):
    objetivoEditar = ObjetivoNacional.objects.get(codigo_on=codigo_on)
    return render(request, 'editarObjetivoNacional.html', {'objetivoEditar': objetivoEditar})

def procesarActualizacionObjetivoNacional(request):
    codigo_on = request.POST['codigo_on']
    descripcion = request.POST['descripcion_on']
    
    objetivo = ObjetivoNacional.objects.get(codigo_on=codigo_on)
    objetivo.descripcion_on = descripcion
    objetivo.save()

    messages.success(request, "Objetivo Nacional actualizado exitosamente.")
    return redirect('listadoObjetivosNacional')


# --------------------------------------OBJETIVO PDYOT--------------------------------------------------------
def listadoObjetivosPdyot(request):
    objetivos = ObjetivoPdyot.objects.all()
    return render(request, "listadoObjetivosPdyot.html", {'objetivos': objetivos})

def eliminarObjetivoPdyot(request, codigo_op):
    objetivo = ObjetivoPdyot.objects.get(codigo_op=codigo_op)
    objetivo.delete()
    messages.success(request, "Objetivo Pdyot eliminado exitosamente.")
    return redirect('listadoObjetivosPdyot')

def nuevoObjetivoPdyot(request):
    return render(request, 'nuevoObjetivoPdyot.html')

def guardarObjetivoPdyot(request):
    descripcion = request.POST["descripcion_op"]
    ObjetivoPdyot.objects.create(descripcion_op=descripcion)
    messages.success(request, "Objetivo Pdyot registrado exitosamente.")
    return redirect('listadoObjetivosPdyot')

def editarObjetivoPdyot(request, codigo_op):
    objetivoEditar = ObjetivoPdyot.objects.get(codigo_op=codigo_op)
    return render(request, 'editarObjetivoPdyot.html', {'objetivoEditar': objetivoEditar})

def procesarActualizacionObjetivoPdyot(request):
    codigo_op = request.POST['codigo_op']
    descripcion = request.POST['descripcion_op']
    
    objetivo = ObjetivoPdyot.objects.get(codigo_op=codigo_op)
    objetivo.descripcion_op = descripcion
    objetivo.save()

    messages.success(request, "Objetivo Pdyot actualizado exitosamente.")
    return redirect('listadoObjetivosPdyot')


# --------------------------------------PARROQUIAS--------------------------------------------------------
# Listado de Parroquias
def listadoParroquias(request):
    parroquias = Parroquia.objects.all()
    return render(request, "listadoParroquias.html", {'parroquias': parroquias})

# Eliminar Parroquia
def eliminarParroquia(request, codigo_par):
    parroquiaEliminar = Parroquia.objects.get(codigo_par=codigo_par)
    parroquiaEliminar.delete()
    messages.success(request, "Parroquia eliminada exitosamente.")
    return redirect('listadoParroquias')

# Formulario Nueva Parroquia
def nuevaParroquia(request):
    return render(request, 'nuevaParroquia.html')

# Guardar Nueva Parroquia
def guardarParroquia(request):
    nombre = request.POST["nombre_par"]
    Parroquia.objects.create(nombre_par=nombre)
    messages.success(request, "Parroquia registrada exitosamente.")
    return redirect('listadoParroquias')

# Vista para editar parroquia
def editarParroquia(request, codigo_par):
    parroquiaEditar = Parroquia.objects.get(codigo_par=codigo_par)
    return render(request, 'editarParroquia.html', {'parroquiaEditar': parroquiaEditar})

# Actualizar Parroquia
def procesarActualizacionParroquia(request):
    codigo_par = request.POST['codigo_par']
    nombre = request.POST['nombre_par']

    parroquia = Parroquia.objects.get(codigo_par=codigo_par)
    parroquia.nombre_par = nombre
    parroquia.save()

    messages.success(request, "Parroquia actualizada exitosamente.")
    return redirect('listadoParroquias')

# --------------------------------------PRIORIDADES--------------------------------------------------------
# Listado de Prioridades
def listadoPrioridades(request):
    prioridades = Prioridad.objects.all()
    return render(request, "listadoPrioridades.html", {'prioridades': prioridades})

# Eliminar Prioridad
def eliminarPrioridad(request, id):
    prioridadEliminar = Prioridad.objects.get(codigo_pri=id)
    prioridadEliminar.delete()
    messages.success(request, "Prioridad eliminada exitosamente.")
    return redirect('listadoPrioridades')

# Formulario Nueva Prioridad
def nuevaPrioridad(request):
    return render(request, 'nuevaPrioridad.html')

# Guardar Nueva Prioridad
def guardarPrioridad(request):
    nombre = request.POST["nombre_pri"]
    Prioridad.objects.create(nombre_pri=nombre)
    messages.success(request, "Prioridad registrada exitosamente.")
    return redirect('listadoPrioridades')

# Vista para editar Prioridad
def editarPrioridad(request, id):
    prioridadEditar = Prioridad.objects.get(codigo_pri=id)
    return render(request, 'editarPrioridad.html', {'prioridadEditar': prioridadEditar})

# Actualizar Prioridad
def procesarActualizacionPrioridad(request):
    codigo_pri = request.POST['codigo_pri']
    nombre = request.POST['nombre_pri']

    prioridad = Prioridad.objects.get(codigo_pri=codigo_pri)
    prioridad.nombre_pri = nombre
    prioridad.save()

    messages.success(request, "Prioridad actualizada exitosamente.")
    return redirect('listadoPrioridades')


# --------------------------------------PROYECTOS--------------------------------------------------------
# Listado de Proyectos
def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "listadoProyectos.html", {'proyectos': proyectos})

# Eliminar Proyecto
def eliminarProyecto(request, codigo):
    proyectoEliminar = Proyecto.objects.get(codigo_pro=codigo)
    proyectoEliminar.delete()
    messages.success(request, "Proyecto eliminado exitosamente.")
    return redirect('listadoProyectos')

# Formulario Nuevo Proyecto
def nuevoProyecto(request):
    return render(request, 'nuevoProyecto.html')

# Guardar Nuevo Proyecto
def guardarProyecto(request):
    nombre = request.POST["nombre_pro"]
    descripcion = request.POST["descripcion_pro"]
    componentes = request.POST["componentes_pro"]
    total_financiamiento = request.POST["total_financiamiento_pro"]
    primer_cuatrimestre = request.POST["primer_cuatrimestre_pro"]
    segundo_cuatrimestre = request.POST["segundo_cuatrimestre_pro"]
    tercer_cuatrimestre = request.POST["tercer_cuatrimestre_pro"]

    Proyecto.objects.create(
        nombre_pro=nombre,
        descripcion_pro=descripcion,
        componentes_pro=componentes,
        total_financiamiento_pro=total_financiamiento,
        primer_cuatrimestre_pro=primer_cuatrimestre,
        segundo_cuatrimestre_pro=segundo_cuatrimestre,
        tercer_cuatrimestre_pro=tercer_cuatrimestre
    )
    messages.success(request, "Proyecto registrado exitosamente.")
    return redirect('listadoProyectos')

# Vista para editar proyecto
def editarProyecto(request, codigo):
    proyectoEditar = Proyecto.objects.get(codigo_pro=codigo)
    return render(request, 'editarProyecto.html', {'proyectoEditar': proyectoEditar})

# Actualizar Proyecto
def procesarActualizacionProyecto(request):
    codigo_pro = request.POST['codigo_pro']
    nombre = request.POST['nombre_pro']
    descripcion = request.POST['descripcion_pro']
    componentes = request.POST['componentes_pro']
    total_financiamiento = request.POST['total_financiamiento_pro']
    primer_cuatrimestre = request.POST['primer_cuatrimestre_pro']
    segundo_cuatrimestre = request.POST['segundo_cuatrimestre_pro']
    tercer_cuatrimestre = request.POST['tercer_cuatrimestre_pro']

    proyecto = Proyecto.objects.get(codigo_pro=codigo_pro)
    proyecto.nombre_pro = nombre
    proyecto.descripcion_pro = descripcion
    proyecto.componentes_pro = componentes
    proyecto.total_financiamiento_pro = total_financiamiento
    proyecto.primer_cuatrimestre_pro = primer_cuatrimestre
    proyecto.segundo_cuatrimestre_pro = segundo_cuatrimestre
    proyecto.tercer_cuatrimestre_pro = tercer_cuatrimestre
    proyecto.save()

    messages.success(request, "Proyecto actualizado exitosamente.")
    return redirect('listadoProyectos')


# --------------------------------------EVENTOS--------------------------------------------------------
# Listado de Eventos
def listadoEventos(request):
    eventos = Evento.objects.all()
    proyectos = Proyecto.objects.all()
    tipos = Tipo.objects.all()
    prioridades = Prioridad.objects.all()
    parroquias = Parroquia.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, "listadoEventos.html", {
        'eventos': eventos,
        'proyectos': proyectos,
        'tipos': tipos,
        'prioridades': prioridades,
        'parroquias': parroquias,
        'usuarios': usuarios
    })

# Eliminar Evento
def eliminarEvento(request, codigo_eve):
    eventoEliminar = Evento.objects.get(codigo_eve=codigo_eve)
    eventoEliminar.delete()
    messages.success(request, "Evento eliminado exitosamente.")
    return redirect('listadoEventos')

# Formulario Nuevo Evento
def nuevoEvento(request):
    proyectos = Proyecto.objects.all()
    tipos = Tipo.objects.all()
    prioridades = Prioridad.objects.all()
    parroquias = Parroquia.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'nuevoEvento.html', {
        'proyectos': proyectos,
        'tipos': tipos,
        'prioridades': prioridades,
        'parroquias': parroquias,
        'usuarios': usuarios
    })

# Guardar Nuevo Evento
def guardarEvento(request):
    if request.method == 'POST':
        codigo_pro = request.POST['codigo_pro']
        codigo_tip = request.POST['codigo_tip']
        codigo_pri = request.POST['codigo_pri']
        codigo_par = request.POST['codigo_par']
        codigo_usu = request.POST['codigo_usu']
        estado_eve = request.POST['estado_eve']
        actividad_eve = request.POST['actividad_eve']
        fecha_eve = request.POST['fecha_eve']
        numero_participantes_eve = request.POST['numero_participantes_eve']
        duracion_minutos_eve = request.POST['duracion_minutos_eve']
        lugar_eve = request.POST['lugar_eve']

        proyecto = Proyecto.objects.get(codigo_pro=codigo_pro)
        tipo = Tipo.objects.get(codigo_tip=codigo_tip)
        prioridad = Prioridad.objects.get(codigo_pri=codigo_pri)
        parroquia = Parroquia.objects.get(codigo_par=codigo_par)
        usuario = Usuario.objects.get(codigo_usu=codigo_usu)

        Evento.objects.create(
            codigo_pro=proyecto,
            codigo_tip=tipo,
            codigo_pri=prioridad,
            codigo_par=parroquia,
            codigo_usu=usuario,
            estado_eve=estado_eve,
            actividad_eve=actividad_eve,
            fecha_eve=fecha_eve,
            numero_participantes_eve=numero_participantes_eve,
            duracion_minutos_eve=duracion_minutos_eve,
            lugar_eve=lugar_eve
        )
        messages.success(request, "Evento registrado exitosamente.")
        return redirect('listadoEventos')

# Vista para editar evento
def editarEvento(request, codigo_eve):
    eventoEditar = Evento.objects.get(codigo_eve=codigo_eve)
    proyectos = Proyecto.objects.all()
    tipos = Tipo.objects.all()
    prioridades = Prioridad.objects.all()
    parroquias = Parroquia.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'editarEvento.html', {
        'eventoEditar': eventoEditar,
        'proyectos': proyectos,
        'tipos': tipos,
        'prioridades': prioridades,
        'parroquias': parroquias,
        'usuarios': usuarios
    })

# Actualizar Evento
def procesarActualizacionEvento(request):
    if request.method == 'POST':
        codigo_eve = request.POST['codigo_eve']
        codigo_pro = request.POST['codigo_pro']
        codigo_tip = request.POST['codigo_tip']
        codigo_pri = request.POST['codigo_pri']
        codigo_par = request.POST['codigo_par']
        codigo_usu = request.POST['codigo_usu']
        estado_eve = request.POST['estado_eve']
        actividad_eve = request.POST['actividad_eve']
        fecha_eve = request.POST['fecha_eve']
        numero_participantes_eve = request.POST['numero_participantes_eve']
        duracion_minutos_eve = request.POST['duracion_minutos_eve']
        lugar_eve = request.POST['lugar_eve']

        proyecto = Proyecto.objects.get(codigo_pro=codigo_pro)
        tipo = Tipo.objects.get(codigo_tip=codigo_tip)
        prioridad = Prioridad.objects.get(codigo_pri=codigo_pri)
        parroquia = Parroquia.objects.get(codigo_par=codigo_par)
        usuario = Usuario.objects.get(codigo_usu=codigo_usu)

        evento = Evento.objects.get(codigo_eve=codigo_eve)
        evento.codigo_pro = proyecto
        evento.codigo_tip = tipo
        evento.codigo_pri = prioridad
        evento.codigo_par = parroquia
        evento.codigo_usu = usuario
        evento.estado_eve = estado_eve
        evento.actividad_eve = actividad_eve
        evento.fecha_eve = fecha_eve
        evento.numero_participantes_eve = numero_participantes_eve
        evento.duracion_minutos_eve = duracion_minutos_eve
        evento.lugar_eve = lugar_eve
        evento.save()

        messages.success(request, "Evento actualizado exitosamente.")
        return redirect('listadoEventos')



# --------------------------------------VOCATIVOS--------------------------------------------------------
# Listado de Vocativos
def listadoVocativos(request):
    vocativos = Vocativo.objects.all()
    eventos = Evento.objects.all()
    return render(request, "listadoVocativos.html", {'vocativos': vocativos, 'eventos': eventos})

# Eliminar Vocativo
def eliminarVocativo(request, codigo_voc):
    vocativoEliminar = Vocativo.objects.get(codigo_voc=codigo_voc)
    vocativoEliminar.delete()
    messages.success(request, "Vocativo eliminado exitosamente.")
    return redirect('listadoVocativos')

# Formulario Nuevo Vocativo
def nuevoVocativo(request):
    eventos = Evento.objects.all()
    return render(request, 'nuevoVocativo.html', {'eventos': eventos})

# Guardar Nuevo Vocativo
def guardarVocativo(request):
    apellido = request.POST["apellido_voc"]
    nombre = request.POST["nombre_voc"]
    cargo = request.POST["cargo_voc"]
    telefono = request.POST["telefono_voc"]
    evento_id = request.POST["codigo_eve"]
    evento = Evento.objects.get(codigo_eve=evento_id)
    Vocativo.objects.create(
        apellido_voc=apellido,
        nombre_voc=nombre,
        cargo_voc=cargo,
        telefono_voc=telefono,
        codigo_eve=evento
    )
    messages.success(request, "Vocativo registrado exitosamente.")
    return redirect('listadoVocativos')

# Vista para editar vocativo
def editarVocativo(request, codigo_voc):
    vocativoEditar = Vocativo.objects.get(codigo_voc=codigo_voc)
    eventos = Evento.objects.all()
    return render(request, 'editarVocativo.html', {'vocativoEditar': vocativoEditar, 'eventos': eventos})

# Actualizar Vocativo
def procesarActualizacionVocativo(request):
    codigo_voc = request.POST['codigo_voc']
    apellido = request.POST['apellido_voc']
    nombre = request.POST['nombre_voc']
    cargo = request.POST['cargo_voc']
    telefono = request.POST['telefono_voc']
    codigo_eve = request.POST['codigo_eve']

    evento = Evento.objects.get(codigo_eve=codigo_eve)
    
    vocativo = Vocativo.objects.get(codigo_voc=codigo_voc)
    vocativo.apellido_voc = apellido
    vocativo.nombre_voc = nombre
    vocativo.cargo_voc = cargo
    vocativo.telefono_voc = telefono
    vocativo.codigo_eve = evento
    vocativo.save()

    messages.success(request, "Vocativo actualizado exitosamente.")
    return redirect('listadoVocativos')


# --------------------------------------DELEGADOS--------------------------------------------------------
# Listado de Delegados
def listadoDelegados(request):
    delegados = Delegado.objects.all()
    eventos = Evento.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, "listadoDelegados.html", {'delegados': delegados, 'eventos': eventos, 'usuarios': usuarios})

# Eliminar Delegado
def eliminarDelegado(request, id):
    delegadoEliminar = Delegado.objects.get(codigo_del=id)
    delegadoEliminar.delete()
    messages.success(request, "Delegado eliminado exitosamente.")
    return redirect('listadoDelegados')

# Formulario Nuevo Delegado
def nuevoDelegado(request):
    eventos = Evento.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'nuevoDelegado.html', {'eventos': eventos, 'usuarios': usuarios})

# Guardar Nuevo Delegado
def guardarDelegado(request):
    codigo_eve = request.POST["codigo_eve"]
    codigo_usu = request.POST["codigo_usu"]
    
    evento = Evento.objects.get(codigo_eve=codigo_eve)
    usuario = Usuario.objects.get(codigo_usu=codigo_usu)
    
    Delegado.objects.create(
        codigo_eve=evento,
        codigo_usu=usuario
    )
    messages.success(request, "Delegado registrado exitosamente.")
    return redirect('listadoDelegados')

# Vista para editar delegado
def editarDelegado(request, id):
    delegadoEditar = Delegado.objects.get(codigo_del=id)
    eventos = Evento.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'editarDelegado.html', {'delegadoEditar': delegadoEditar, 'eventos': eventos, 'usuarios': usuarios})

# Actualizar Delegado
def procesarActualizacionDelegado(request):
    codigo_del = request.POST['codigo_del']
    codigo_eve = request.POST['codigo_eve']
    codigo_usu = request.POST['codigo_usu']

    evento = Evento.objects.get(codigo_eve=codigo_eve)
    usuario = Usuario.objects.get(codigo_usu=codigo_usu)
    
    delegado = Delegado.objects.get(codigo_del=codigo_del)
    delegado.codigo_eve = evento
    delegado.codigo_usu = usuario
    delegado.save()

    messages.success(request, "Delegado actualizado exitosamente.")
    return redirect('listadoDelegados')