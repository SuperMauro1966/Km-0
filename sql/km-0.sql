-- -------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              10.6.18-MariaDB - mariadb.org binary distribution
-- S.O. server:                  Win64
-- HeidiSQL Versione:            12.6.0.6765
-- -------------------------------------------------------

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
  `provincia` varchar(2) NOT NULL,
  `via` varchar(255) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cognome` varchar(255) NOT NULL,
  `CF` varchar(16) NOT NULL,
  `telefono` varchar(14) NOT NULL,
  `idCredential` int(11) NOT NULL,
  PRIMARY KEY (`idCliente`),
  KEY `FK_tbcliente_idCredential_tbcredential_idCredential` (`idCredential`),
  CONSTRAINT `FK_tbcliente_idCredential_tbcredential_idCredential` FOREIGN KEY (`idCredential`) REFERENCES `tbcredential` (`idCredential`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcliente: ~1 rows (circa)
DELETE FROM `tbcliente`;
INSERT INTO `tbcliente` (`idCliente`, `citta`, `provincia`, `via`, `nome`, `cognome`, `CF`, `telefono`, `idCredential`) VALUES
	(1, 'Imola', 'BO', 'Via della liberazione', 'Mario', 'Rossi', 'AAA', '+39', 3);

-- Dump della struttura di tabella km-0.tbcredential
DROP TABLE IF EXISTS `tbcredential`;
CREATE TABLE IF NOT EXISTS `tbcredential` (
  `idCredential` int(11) NOT NULL AUTO_INCREMENT,
  `pswd` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`idCredential`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcredential: ~4 rows (circa)
DELETE FROM `tbcredential`;
INSERT INTO `tbcredential` (`idCredential`, `pswd`, `email`) VALUES
	(1, '1234', 'Sergio'),
	(2, '1234', 'Gabriele'),
	(3, '5678', 'Pippo'),
	(4, '5678', 'Pluto');

-- Dump della struttura di tabella km-0.tbevento
DROP TABLE IF EXISTS `tbevento`;
CREATE TABLE IF NOT EXISTS `tbevento` (
  `idEvento` int(11) NOT NULL AUTO_INCREMENT,
  `descrizione` text NOT NULL,
  `dataInizio` datetime NOT NULL,
  `dataFine` datetime NOT NULL,
  `nome` varchar(255) NOT NULL,
  `condiviso` tinyint(1) NOT NULL,
  `idCredential` int(11) NOT NULL,
  PRIMARY KEY (`idEvento`),
  KEY `FK_tbevento_idCredential_tbcredential_idCredential` (`idCredential`) USING BTREE,
  CONSTRAINT `FK_tbevento_idCredential_tbcredential_idCredential` FOREIGN KEY (`idCredential`) REFERENCES `tbcredential` (`idCredential`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbevento: ~0 rows (circa)
DELETE FROM `tbevento`;

-- Dump della struttura di tabella km-0.tbservizio
DROP TABLE IF EXISTS `tbservizio`;
CREATE TABLE IF NOT EXISTS `tbservizio` (
  `idServizio` int(11) NOT NULL AUTO_INCREMENT,
  `descrizione` text NOT NULL,
  `nome` varchar(255) NOT NULL,
  PRIMARY KEY (`idServizio`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbservizio: ~0 rows (circa)
DELETE FROM `tbservizio`;

-- Dump della struttura di tabella km-0.tbubicazione
DROP TABLE IF EXISTS `tbubicazione`;
CREATE TABLE IF NOT EXISTS `tbubicazione` (
  `idUbicazione` int(11) NOT NULL AUTO_INCREMENT,
  `citta` varchar(255) NOT NULL,
  `provincia` varchar(2) NOT NULL,
  `via` varchar(255) NOT NULL,
  `fissa` tinyint(1) NOT NULL,
  `orario` text NOT NULL,
  `attiva` tinyint(1) NOT NULL,
  PRIMARY KEY (`idUbicazione`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbubicazione: ~0 rows (circa)
DELETE FROM `tbubicazione`;

-- Dump della struttura di tabella km-0.tbvenditore
DROP TABLE IF EXISTS `tbvenditore`;
CREATE TABLE IF NOT EXISTS `tbvenditore` (
  `idVenditore` int(11) NOT NULL AUTO_INCREMENT,
  `sitoweb` varchar(255) NOT NULL,
  `partitaIVA` int(11) NOT NULL,
  `ragioneSociale` varchar(255) NOT NULL,
  `CF` varchar(16) NOT NULL,
  `idCredential` int(11) NOT NULL,
  PRIMARY KEY (`idVenditore`),
  KEY `FK_tbvenditore_idCredential_tbcredential_idCredential` (`idCredential`) USING BTREE,
  CONSTRAINT `tbvenditore_ibfk_1` FOREIGN KEY (`idCredential`) REFERENCES `tbcredential` (`idCredential`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbvenditore: ~1 rows (circa)
DELETE FROM `tbvenditore`;
INSERT INTO `tbvenditore` (`idVenditore`, `sitoweb`, `partitaIVA`, `ragioneSociale`, `CF`, `idCredential`) VALUES
	(1, 'www.disney.it', 10, 'Topolino', 'BBB', 4);

-- Dump della struttura di vista km-0.vwadmin
DROP VIEW IF EXISTS `vwadmin`;
-- Creazione di una tabella temporanea per risolvere gli errori di dipendenza della vista
CREATE TABLE `vwadmin` (
	`idCredential` INT(11) NOT NULL,
	`email` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`pswd` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci'
) ENGINE=MyISAM;

-- Rimozione temporanea di tabella e creazione della struttura finale della vista
DROP TABLE IF EXISTS `vwadmin`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vwadmin` AS select `tbcredential`.`idCredential` AS `idCredential`,`tbcredential`.`email` AS `email`,`tbcredential`.`pswd` AS `pswd` from `tbcredential` where !(`tbcredential`.`idCredential` in ((select `tbvenditore`.`idCredential` from `tbvenditore`) union (select `tbcliente`.`idCredential` from `tbcliente`)));

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
