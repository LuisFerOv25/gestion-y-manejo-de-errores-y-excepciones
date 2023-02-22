-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-02-2023 a las 03:47:44
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_farmaclick`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id_categoria`, `nombre`) VALUES
(1, 'cuidado personal'),
(2, 'dermacosmetico'),
(3, 'nutricionales'),
(4, 'bebe'),
(5, 'medicamentos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(400) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio` double NOT NULL,
  `proveedor` varchar(45) NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `imagen` text NOT NULL,
  `categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `nombre`, `descripcion`, `cantidad`, `precio`, `proveedor`, `fecha_vencimiento`, `imagen`, `categoria`) VALUES
(3, 'talco', 'NaN', 5, 500, 'rexona', '2023-11-12', 'Entity Relationship Diagram.jpg', 4),
(8, 'maquillaje', 'NaN', 5, 5000, 'Nivea', '2023-12-15', 'EXPO ETICA.docx', 2),
(9, 'vitamina B', 'NaN', 7, 58000, 'Colpatria', '2026-11-12', 'carrera.xlsx', 3),
(10, 'tretinol', 'NaN', 5, 5799, 'axa', '2024-11-09', 'Entity Relationship Diagram.jpg', 5),
(11, 'desodorante', 'NaN', 20, 6000, 'NaN', '2023-11-12', 'martillb.blend', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `tipo_user` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `apellido` varchar(60) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `direccion` varchar(60) NOT NULL,
  `telefono` char(12) NOT NULL,
  `genero` varchar(20) NOT NULL,
  `password` text NOT NULL,
  `create_at` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `tipo_user`, `nombre`, `apellido`, `correo`, `direccion`, `telefono`, `genero`, `password`, `create_at`) VALUES
(1, 2, 'luis', 'oviedo', 'luis45@gmail.com', 'nan', '5555555555', 'Masculino', 'sha256$AANyD2VAgb3FNw0H$79da655b19df5350b2240ca36eec09170b6c0a26824a41ac2e9a82a1ce60b9b0', '2023-02-16'),
(2, 2, 'momica', 'juarez', 'moinica@g.com', 'bfdbgb', '3444444', 'Femenino', 'sha256$0gGcYyslBhaaer6d$c0284b1bf5b8bbe4715b9d086a4c16c9a02f8ea85d69111a296b4a08e9984a9f', '2023-2-16'),
(3, 1, 'julio', 'norma', 'mz234', 'k@g.com', '3211111111', 'Male', '', ''),
(6, 1, 'carlos', 'narvaez', 'gfh@g.com', 'sgdfhf', '1111222222', 'Male', 'sha256$ssWPEvpNE6A80zQF$908f23c351fec204110c6cae84ed389c52764fefa327d0d6671290d305c23515', '2023-2-17'),
(7, 2, 'juan', 'cordoba', 'juanc@gmail.com', 'bgfht5', '321555555', 'Masculino', 'sha256$zWsELssmlWg2xtym$46708311343c9f68edb241eb97011ccd956e9cafb5870d4caab0cd133a54d402', '2023-2-21');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `categoria` (`categoria`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id_categoria`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
