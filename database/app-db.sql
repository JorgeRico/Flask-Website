-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 28-05-2025 a las 00:32:44
-- Versión del servidor: 8.0.42
-- Versión de PHP: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `app-db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mtgSet`
--

CREATE TABLE `mtgSet` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `numCards` int NOT NULL,
  `deleted` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `mtgSet`
--

INSERT INTO `mtgSet` (`id`, `name`, `numCards`, `deleted`) VALUES
(1, 'Test', 200, 0),
(2, 'Test 2', 200, 0),
(3, 'Test 3', 200, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `mtgSet`
--
ALTER TABLE `mtgSet`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `mtgSet`
--
ALTER TABLE `mtgSet`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
