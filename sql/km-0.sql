-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              10.6.18-MariaDB - mariadb.org binary distribution
-- S.O. server:                  Win64
-- HeidiSQL Versione:            12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dump della struttura del database km-0
DROP DATABASE IF EXISTS `km-0`;
CREATE DATABASE IF NOT EXISTS `km-0` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `km-0`;

-- Dump della struttura di tabella km-0.tbcliente
DROP TABLE IF EXISTS `tbcliente`;
CREATE TABLE IF NOT EXISTS `tbcliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `citta` varchar(34) NOT NULL,
  `provincia` varchar(34) NOT NULL,
  `via` varchar(255) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cognome` varchar(255) NOT NULL,
  `CF` varchar(16) NOT NULL,
  `telefono` varchar(14) NOT NULL,
  `idCredential` int(11) NOT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `FK_tbcliente_idCredential_tbcredential_idCredential` (`idCredential`),
  CONSTRAINT `FK_tbcliente_idCredential_tbcredential_idCredential` FOREIGN KEY (`idCredential`) REFERENCES `tbcredential` (`idCredential`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcliente: ~0 rows (circa)
DELETE FROM `tbcliente`;

-- Dump della struttura di tabella km-0.tbcredential
DROP TABLE IF EXISTS `tbcredential`;
CREATE TABLE IF NOT EXISTS `tbcredential` (
  `idCredential` int(11) NOT NULL AUTO_INCREMENT,
  `pswd` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`idCredential`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcredential: ~2 rows (circa)
DELETE FROM `tbcredential`;
INSERT INTO `tbcredential` (`idCredential`, `pswd`, `email`) VALUES
	(1, '1234', 'Sergio'),
	(2, '1234', 'Gabriele');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
