# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# LISTO
class Anio(models.Model):
    codigo_ani = models.AutoField(primary_key=True)
    nombre_ani = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anio'

# LISTO
class AyudaMemoria(models.Model):
    codigo_am = models.BigAutoField(primary_key=True)
    inversion_proyecto_am = models.FloatField(blank=True, null=True)
    inversion_global_am = models.FloatField(blank=True, null=True)
    beneficiarios_am = models.CharField(max_length=500, blank=True, null=True)
    descripcion_am = models.TextField(blank=True, null=True)
    lugar_am = models.CharField(max_length=500, blank=True, null=True)
    codigo_eve = models.ForeignKey('Evento', models.DO_NOTHING, db_column='codigo_eve', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ayuda_memoria'


class Delegado(models.Model):
    codigo_del = models.BigAutoField(primary_key=True)
    codigo_eve = models.ForeignKey('Evento', models.DO_NOTHING, db_column='codigo_eve', blank=True, null=True)
    codigo_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delegado'

# LISTO
class Direccion(models.Model):
    codigo_dir = models.BigAutoField(primary_key=True)
    nombre_dir = models.CharField(max_length=100, blank=True, null=True)
    color_dir = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'

# LISTO
class Evento(models.Model):
    codigo_eve = models.BigAutoField(primary_key=True)
    codigo_pro = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='codigo_pro', blank=True, null=True)
    codigo_tip = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='codigo_tip', blank=True, null=True)
    codigo_pri = models.ForeignKey('Prioridad', models.DO_NOTHING, db_column='codigo_pri', blank=True, null=True)
    codigo_par = models.ForeignKey('Parroquia', models.DO_NOTHING, db_column='codigo_par', blank=True, null=True)
    codigo_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo_usu', blank=True, null=True)
    estado_eve = models.CharField(max_length=100, blank=True, null=True)
    motivo_rechazo_eve = models.CharField(max_length=2500, blank=True, null=True)
    actividad_eve = models.TextField(blank=True, null=True)
    fecha_eve = models.DateTimeField(blank=True, null=True)
    numero_participantes_eve = models.IntegerField(blank=True, null=True)
    duracion_minutos_eve = models.IntegerField(blank=True, null=True)
    lugar_eve = models.CharField(max_length=500, blank=True, null=True)
    latitud_eve = models.FloatField(blank=True, null=True)
    longitud_eve = models.FloatField(blank=True, null=True)
    ubicacion_eve = models.CharField(max_length=2500, blank=True, null=True)
    codigo_dir = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='codigo_dir', blank=True, null=True)
    antecedentes_eve = models.TextField(blank=True, null=True)
    vocativos_eve = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'

# LISTO
class Modalidad(models.Model):
    codigo_mod = models.BigAutoField(primary_key=True)
    nombre_mod = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'

# LISTO
class Notificacion(models.Model):
    codigo_not = models.BigAutoField(primary_key=True)
    mensaje_not = models.CharField(max_length=5000, blank=True, null=True)
    emisor_not = models.BigIntegerField(blank=True, null=True)
    receptor_not = models.BigIntegerField(blank=True, null=True)
    estado_not = models.IntegerField(blank=True, null=True)
    fecha_not = models.DateTimeField(blank=True, null=True)
    codigo_eve = models.BigIntegerField(blank=True, null=True)
    push_not = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'

