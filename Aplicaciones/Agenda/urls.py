#configurando redireccionanmiento
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    #URL AÑO
    #-----------------------------------------AÑOS--------------------------------------------------
    path('listadoAnios/', views.listadoAnios, name='listadoAnios'),
    path('eliminarAnio/<id>', views.eliminarAnio, name='eliminarAnio'),
    path('nuevoAnio/', views.nuevoAnio, name='nuevoAnio'),
    path('guardarAnio/', views.guardarAnio, name='guardarAnio'),
    path('editarAnio/<id>', views.editarAnio, name='editarAnio'),
    path('procesarActualizacionAnio/', views.procesarActualizacionAnio, name='procesarActualizacionAnio'),

    #-----------------------------------------AYUDA MEMORIA--------------------------------------------------
    path('listadoAyudaMemoria/', views.listadoAyudaMemoria, name='listadoAyudaMemoria'),
    path('eliminarAyudaMemoria/<id>', views.eliminarAyudaMemoria, name='eliminarAyudaMemoria'),
    path('nuevaAyudaMemoria/', views.nuevaAyudaMemoria, name='nuevaAyudaMemoria'),
    path('guardarAyudaMemoria/', views.guardarAyudaMemoria, name='guardarAyudaMemoria'),
    path('editarAyudaMemoria/<id>', views.editarAyudaMemoria, name='editarAyudaMemoria'),
    path('procesarActualizacionAyudaMemoria/', views.procesarActualizacionAyudaMemoria, name='procesarActualizacionAyudaMemoria'),

    #-----------------------------------------MODALIDAD--------------------------------------------------
    path('listadoModalidades/', views.listadoModalidades, name='listadoModalidades'),
    path('eliminarModalidad/<codigo>', views.eliminarModalidad, name='eliminarModalidad'),
    path('nuevoModalidad/', views.nuevaModalidad, name='nuevoModalidad'),
    path('guardarModalidad/', views.guardarModalidad, name='guardarModalidad'),
    path('editarModalidad/<codigo>', views.editarModalidad, name='editarModalidad'),
    path('procesarActualizacionModalidad/', views.procesarActualizacionModalidad, name='procesarActualizacionModalidad'),

    #-----------------------------------------NOTIFICACIONES--------------------------------------------------
    path('listadoNotificaciones/', views.listadoNotificaciones, name='listadoNotificaciones'),
    path('eliminarNotificacion/<id>', views.eliminarNotificacion, name='eliminarNotificacion'),
    path('nuevaNotificacion/', views.nuevaNotificacion, name='nuevaNotificacion'),
    path('guardarNotificacion/', views.guardarNotificacion, name='guardarNotificacion'),
    path('editarNotificacion/<id>', views.editarNotificacion, name='editarNotificacion'),
    path('procesarActualizacionNotificacion/', views.procesarActualizacionNotificacion, name='procesarActualizacionNotificacion'),

    #-----------------------------------------DIRECCIONES--------------------------------------------------
    path('listadoDirecciones/', views.listadoDirecciones, name='listadoDirecciones'),
    path('eliminarDireccion/<id>', views.eliminarDireccion, name='eliminarDireccion'),
    path('nuevaDireccion/', views.nuevaDireccion, name='nuevaDireccion'),
    path('guardarDireccion/', views.guardarDireccion, name='guardarDireccion'),
    path('editarDireccion/<id>', views.editarDireccion, name='editarDireccion'),
    path('procesarActualizacionDireccion/', views.procesarActualizacionDireccion, name='procesarActualizacionDireccion'),

    #-----------------------------------------USUARIOS--------------------------------------------------
    path('listadoUsuarios/', views.listadoUsuarios, name='listadoUsuarios'),
    path('eliminarUsuario/<id>', views.eliminarUsuario, name='eliminarUsuario'),
    path('nuevoUsuario/', views.nuevoUsuario, name='nuevoUsuario'),
    path('guardarUsuario/', views.guardarUsuario, name='guardarUsuario'),
    path('editarUsuario/<id>', views.editarUsuario, name='editarUsuario'),
    path('procesarActualizacionUsuario/', views.procesarActualizacionUsuario, name='procesarActualizacionUsuario'),

    #-----------------------------------------UNIDADES--------------------------------------------------
    path('listadoUnidades/', views.listadoUnidades, name='listadoUnidades'),
    path('eliminarUnidad/<codigo>', views.eliminarUnidad, name='eliminarUnidad'),
    path('nuevaUnidad/', views.nuevaUnidad, name='nuevaUnidad'),
    path('guardarUnidad/', views.guardarUnidad, name='guardarUnidad'),
    path('editarUnidad/<codigo>', views.editarUnidad, name='editarUnidad'),
    path('procesarActualizacionUnidad/', views.procesarActualizacionUnidad, name='procesarActualizacionUnidad'),

    #-----------------------------------------TIPOS--------------------------------------------------
    path('listadoTipos/', views.listadoTipos, name='listadoTipos'),
    path('eliminarTipo/<codigo>', views.eliminarTipo, name='eliminarTipo'),
    path('nuevoTipo/', views.nuevoTipo, name='nuevoTipo'),
    path('guardarTipo/', views.guardarTipo, name='guardarTipo'),
    path('editarTipo/<codigo>', views.editarTipo, name='editarTipo'),
    path('procesarActualizacionTipo/', views.procesarActualizacionTipo, name='procesarActualizacionTipo'),

    #-----------------------------------------POA--------------------------------------------------
    path('listadoPoa/', views.listadoPoa, name='listadoPoa'),
    path('eliminarPoa/<codigo_poa>', views.eliminarPoa, name='eliminarPoa'),
    path('nuevoPoa/', views.nuevoPoa, name='nuevoPoa'),
    path('guardarPoa/', views.guardarPoa, name='guardarPoa'),
    path('editarPoa/<codigo_poa>', views.editarPoa, name='editarPoa'),
    path('procesarActualizacionPoa/', views.procesarActualizacionPoa, name='procesarActualizacionPoa'),

    # -------------------------------------- OBJETIVO CANTONAL ------------------------------------------
    path('listadoObjetivosCantonal/', views.listadoObjetivosCantonal, name='listadoObjetivosCantonal'),
    path('eliminarObjetivoCantonal/<codigo_oc>', views.eliminarObjetivoCantonal, name='eliminarObjetivoCantonal'),
    path('nuevoObjetivoCantonal/', views.nuevoObjetivoCantonal, name='nuevoObjetivoCantonal'),
    path('guardarObjetivoCantonal/', views.guardarObjetivoCantonal, name='guardarObjetivoCantonal'),
    path('editarObjetivoCantonal/<codigo_oc>', views.editarObjetivoCantonal, name='editarObjetivoCantonal'),
    path('procesarActualizacionObjetivoCantonal/', views.procesarActualizacionObjetivoCantonal, name='procesarActualizacionObjetivoCantonal'),

    # -------------------------------------- OBJETIVO DESARROLLO --------------------------------------
    path('listadoObjetivosDesarrollo/', views.listadoObjetivosDesarrollo, name='listadoObjetivosDesarrollo'),
    path('eliminarObjetivoDesarrollo/<codigo_od>', views.eliminarObjetivoDesarrollo, name='eliminarObjetivoDesarrollo'),
    path('nuevoObjetivoDesarrollo/', views.nuevoObjetivoDesarrollo, name='nuevoObjetivoDesarrollo'),
    path('guardarObjetivoDesarrollo/', views.guardarObjetivoDesarrollo, name='guardarObjetivoDesarrollo'),
    path('editarObjetivoDesarrollo/<codigo_od>', views.editarObjetivoDesarrollo, name='editarObjetivoDesarrollo'),
    path('procesarActualizacionObjetivoDesarrollo/', views.procesarActualizacionObjetivoDesarrollo, name='procesarActualizacionObjetivoDesarrollo'),

    # -------------------------------------- OBJETIVO NACIONAL ---------------------------------------
    path('listadoObjetivosNacional/', views.listadoObjetivosNacional, name='listadoObjetivosNacional'),
    path('eliminarObjetivoNacional/<codigo_on>', views.eliminarObjetivoNacional, name='eliminarObjetivoNacional'),
    path('nuevoObjetivoNacional/', views.nuevoObjetivoNacional, name='nuevoObjetivoNacional'),
    path('guardarObjetivoNacional/', views.guardarObjetivoNacional, name='guardarObjetivoNacional'),
    path('editarObjetivoNacional/<codigo_on>', views.editarObjetivoNacional, name='editarObjetivoNacional'),
    path('procesarActualizacionObjetivoNacional/', views.procesarActualizacionObjetivoNacional, name='procesarActualizacionObjetivoNacional'),

    # -------------------------------------- OBJETIVO PDYOT ------------------------------------------
    path('listadoObjetivosPdyot/', views.listadoObjetivosPdyot, name='listadoObjetivosPdyot'),
    path('eliminarObjetivoPdyot/<codigo_op>', views.eliminarObjetivoPdyot, name='eliminarObjetivoPdyot'),
    path('nuevoObjetivoPdyot/', views.nuevoObjetivoPdyot, name='nuevoObjetivoPdyot'),
    path('guardarObjetivoPdyot/', views.guardarObjetivoPdyot, name='guardarObjetivoPdyot'),
    path('editarObjetivoPdyot/<codigo_op>', views.editarObjetivoPdyot, name='editarObjetivoPdyot'),
    path('procesarActualizacionObjetivoPdyot/', views.procesarActualizacionObjetivoPdyot, name='procesarActualizacionObjetivoPdyot'),

    #-----------------------------------------PARROQUIAS--------------------------------------------------
    path('listadoParroquias/', views.listadoParroquias, name='listadoParroquias'),
    path('eliminarParroquia/<codigo_par>', views.eliminarParroquia, name='eliminarParroquia'),
    path('nuevaParroquia/', views.nuevaParroquia, name='nuevaParroquia'),
    path('guardarParroquia/', views.guardarParroquia, name='guardarParroquia'),
    path('editarParroquia/<codigo_par>', views.editarParroquia, name='editarParroquia'),
    path('procesarActualizacionParroquia/', views.procesarActualizacionParroquia, name='procesarActualizacionParroquia'),

    #-----------------------------------------PRIORIDADES--------------------------------------------------
    path('listadoPrioridades/', views.listadoPrioridades, name='listadoPrioridades'),
    path('eliminarPrioridad/<id>', views.eliminarPrioridad, name='eliminarPrioridad'),
    path('nuevaPrioridad/', views.nuevaPrioridad, name='nuevaPrioridad'),
    path('guardarPrioridad/', views.guardarPrioridad, name='guardarPrioridad'),
    path('editarPrioridad/<id>', views.editarPrioridad, name='editarPrioridad'),
    path('procesarActualizacionPrioridad/', views.procesarActualizacionPrioridad, name='procesarActualizacionPrioridad'),

    #-----------------------------------------PROYECTOS--------------------------------------------------
    path('listadoProyectos/', views.listadoProyectos, name='listadoProyectos'),
    path('eliminarProyecto/<codigo>', views.eliminarProyecto, name='eliminarProyecto'),
    path('nuevoProyecto/', views.nuevoProyecto, name='nuevoProyecto'),
    path('guardarProyecto/', views.guardarProyecto, name='guardarProyecto'),
    path('editarProyecto/<codigo>', views.editarProyecto, name='editarProyecto'),
    path('procesarActualizacionProyecto/', views.procesarActualizacionProyecto, name='procesarActualizacionProyecto'),

    #-----------------------------------------EVENTOS--------------------------------------------------
    path('listadoEventos/', views.listadoEventos, name='listadoEventos'),
    path('eliminarEvento/<codigo_eve>', views.eliminarEvento, name='eliminarEvento'),
    path('nuevoEvento/', views.nuevoEvento, name='nuevoEvento'),
    path('guardarEvento/', views.guardarEvento, name='guardarEvento'),
    path('editarEvento/<codigo_eve>', views.editarEvento, name='editarEvento'),
    path('procesarActualizacionEvento/', views.procesarActualizacionEvento, name='procesarActualizacionEvento'),

    #-----------------------------------------VOCATIVOS--------------------------------------------------
    path('listadoVocativos/', views.listadoVocativos, name='listadoVocativos'),
    path('eliminarVocativo/<codigo_voc>', views.eliminarVocativo, name='eliminarVocativo'),
    path('nuevoVocativo/', views.nuevoVocativo, name='nuevoVocativo'),
    path('guardarVocativo/', views.guardarVocativo, name='guardarVocativo'),
    path('editarVocativo/<codigo_voc>', views.editarVocativo, name='editarVocativo'),
    path('procesarActualizacionVocativo/', views.procesarActualizacionVocativo, name='procesarActualizacionVocativo'),

    #-----------------------------------------DELEGADOS--------------------------------------------------
    path('listadoDelegados/', views.listadoDelegados, name='listadoDelegados'),
    path('eliminarDelegado/<id>', views.eliminarDelegado, name='eliminarDelegado'),
    path('nuevoDelegado/', views.nuevoDelegado, name='nuevoDelegado'),
    path('guardarDelegado/', views.guardarDelegado, name='guardarDelegado'),
    path('editarDelegado/<id>', views.editarDelegado, name='editarDelegado'),
    path('procesarActualizacionDelegado/', views.procesarActualizacionDelegado, name='procesarActualizacionDelegado'),
]