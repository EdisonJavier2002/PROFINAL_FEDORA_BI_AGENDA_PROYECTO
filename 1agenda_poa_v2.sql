-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-02-2025 a las 18:12:21
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda_poa_v2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anio`
--

CREATE TABLE `anio` (
  `codigo_ani` int(11) NOT NULL,
  `nombre_ani` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `anio`
--

INSERT INTO `anio` (`codigo_ani`, `nombre_ani`) VALUES
(1, 2020);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ayuda_memoria`
--

CREATE TABLE `ayuda_memoria` (
  `codigo_am` bigint(11) NOT NULL,
  `inversion_proyecto_am` float DEFAULT NULL,
  `inversion_global_am` float DEFAULT NULL,
  `beneficiarios_am` varchar(500) DEFAULT NULL,
  `descripcion_am` text DEFAULT NULL,
  `lugar_am` varchar(500) DEFAULT NULL,
  `codigo_eve` bigint(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `delegado`
--

CREATE TABLE `delegado` (
  `codigo_del` bigint(11) NOT NULL,
  `codigo_eve` bigint(11) DEFAULT NULL,
  `codigo_usu` bigint(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direccion`
--

CREATE TABLE `direccion` (
  `codigo_dir` bigint(11) NOT NULL,
  `nombre_dir` varchar(100) DEFAULT NULL,
  `color_dir` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `direccion`
--

INSERT INTO `direccion` (`codigo_dir`, `nombre_dir`, `color_dir`) VALUES
(1, 'Administrativa', NULL),
(2, 'Obras Públicas', NULL),
(3, 'Alcaldía', NULL),
(4, 'Movilidad', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evento`
--

CREATE TABLE `evento` (
  `codigo_eve` bigint(11) NOT NULL,
  `codigo_pro` bigint(11) DEFAULT NULL,
  `codigo_tip` bigint(11) DEFAULT NULL,
  `codigo_pri` bigint(11) DEFAULT NULL,
  `codigo_par` bigint(11) DEFAULT NULL,
  `codigo_usu` bigint(11) DEFAULT NULL,
  `estado_eve` varchar(100) DEFAULT 'Enviado',
  `motivo_rechazo_eve` varchar(2500) DEFAULT NULL,
  `actividad_eve` text DEFAULT NULL,
  `fecha_eve` datetime DEFAULT NULL,
  `numero_participantes_eve` int(11) DEFAULT NULL,
  `duracion_minutos_eve` int(11) DEFAULT NULL,
  `lugar_eve` varchar(500) DEFAULT NULL,
  `latitud_eve` float DEFAULT NULL,
  `longitud_eve` float DEFAULT NULL,
  `ubicacion_eve` varchar(2500) DEFAULT NULL,
  `codigo_dir` bigint(11) DEFAULT NULL,
  `antecedentes_eve` text DEFAULT NULL,
  `vocativos_eve` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `evento`
--

INSERT INTO `evento` (`codigo_eve`, `codigo_pro`, `codigo_tip`, `codigo_pri`, `codigo_par`, `codigo_usu`, `estado_eve`, `motivo_rechazo_eve`, `actividad_eve`, `fecha_eve`, `numero_participantes_eve`, `duracion_minutos_eve`, `lugar_eve`, `latitud_eve`, `longitud_eve`, `ubicacion_eve`, `codigo_dir`, `antecedentes_eve`, `vocativos_eve`) VALUES
(2, 1, 1, 2, 1, 3, 'Rechazado', 'Motivo para notificación', 'Fumigacion del coliseo de Aloasi', '2020-03-31 15:00:00', 150, 2, 'Coliseo de Aloasí', -0.517223, -78.5857, 'Coliseo Aloasi, Machachi, Ecuador', 1, NULL, NULL),
(3, 1, 1, 2, 1, 3, 'Rechazado', 'Motivo abcd', 'Rueda de prensa', '2020-04-01 10:00:00', 150, 2, 'Coliseo de Aloasí', -0.517223, -78.5857, 'Coliseo Aloasi, Machachi, Ecuador', 1, NULL, NULL),
(5, 2, 2, 3, 1, 5, 'Rechazado', 'Agenda demasiado apretada', 'Reunión con transportistas', '2020-04-03 11:00:00', 150, 1, 'Dirección de Movilidad', -0.517208, -78.5703, 'CENTRO DE MATRICULACION VEHICULAR, Machachi, Ecuador', 4, NULL, NULL),
(13, 3, 1, 1, 1, 4, 'Aceptado', NULL, 'Reunión urgente del COE cantonal', '2020-04-01 10:00:00', 10, 2, 'Coliseo de Machachi', -0.505665, -78.5677, 'coliseo cerca de Machachi, Ecuador', 3, NULL, NULL),
(14, 4, 2, 1, 1, 4, 'Aceptado', NULL, 'Reunión con empresa contratada para desinfección del mercado', '2020-04-01 09:00:00', 5, 2, 'Mercado Mayorista', -0.515535, -78.5672, 'Mercado Mayorista, Machachi, Ecuador', 3, NULL, NULL),
(15, 3, 1, 1, 1, 4, 'Aceptado', NULL, 'Almuerzo con policias', '2020-04-01 13:00:00', 10, 1, 'Comando de Policia', -0.51552, -78.5647, 'Comando de Policía Mejía, Avenida Cristóbal Colón, Machachi, Ecuador', 3, NULL, NULL),
(16, 4, 1, 1, 3, 3, 'Rechazado', 'Motivo De Prueba', 'Reunion COE parroquial de Cutuglahua', '2020-04-03 10:00:00', 15, 1, 'Santo Domingo de Cutuglagua', -0.372638, -78.5633, 'Iglesia de Santo Domingo De Cutuglagua, Quito, Mejia, Ecuador', 1, 'Antecedentes del ayuda memoria', '- Presidente\r\n- Asambleista\r\n- Ministro'),
(17, 4, 1, 2, 2, 3, 'Aceptado', 'Motivo abc', 'Actividad de prueba para notificaciones', '2020-04-04 08:00:00', 50, 1, 'Coliseo de Alóag', -0.468837, -78.5866, 'Coliseo Aloag, Alóag, Ecuador', 1, 'Estos son los antecedentes de prueba', '- Presidente\r\n- Asambleista'),
(18, 3, 2, 1, 5, 4, 'Aceptado', NULL, 'Alguna actividad', '2020-04-02 16:00:00', 10, 1, 'Accion Social', -0.511477, -78.5649, 'Acción Social de Mejía, Machachi, Ecuador', 3, '', 'P');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modalidad`
--

CREATE TABLE `modalidad` (
  `codigo_mod` bigint(11) NOT NULL,
  `nombre_mod` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notificacion`
--

CREATE TABLE `notificacion` (
  `codigo_not` bigint(11) NOT NULL,
  `mensaje_not` varchar(5000) DEFAULT NULL,
  `emisor_not` bigint(11) DEFAULT NULL,
  `receptor_not` bigint(11) DEFAULT NULL,
  `estado_not` int(11) DEFAULT NULL,
  `fecha_not` datetime DEFAULT NULL,
  `codigo_eve` bigint(11) DEFAULT NULL,
  `push_not` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Volcado de datos para la tabla `notificacion`
--

INSERT INTO `notificacion` (`codigo_not`, `mensaje_not`, `emisor_not`, `receptor_not`, `estado_not`, `fecha_not`, `codigo_eve`, `push_not`) VALUES
(1, 'Evento Creado', 3, 4, 1, '2020-03-31 23:56:27', 17, 0),
(2, 'Evento Rechazado', 4, 3, 1, '2020-03-31 23:59:11', 17, 0),
(4, 'Evento Pre-Aceptado', 4, 3, 1, '2020-04-01 00:23:10', 17, 0),
(5, 'Antecedentes y Vocativos Subidos', 3, 4, 1, '2020-04-01 00:25:44', 17, 0),
(6, 'Evento Acceptado', 4, 3, 1, '2020-04-01 00:26:47', 17, 0),
(7, 'Evento Creado', 4, 4, 1, '2020-04-01 00:28:50', 18, 0),
(8, 'Evento Pre-Aceptado', 4, 4, 1, '2020-04-01 00:29:26', 18, 0),
(9, 'Evento Aceptado', 4, 4, 1, '2020-04-01 00:29:44', 18, 0),
(10, 'Evento Aceptado', 4, 4, 1, '2020-04-01 00:31:19', 18, 0),
(11, 'Evento Aceptado', 4, 4, 1, '2020-04-01 00:34:28', 18, 0),
(12, 'Evento Aceptado', 4, 4, 1, '2020-04-01 00:35:00', 18, 0),
(13, 'Evento Aceptado', 4, 3, 1, '2020-04-01 00:45:30', 17, 0),
(14, 'Evento Rechazado', 4, 3, 1, '2020-04-01 00:46:31', 16, 0),
(15, 'Evento Rechazado', 4, 3, 1, '2020-04-01 00:50:12', 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objetivo_cantonal`
--

CREATE TABLE `objetivo_cantonal` (
  `codigo_oc` bigint(11) NOT NULL,
  `descripcion_oc` varchar(3500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objetivo_desarrollo`
--

CREATE TABLE `objetivo_desarrollo` (
  `codigo_od` bigint(11) NOT NULL,
  `descripcion_od` varchar(3500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objetivo_nacional`
--

CREATE TABLE `objetivo_nacional` (
  `codigo_on` bigint(11) NOT NULL,
  `descripcion_on` varchar(3500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objetivo_pdyot`
--

CREATE TABLE `objetivo_pdyot` (
  `codigo_op` bigint(11) NOT NULL,
  `descripcion_op` varchar(3500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parroquia`
--

CREATE TABLE `parroquia` (
  `codigo_par` bigint(11) NOT NULL,
  `nombre_par` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `parroquia`
--

INSERT INTO `parroquia` (`codigo_par`, `nombre_par`) VALUES
(1, 'Aloasi'),
(2, 'Aloag'),
(3, 'Cutuglagua'),
(4, 'El Chaupi'),
(5, 'Machachi'),
(6, 'Manuel Cornejo Astorga'),
(7, 'Tambillo'),
(8, 'Uyumbicho');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `poa`
--

CREATE TABLE `poa` (
  `codigo_poa` bigint(11) NOT NULL,
  `anio_poa` varchar(100) DEFAULT NULL,
  `descripcion_poa` varchar(100) DEFAULT NULL,
  `codigo_dir` bigint(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `poa`
--

INSERT INTO `poa` (`codigo_poa`, `anio_poa`, `descripcion_poa`, `codigo_dir`) VALUES
(1, '1', 'Plan Operativo Anual', 1),
(2, '1', 'Plan Operativo Anual', 4),
(3, '1', 'Plan Operativo Anual', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prioridad`
--

CREATE TABLE `prioridad` (
  `codigo_pri` bigint(11) NOT NULL,
  `nombre_pri` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `prioridad`
--

INSERT INTO `prioridad` (`codigo_pri`, `nombre_pri`) VALUES
(1, 'Alta'),
(2, 'Media'),
(3, 'Baja');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `codigo_pro` bigint(11) NOT NULL,
  `codigo_par` bigint(11) DEFAULT NULL,
  `codigo_od` bigint(11) DEFAULT NULL,
  `codigo_on` bigint(11) DEFAULT NULL,
  `codigo_oc` bigint(11) DEFAULT NULL,
  `codigo_op` bigint(11) DEFAULT NULL,
  `codigo_poa` bigint(11) UNSIGNED DEFAULT NULL,
  `codigo_mod` bigint(11) DEFAULT NULL,
  `nombre_pro` varchar(5000) DEFAULT NULL,
  `descripcion_pro` varchar(5000) DEFAULT NULL,
  `componentes_pro` varchar(5000) DEFAULT NULL,
  `total_financiamiento_pro` float DEFAULT NULL,
  `primer_cuatrimestre_pro` tinyint(1) DEFAULT NULL,
  `segundo_cuatrimestre_pro` tinyint(1) DEFAULT NULL,
  `tercer_cuatrimestre_pro` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`codigo_pro`, `codigo_par`, `codigo_od`, `codigo_on`, `codigo_oc`, `codigo_op`, `codigo_poa`, `codigo_mod`, `nombre_pro`, `descripcion_pro`, `componentes_pro`, `total_financiamiento_pro`, `primer_cuatrimestre_pro`, `segundo_cuatrimestre_pro`, `tercer_cuatrimestre_pro`) VALUES
(1, 1, NULL, NULL, NULL, NULL, 1, NULL, 'Proyecto de Prueba 1', '', NULL, 25350, NULL, NULL, NULL),
(2, 1, NULL, NULL, NULL, NULL, 2, NULL, 'Actividades Institucionales', NULL, NULL, NULL, NULL, NULL, NULL),
(3, 1, NULL, NULL, NULL, NULL, 3, NULL, 'Actividades Institucionales', NULL, NULL, NULL, NULL, NULL, NULL),
(4, 1, NULL, NULL, NULL, NULL, 1, NULL, 'Actividades Institucionales', NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo`
--

CREATE TABLE `tipo` (
  `codigo_tip` bigint(11) NOT NULL,
  `nombre_tip` varchar(500) DEFAULT NULL,
  `color_tip` varchar(50) DEFAULT 'gray'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `tipo`
--

INSERT INTO `tipo` (`codigo_tip`, `nombre_tip`, `color_tip`) VALUES
(1, 'Social', 'gray'),
(2, 'Político', 'gray');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `unidad`
--

CREATE TABLE `unidad` (
  `codigo_uni` bigint(11) NOT NULL,
  `nombre_uni` varchar(100) DEFAULT NULL,
  `codigo_dir` bigint(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `unidad`
--

INSERT INTO `unidad` (`codigo_uni`, `nombre_uni`, `codigo_dir`) VALUES
(1, 'TICS', 1),
(2, 'DIRECCION', 1),
(3, 'SECRETARIA', 3),
(4, 'DIRECCION', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `codigo_usu` bigint(11) NOT NULL,
  `nombre_usu` varchar(100) DEFAULT NULL,
  `email_usu` varchar(100) DEFAULT NULL,
  `password_usu` varchar(100) DEFAULT NULL,
  `codigo_uni` bigint(11) DEFAULT NULL,
  `perfil_usu` varchar(100) DEFAULT NULL,
  `estado_usu` tinyint(1) DEFAULT NULL,
  `es_delegado` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`codigo_usu`, `nombre_usu`, `email_usu`, `password_usu`, `codigo_uni`, `perfil_usu`, `estado_usu`, `es_delegado`) VALUES
(1, 'Angel Toapanta', 'a', 'QWWERTYU', 1, 'Coordinador', 1, 0),
(2, 'René Quisaguano', 'r', 'QWWERTYU', 1, 'Empleado', 1, 0),
(3, 'Jorge Pazmiño', 'j.pazmiño', 'QWWERTYU', 2, 'Director', 1, 0),
(4, 'Zoila Orquera', 'z.orquera', 'QWWERTYU', 3, 'Agenda', 1, 0),
(5, 'Teodoro Remache', 't.remache', 'QWWERTYU', 4, 'Director', 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vocativo`
--

CREATE TABLE `vocativo` (
  `codigo_voc` bigint(11) NOT NULL,
  `apellido_voc` varchar(500) DEFAULT NULL,
  `nombre_voc` varchar(500) DEFAULT NULL,
  `cargo_voc` varchar(500) DEFAULT NULL,
  `telefono_voc` varchar(15) DEFAULT NULL,
  `codigo_eve` bigint(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anio`
--
ALTER TABLE `anio`
  ADD PRIMARY KEY (`codigo_ani`) USING BTREE;

--
-- Indices de la tabla `ayuda_memoria`
--
ALTER TABLE `ayuda_memoria`
  ADD PRIMARY KEY (`codigo_am`),
  ADD KEY `codigo_eve` (`codigo_eve`);

--
-- Indices de la tabla `delegado`
--
ALTER TABLE `delegado`
  ADD PRIMARY KEY (`codigo_del`),
  ADD KEY `codigo_eve` (`codigo_eve`),
  ADD KEY `codigo_usu` (`codigo_usu`);

--
-- Indices de la tabla `direccion`
--
ALTER TABLE `direccion`
  ADD PRIMARY KEY (`codigo_dir`) USING BTREE;

--
-- Indices de la tabla `evento`
--
ALTER TABLE `evento`
  ADD PRIMARY KEY (`codigo_eve`) USING BTREE,
  ADD KEY `codigo_pro` (`codigo_pro`) USING BTREE,
  ADD KEY `codigo_tip` (`codigo_tip`) USING BTREE,
  ADD KEY `codigo_pri` (`codigo_pri`) USING BTREE,
  ADD KEY `codigo_par` (`codigo_par`) USING BTREE,
  ADD KEY `codigo_usu` (`codigo_usu`) USING BTREE,
  ADD KEY `fk_direccion_evento` (`codigo_dir`) USING BTREE;

--
-- Indices de la tabla `modalidad`
--
ALTER TABLE `modalidad`
  ADD PRIMARY KEY (`codigo_mod`) USING BTREE;

--
-- Indices de la tabla `notificacion`
--
ALTER TABLE `notificacion`
  ADD PRIMARY KEY (`codigo_not`) USING BTREE;

--
-- Indices de la tabla `objetivo_cantonal`
--
ALTER TABLE `objetivo_cantonal`
  ADD PRIMARY KEY (`codigo_oc`) USING BTREE;

--
-- Indices de la tabla `objetivo_desarrollo`
--
ALTER TABLE `objetivo_desarrollo`
  ADD PRIMARY KEY (`codigo_od`) USING BTREE;

--
-- Indices de la tabla `objetivo_nacional`
--
ALTER TABLE `objetivo_nacional`
  ADD PRIMARY KEY (`codigo_on`) USING BTREE;

--
-- Indices de la tabla `objetivo_pdyot`
--
ALTER TABLE `objetivo_pdyot`
  ADD PRIMARY KEY (`codigo_op`) USING BTREE;

--
-- Indices de la tabla `parroquia`
--
ALTER TABLE `parroquia`
  ADD PRIMARY KEY (`codigo_par`) USING BTREE;

--
-- Indices de la tabla `poa`
--
ALTER TABLE `poa`
  ADD PRIMARY KEY (`codigo_poa`) USING BTREE,
  ADD KEY `codigo_dir` (`codigo_dir`) USING BTREE;

--
-- Indices de la tabla `prioridad`
--
ALTER TABLE `prioridad`
  ADD PRIMARY KEY (`codigo_pri`) USING BTREE;

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`codigo_pro`) USING BTREE,
  ADD KEY `codigo_par` (`codigo_par`) USING BTREE,
  ADD KEY `codigo_od` (`codigo_od`) USING BTREE,
  ADD KEY `codigo_on` (`codigo_on`) USING BTREE,
  ADD KEY `codigo_oc` (`codigo_oc`) USING BTREE,
  ADD KEY `codigo_op` (`codigo_op`) USING BTREE,
  ADD KEY `codigo_mod` (`codigo_mod`) USING BTREE;

--
-- Indices de la tabla `tipo`
--
ALTER TABLE `tipo`
  ADD PRIMARY KEY (`codigo_tip`) USING BTREE;

--
-- Indices de la tabla `unidad`
--
ALTER TABLE `unidad`
  ADD PRIMARY KEY (`codigo_uni`) USING BTREE,
  ADD KEY `codigo_dir` (`codigo_dir`) USING BTREE;

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`codigo_usu`) USING BTREE,
  ADD KEY `codigo_uni` (`codigo_uni`) USING BTREE;

--
-- Indices de la tabla `vocativo`
--
ALTER TABLE `vocativo`
  ADD PRIMARY KEY (`codigo_voc`),
  ADD KEY `codigo_eve` (`codigo_eve`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anio`
--
ALTER TABLE `anio`
  MODIFY `codigo_ani` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `ayuda_memoria`
--
ALTER TABLE `ayuda_memoria`
  MODIFY `codigo_am` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `delegado`
--
ALTER TABLE `delegado`
  MODIFY `codigo_del` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `direccion`
--
ALTER TABLE `direccion`
  MODIFY `codigo_dir` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `evento`
--
ALTER TABLE `evento`
  MODIFY `codigo_eve` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `modalidad`
--
ALTER TABLE `modalidad`
  MODIFY `codigo_mod` bigint(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `notificacion`
--
ALTER TABLE `notificacion`
  MODIFY `codigo_not` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `objetivo_cantonal`
--
ALTER TABLE `objetivo_cantonal`
  MODIFY `codigo_oc` bigint(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `objetivo_desarrollo`
--
ALTER TABLE `objetivo_desarrollo`
  MODIFY `codigo_od` bigint(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `objetivo_nacional`
--
ALTER TABLE `objetivo_nacional`
  MODIFY `codigo_on` bigint(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `objetivo_pdyot`
--
ALTER TABLE `objetivo_pdyot`
  MODIFY `codigo_op` bigint(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `parroquia`
--
ALTER TABLE `parroquia`
  MODIFY `codigo_par` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `poa`
--
ALTER TABLE `poa`
  MODIFY `codigo_poa` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `prioridad`
--
ALTER TABLE `prioridad`
  MODIFY `codigo_pri` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `codigo_pro` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipo`
--
ALTER TABLE `tipo`
  MODIFY `codigo_tip` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `unidad`
--
ALTER TABLE `unidad`
  MODIFY `codigo_uni` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `codigo_usu` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `vocativo`
--
ALTER TABLE `vocativo`
  MODIFY `codigo_voc` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ayuda_memoria`
--
ALTER TABLE `ayuda_memoria`
  ADD CONSTRAINT `ayuda_memoria_ibfk_1` FOREIGN KEY (`codigo_eve`) REFERENCES `evento` (`codigo_eve`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `delegado`
--
ALTER TABLE `delegado`
  ADD CONSTRAINT `delegado_ibfk_1` FOREIGN KEY (`codigo_eve`) REFERENCES `evento` (`codigo_eve`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `delegado_ibfk_2` FOREIGN KEY (`codigo_usu`) REFERENCES `usuario` (`codigo_usu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `evento`
--
ALTER TABLE `evento`
  ADD CONSTRAINT `evento_ibfk_1` FOREIGN KEY (`codigo_pro`) REFERENCES `proyecto` (`codigo_pro`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `evento_ibfk_2` FOREIGN KEY (`codigo_tip`) REFERENCES `tipo` (`codigo_tip`) ON UPDATE CASCADE,
  ADD CONSTRAINT `evento_ibfk_3` FOREIGN KEY (`codigo_pri`) REFERENCES `prioridad` (`codigo_pri`) ON UPDATE CASCADE,
  ADD CONSTRAINT `evento_ibfk_4` FOREIGN KEY (`codigo_par`) REFERENCES `parroquia` (`codigo_par`) ON UPDATE CASCADE,
  ADD CONSTRAINT `evento_ibfk_5` FOREIGN KEY (`codigo_usu`) REFERENCES `usuario` (`codigo_usu`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_direccion_evento` FOREIGN KEY (`codigo_dir`) REFERENCES `direccion` (`codigo_dir`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `vocativo`
--
ALTER TABLE `vocativo`
  ADD CONSTRAINT `vocativo_ibfk_1` FOREIGN KEY (`codigo_eve`) REFERENCES `evento` (`codigo_eve`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
