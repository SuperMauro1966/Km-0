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

-- Dump della struttura di tabella km-0.tbcredential
DROP TABLE IF EXISTS `tbcredential`;
CREATE TABLE IF NOT EXISTS `tbcredential` (
  `idCredential` int(11) NOT NULL AUTO_INCREMENT,
  `pswd` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`idCredential`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcredential: ~2 rows (circa)
DELETE FROM `tbcredential`;
INSERT INTO `tbcredential` (`idCredential`, `pswd`, `email`) VALUES
	(1, '1234', 'Sergio'),
	(2, '1234', 'Gabriele');

-- Dump della struttura di tabella km-0.tbvenditore
DROP TABLE IF EXISTS `tbvenditore`;
CREATE TABLE IF NOT EXISTS `tbvenditore` (
  `idVenditore` int(11) NOT NULL AUTO_INCREMENT,
  `sitoweb` varchar(255) DEFAULT NULL,
  `partitaIVA` int(11) DEFAULT NULL,
  `ragioneSociale` varchar(255) DEFAULT NULL,
  `CF` varchar(16) DEFAULT NULL,
  `idCredential` int(11) DEFAULT NULL,
  PRIMARY KEY (`idVenditore`),
  KEY `codCredential` (`idCredential`) USING BTREE,
  CONSTRAINT `tbvenditore_ibfk_1` FOREIGN KEY (`idCredential`) REFERENCES `tbcredential` (`idCredential`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbvenditore: ~0 rows (circa)
DELETE FROM `tbvenditore`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