# LISTO
class ObjetivoCantonal(models.Model):
    codigo_oc = models.BigAutoField(primary_key=True)
    descripcion_oc = models.CharField(max_length=3500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_cantonal'

# LISTO
class ObjetivoDesarrollo(models.Model):
    codigo_od = models.BigAutoField(primary_key=True)
    descripcion_od = models.CharField(max_length=3500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_desarrollo'

# LISTO
class ObjetivoNacional(models.Model):
    codigo_on = models.BigAutoField(primary_key=True)
    descripcion_on = models.CharField(max_length=3500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_nacional'

# LISTO
class ObjetivoPdyot(models.Model):
    codigo_op = models.BigAutoField(primary_key=True)
    descripcion_op = models.CharField(max_length=3500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_pdyot'

# LISTO
class Parroquia(models.Model):
    codigo_par = models.BigAutoField(primary_key=True)
    nombre_par = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquia'

# LISTO
class Poa(models.Model):
    codigo_poa = models.BigAutoField(primary_key=True)
    anio_poa = models.CharField(max_length=100, blank=True, null=True)
    descripcion_poa = models.CharField(max_length=100, blank=True, null=True)
    codigo_dir = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poa'

# LISTO
class Prioridad(models.Model):
    codigo_pri = models.BigAutoField(primary_key=True)
    nombre_pri = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prioridad'

# LISTO
class Proyecto(models.Model):
    codigo_pro = models.BigAutoField(primary_key=True)
    codigo_par = models.ForeignKey(Parroquia, models.DO_NOTHING, db_column='codigo_par', blank=True, null=True)
    codigo_od = models.ForeignKey(ObjetivoDesarrollo, models.DO_NOTHING, db_column='codigo_od', blank=True, null=True)
    codigo_on = models.ForeignKey(ObjetivoNacional, models.DO_NOTHING, db_column='codigo_on', blank=True, null=True)
    codigo_oc = models.ForeignKey(ObjetivoCantonal, models.DO_NOTHING, db_column='codigo_oc', blank=True, null=True)
    codigo_op = models.ForeignKey(ObjetivoPdyot, models.DO_NOTHING, db_column='codigo_op', blank=True, null=True)
    codigo_poa = models.ForeignKey(Poa, models.DO_NOTHING, db_column='codigo_poa', blank=True, null=True)
    codigo_mod = models.ForeignKey(Modalidad, models.DO_NOTHING, db_column='codigo_mod', blank=True, null=True)
    
    nombre_pro = models.CharField(max_length=5000, blank=True, null=True)
    descripcion_pro = models.CharField(max_length=5000, blank=True, null=True)
    componentes_pro = models.CharField(max_length=5000, blank=True, null=True)
    total_financiamiento_pro = models.FloatField(blank=True, null=True)
    primer_cuatrimestre_pro = models.IntegerField(blank=True, null=True)
    segundo_cuatrimestre_pro = models.IntegerField(blank=True, null=True)
    tercer_cuatrimestre_pro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto'


# LISTO
class Tipo(models.Model):
    codigo_tip = models.BigAutoField(primary_key=True)
    nombre_tip = models.CharField(max_length=500, blank=True, null=True)
    color_tip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'

# LISTO
class Unidad(models.Model):
    codigo_uni = models.BigAutoField(primary_key=True)
    nombre_uni = models.CharField(max_length=100, blank=True, null=True)
    codigo_dir = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad'

# LISTO
class Usuario(models.Model):
    codigo_usu = models.BigAutoField(primary_key=True)
    nombre_usu = models.CharField(max_length=100, blank=True, null=True)
    email_usu = models.CharField(max_length=100, blank=True, null=True)
    password_usu = models.CharField(max_length=100, blank=True, null=True)
    codigo_uni = models.BigIntegerField(blank=True, null=True)
    perfil_usu = models.CharField(max_length=100, blank=True, null=True)
    estado_usu = models.IntegerField(blank=True, null=True)
    es_delegado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

# LISTO
class Vocativo(models.Model):
    codigo_voc = models.BigAutoField(primary_key=True)
    apellido_voc = models.CharField(max_length=500, blank=True, null=True)
    nombre_voc = models.CharField(max_length=500, blank=True, null=True)
    cargo_voc = models.CharField(max_length=500, blank=True, null=True)
    telefono_voc = models.CharField(max_length=15, blank=True, null=True)
    codigo_eve = models.ForeignKey(Evento, models.DO_NOTHING, db_column='codigo_eve', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vocativo'
