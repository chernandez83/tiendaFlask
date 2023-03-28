-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2023 at 05:10 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tiendaflask`
--

-- --------------------------------------------------------

--
-- Table structure for table `autor`
--

CREATE TABLE `autor` (
  `ID` smallint(4) UNSIGNED NOT NULL,
  `apellidos` varchar(40) NOT NULL,
  `nombres` varchar(40) NOT NULL,
  `fechanacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Almacena los datos de los autores';

--
-- Dumping data for table `autor`
--

INSERT INTO `autor` (`ID`, `apellidos`, `nombres`, `fechanacimiento`) VALUES
(1, 'Vallejo Mendoza', 'César Abraham', '1892-03-16'),
(2, 'Vargas Llosa', 'Jorge Mario Pedro', '1936-03-28'),
(3, 'Alegría Bazán', 'Ciro', '1909-11-04'),
(4, 'García Márquez', 'Gabriel José de la Concordia', '1927-03-06');

-- --------------------------------------------------------

--
-- Table structure for table `compra`
--

CREATE TABLE `compra` (
  `UUID` char(36) NOT NULL,
  `ISBN` char(12) NOT NULL,
  `usuario_id` smallint(3) UNSIGNED NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena las compras';

--
-- Dumping data for table `compra`
--

INSERT INTO `compra` (`UUID`, `ISBN`, `usuario_id`, `fecha`) VALUES
('06f9d5a1-cb6b-11ed-8398-7824af88fa76', '892014771852', 3, '2023-03-25 18:13:25'),
('1deedac1-cb6b-11ed-8398-7824af88fa76', '589120131047', 3, '2023-03-25 18:14:04'),
('6e671e86-cd15-11ed-9985-7824af88fa76', '383370912281', 3, '2023-03-27 21:05:44'),
('81fa98d8-cb6b-11ed-8398-7824af88fa76', '930281938211', 4, '2023-03-25 18:16:52'),
('842c0c95-cb6b-11ed-8398-7824af88fa76', '591338770183', 4, '2023-03-25 18:16:55'),
('8e916408-cd11-11ed-9985-7824af88fa76', '762841019387', 3, '2023-03-27 20:38:00'),
('e8039e66-cd15-11ed-9985-7824af88fa76', '383370912281', 4, '2023-03-27 21:09:08');

-- --------------------------------------------------------

--
-- Table structure for table `libro`
--

CREATE TABLE `libro` (
  `ISBN` char(12) NOT NULL,
  `Titulo` varchar(100) NOT NULL,
  `autor_id` smallint(4) UNSIGNED NOT NULL,
  `anoedicion` year(4) NOT NULL,
  `precio` decimal(3,0) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los datos de los libros';

--
-- Dumping data for table `libro`
--

INSERT INTO `libro` (`ISBN`, `Titulo`, `autor_id`, `anoedicion`, `precio`) VALUES
('238874100138', 'Conversación en La Catedral', 2, 1951, '70'),
('383370912281', 'El mundo es ancho y ajeno', 3, 1941, '65'),
('480129403571', 'La ciudad y los perros', 2, 1963, '81'),
('483240184226', 'La serpiente de oro', 3, 1935, '85'),
('589120131047', 'Los perros hambrientos', 3, 1939, '31'),
('591338770183', 'Paco Yunque', 1, 1951, '55'),
('661984010128', 'El general en su laberinto', 4, 1989, '110'),
('683425019133', 'El coronel no tiene quien le escriba', 4, 1961, '42'),
('762841019387', 'Cien años de soledad', 4, 1967, '75'),
('890366138239', 'La fiesta del Chivo', 2, 2000, '30'),
('892014771852', 'Poemas humanos', 1, 1939, '120'),
('930281938211', 'El amor en los tiempos del cólera', 4, 1985, '38'),
('978318472263', 'Los heraldos negros', 1, 1919, '48'),
('981402938251', 'La casa verde', 2, 1966, '105');

-- --------------------------------------------------------

--
-- Table structure for table `tipousuario`
--

CREATE TABLE `tipousuario` (
  `ID` tinyint(1) UNSIGNED NOT NULL,
  `Nombre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Alamacena los tipos de usuarios';

--
-- Dumping data for table `tipousuario`
--

INSERT INTO `tipousuario` (`ID`, `Nombre`) VALUES
(1, 'Administrador'),
(2, 'Cliente');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `ID` smallint(3) UNSIGNED NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `tipousuario_id` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Alamacena los usuarios';

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`ID`, `usuario`, `password`, `tipousuario_id`) VALUES
(2, 'admin', 'pbkdf2:sha256:260000$TIb5dcVia6HCEG3H$dff2ccb0e4bf813076393e3d72ec3a89133aa29df18e5ed3d2bead2630b63c70', 1),
(3, 'Cut', 'pbkdf2:sha256:260000$scMIShtKgBv0Wac5$4e8a022e23ed17e0b383c2ed93033253c91e03c6af40c296a040b733c66d4e01', 2),
(4, 'Uriel', 'pbkdf2:sha256:260000$jMTXdF6vXmAJ846T$adc3a76d90527b432470ca1ef4b3b2b1ac9a0374f6f386cad85eb0d6563a9be1', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`UUID`),
  ADD KEY `FK_compra_libro` (`ISBN`),
  ADD KEY `FK_compra_usuario` (`usuario_id`);

--
-- Indexes for table `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`ISBN`),
  ADD KEY `FK_libro_autor` (`autor_id`);

--
-- Indexes for table `tipousuario`
--
ALTER TABLE `tipousuario`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_usuario_tipousuario` (`tipousuario_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `autor`
--
ALTER TABLE `autor`
  MODIFY `ID` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tipousuario`
--
ALTER TABLE `tipousuario`
  MODIFY `ID` tinyint(1) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `FK_compra_libro` FOREIGN KEY (`ISBN`) REFERENCES `libro` (`ISBN`),
  ADD CONSTRAINT `FK_compra_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`ID`);

--
-- Constraints for table `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `FK_libro_autor` FOREIGN KEY (`autor_id`) REFERENCES `autor` (`ID`);

--
-- Constraints for table `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `FK_usuario_tipousuario` FOREIGN KEY (`tipousuario_id`) REFERENCES `tipousuario` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
