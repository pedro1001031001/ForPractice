-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla bolice.cliente
DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_pat` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `apellido_mat` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `domicilio` varchar(50) DEFAULT NULL,
  `telefono` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `RFC` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bolice.cliente: ~4 rows (aproximadamente)
INSERT INTO `cliente` (`id_cliente`, `nombre`, `apellido_pat`, `apellido_mat`, `domicilio`, `telefono`, `RFC`) VALUES
	(1, 'Lex', 'Luthor', ' ', 'Smallville', '000000', '000'),
	(2, 'Eobard', 'Thawne', ' ', 'Central City', '000000', '000'),
	(3, 'Harleen', 'Quinzel', ' ', 'Gotham City', '000000', '000'),
	(4, 'Pamela', 'Isley', ' ', 'Gotham City', '000000', '000'),
	(5, 'Selina', 'Kyle', ' ', 'Gotham City', '000000', '000');

-- Volcando estructura para tabla bolice.inventario
DROP TABLE IF EXISTS `inventario`;
CREATE TABLE IF NOT EXISTS `inventario` (
  `piezas` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bolice.inventario: ~0 rows (aproximadamente)

-- Volcando estructura para tabla bolice.producto
DROP TABLE IF EXISTS `producto`;
CREATE TABLE IF NOT EXISTS `producto` (
  `Id_producto` int DEFAULT NULL,
  `precio` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bolice.producto: ~0 rows (aproximadamente)

-- Volcando estructura para tabla bolice.sabor
DROP TABLE IF EXISTS `sabor`;
CREATE TABLE IF NOT EXISTS `sabor` (
  `Id_sabor` int NOT NULL AUTO_INCREMENT,
  `sabor` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id_sabor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bolice.sabor: ~4 rows (aproximadamente)
INSERT INTO `sabor` (`Id_sabor`, `sabor`) VALUES
	(1, 'Nuez'),
	(2, 'Chocolate'),
	(3, 'Coco'),
	(4, 'Fresa'),
	(5, 'Vainilla');

-- Volcando estructura para tabla bolice.tama_o
DROP TABLE IF EXISTS `tama_o`;
CREATE TABLE IF NOT EXISTS `tama_o` (
  `Id_tam` int NOT NULL AUTO_INCREMENT,
  `tama_o` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`Id_tam`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bolice.tama_o: ~2 rows (aproximadamente)
INSERT INTO `tama_o` (`Id_tam`, `tama_o`) VALUES
	(1, 'Grande'),
	(2, 'Mediano'),
	(3, 'Pequeño');

-- Volcando estructura para tabla bolice.usuario
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_pat` varchar(30) DEFAULT NULL,
  `apellido_mat` varchar(30) NOT NULL,
  `contrase_a` varchar(16) DEFAULT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla bolice.usuario: ~5 rows (aproximadamente)
INSERT INTO `usuario` (`id_usuario`, `nombre`, `apellido_pat`, `apellido_mat`, `contrase_a`, `correo`, `telefono`) VALUES
	(1, 'Bruce', 'Wayne', ' ', 'soybatman', 'batman@gmail.com', '6666666'),
	(2, 'Clark', 'Kent', ' ', 'soysuperman', 'superman@gmail.com', '10000001'),
	(3, 'Barry', 'Allen', ' ', 'soyflash', 'flash@gmail.com', '2000000002'),
	(4, 'Arthur', 'Curry', ' ', 'soyaquaman', 'aquaman@gmail.com', NULL),
	(5, 'Diana', 'Prince', ' ', 'soywander', 'wanderwoman@gmail.com', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
