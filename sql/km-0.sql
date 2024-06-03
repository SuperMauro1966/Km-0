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

-- Dump della struttura di tabella km-0.tbaccetta
DROP TABLE IF EXISTS `tbaccetta`;
CREATE TABLE IF NOT EXISTS `tbaccetta` (
  `idVenditore` int(11) NOT NULL,
  `idPagamento` int(11) NOT NULL,
  PRIMARY KEY (`idVenditore`,`idPagamento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbaccetta: ~0 rows (circa)
DELETE FROM `tbaccetta`;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcliente: ~0 rows (circa)
DELETE FROM `tbcliente`;

-- Dump della struttura di tabella km-0.tbcontiene
DROP TABLE IF EXISTS `tbcontiene`;
CREATE TABLE IF NOT EXISTS `tbcontiene` (
  `idServizio` int(11) NOT NULL,
  `idOrdine` int(11) NOT NULL,
  PRIMARY KEY (`idServizio`,`idOrdine`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcontiene: ~0 rows (circa)
DELETE FROM `tbcontiene`;

-- Dump della struttura di tabella km-0.tbcrea
DROP TABLE IF EXISTS `tbcrea`;
CREATE TABLE IF NOT EXISTS `tbcrea` (
  `idVenditore` int(11) NOT NULL,
  `idEvento` int(11) NOT NULL,
  PRIMARY KEY (`idVenditore`,`idEvento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcrea: ~0 rows (circa)
DELETE FROM `tbcrea`;

-- Dump della struttura di tabella km-0.tbcredential
DROP TABLE IF EXISTS `tbcredential`;
CREATE TABLE IF NOT EXISTS `tbcredential` (
  `idCredential` int(11) NOT NULL AUTO_INCREMENT,
  `pswd` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `attivo` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`idCredential`),
  UNIQUE KEY `idx_tbcredential_email_pswd` (`email`,`pswd`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbcredential: ~2 rows (circa)
DELETE FROM `tbcredential`;
INSERT INTO `tbcredential` (`idCredential`, `pswd`, `email`, `attivo`) VALUES
	(1, '1234', 'Sergio', 1),
	(2, '1234', 'Gabriele', 1);

-- Dump della struttura di tabella km-0.tbeffettua
DROP TABLE IF EXISTS `tbeffettua`;
CREATE TABLE IF NOT EXISTS `tbeffettua` (
  `idCliente` int(11) NOT NULL,
  `idOrdine` int(11) NOT NULL,
  `idPagamento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbeffettua: ~0 rows (circa)
DELETE FROM `tbeffettua`;

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

-- Dump della struttura di tabella km-0.tbmodalitapagamento
DROP TABLE IF EXISTS `tbmodalitapagamento`;
CREATE TABLE IF NOT EXISTS `tbmodalitapagamento` (
  `idPagamento` int(11) NOT NULL,
  `idOrdine` int(11) NOT NULL,
  PRIMARY KEY (`idPagamento`,`idOrdine`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbmodalitapagamento: ~0 rows (circa)
DELETE FROM `tbmodalitapagamento`;

-- Dump della struttura di tabella km-0.tboffre
DROP TABLE IF EXISTS `tboffre`;
CREATE TABLE IF NOT EXISTS `tboffre` (
  `idPagamento` int(11) NOT NULL,
  `idServizio` int(11) NOT NULL,
  `prezzo` float NOT NULL,
  `quantita` text NOT NULL,
  PRIMARY KEY (`idPagamento`,`idServizio`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tboffre: ~0 rows (circa)
DELETE FROM `tboffre`;

-- Dump della struttura di tabella km-0.tbordine
DROP TABLE IF EXISTS `tbordine`;
CREATE TABLE IF NOT EXISTS `tbordine` (
  `idOrdine` int(11) NOT NULL AUTO_INCREMENT,
  `stato` varchar(10) NOT NULL,
  `data` datetime NOT NULL,
  `idRecensione` int(11) NOT NULL,
  PRIMARY KEY (`idOrdine`),
  KEY `FK_tbordine_idRecensione_tbpagameneto_idPagamento` (`idRecensione`),
  CONSTRAINT `FK_tbordine_idRecensione_tbpagameneto_idPagamento` FOREIGN KEY (`idRecensione`) REFERENCES `tbpagamento` (`idPagamento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbordine: ~0 rows (circa)
DELETE FROM `tbordine`;

-- Dump della struttura di tabella km-0.tbpagamento
DROP TABLE IF EXISTS `tbpagamento`;
CREATE TABLE IF NOT EXISTS `tbpagamento` (
  `idPagamento` int(11) NOT NULL AUTO_INCREMENT,
  `descrizione` text NOT NULL,
  `nome` varchar(255) NOT NULL,
  PRIMARY KEY (`idPagamento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbpagamento: ~0 rows (circa)
DELETE FROM `tbpagamento`;

-- Dump della struttura di tabella km-0.tbrecensione
DROP TABLE IF EXISTS `tbrecensione`;
CREATE TABLE IF NOT EXISTS `tbrecensione` (
  `idRecensione` int(11) NOT NULL AUTO_INCREMENT,
  `recensione` text NOT NULL,
  `valutazione` int(11) NOT NULL,
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`idRecensione`),
  KEY `FK_tbrecensione_idCliente_tbcliente_idCliente` (`idCliente`),
  CONSTRAINT `FK_tbrecensione_idCliente_tbcliente_idCliente` FOREIGN KEY (`idCliente`) REFERENCES `tbcliente` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbrecensione: ~0 rows (circa)
DELETE FROM `tbrecensione`;

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

-- Dump della struttura di tabella km-0.tbsirivolgea
DROP TABLE IF EXISTS `tbsirivolgea`;
CREATE TABLE IF NOT EXISTS `tbsirivolgea` (
  `idServizio` int(11) NOT NULL,
  `idOrdine` int(11) NOT NULL,
  PRIMARY KEY (`idServizio`,`idOrdine`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbsirivolgea: ~0 rows (circa)
DELETE FROM `tbsirivolgea`;

-- Dump della struttura di tabella km-0.tbsistabiliscein
DROP TABLE IF EXISTS `tbsistabiliscein`;
CREATE TABLE IF NOT EXISTS `tbsistabiliscein` (
  `idVenditore` int(11) NOT NULL,
  `idUbicazione` int(11) NOT NULL,
  PRIMARY KEY (`idVenditore`,`idUbicazione`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbsistabiliscein: ~0 rows (circa)
DELETE FROM `tbsistabiliscein`;

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
  `telefono` varchar(14) NOT NULL,
  `idCredential` int(11) NOT NULL,
  PRIMARY KEY (`idVenditore`),
  KEY `codCredential` (`idCredential`) USING BTREE,
  CONSTRAINT `FK_tbvenditore_idCredential_tbcredential_idCredential` FOREIGN KEY (`idCredential`) REFERENCES `tbcredential` (`idCredential`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella km-0.tbvenditore: ~0 rows (circa)
DELETE FROM `tbvenditore`;

-- Dump della struttura di vista km-0.vwadmin
DROP VIEW IF EXISTS `vwadmin`;
-- Creazione di una tabella temporanea per risolvere gli errori di dipendenza della vista
CREATE TABLE `vwadmin` (
	`idCredential` INT(11) NOT NULL,
	`email` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`pswd` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`attivo` TINYINT(1) NULL
) ENGINE=MyISAM;

-- Dump della struttura di vista km-0.vwcliente
DROP VIEW IF EXISTS `vwcliente`;
-- Creazione di una tabella temporanea per risolvere gli errori di dipendenza della vista
CREATE TABLE `vwcliente` (
	`idCliente` INT(11) NOT NULL,
	`citta` VARCHAR(34) NOT NULL COLLATE 'latin1_swedish_ci',
	`provincia` VARCHAR(34) NOT NULL COLLATE 'latin1_swedish_ci',
	`via` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`nome` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`cognome` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`CF` VARCHAR(16) NOT NULL COLLATE 'latin1_swedish_ci',
	`telefono` VARCHAR(14) NOT NULL COLLATE 'latin1_swedish_ci',
	`email` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`pswd` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`attivo` TINYINT(1) NULL
) ENGINE=MyISAM;

-- Dump della struttura di vista km-0.vwvenditore
DROP VIEW IF EXISTS `vwvenditore`;
-- Creazione di una tabella temporanea per risolvere gli errori di dipendenza della vista
CREATE TABLE `vwvenditore` (
	`idVenditore` INT(11) NOT NULL,
	`sitoweb` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`partitaIVA` INT(11) NOT NULL,
	`ragioneSociale` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`CF` VARCHAR(16) NOT NULL COLLATE 'latin1_swedish_ci',
	`telefono` VARCHAR(14) NOT NULL COLLATE 'latin1_swedish_ci',
	`email` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`pswd` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`attivo` TINYINT(1) NULL
) ENGINE=MyISAM;

-- Rimozione temporanea di tabella e creazione della struttura finale della vista
DROP TABLE IF EXISTS `vwcliente`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vwcliente` AS select `tbcliente`.`idCliente` AS `idCliente`,`tbcliente`.`citta` AS `citta`,`tbcliente`.`provincia` AS `provincia`,`tbcliente`.`via` AS `via`,`tbcliente`.`nome` AS `nome`,`tbcliente`.`cognome` AS `cognome`,`tbcliente`.`CF` AS `CF`,`tbcliente`.`telefono` AS `telefono`,`tbcredential`.`email` AS `email`,`tbcredential`.`pswd` AS `pswd`,`tbcredential`.`attivo` AS `attivo` from (`tbcliente` join `tbcredential` on(`tbcredential`.`idCredential` = `tbcliente`.`idCredential`));

-- Rimozione temporanea di tabella e creazione della struttura finale della vista
DROP TABLE IF EXISTS `vwvenditore`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vwvenditore` AS select `tv`.`idVenditore` AS `idVenditore`,`tv`.`sitoweb` AS `sitoweb`,`tv`.`partitaIVA` AS `partitaIVA`,`tv`.`ragioneSociale` AS `ragioneSociale`,`tv`.`CF` AS `CF`,`tv`.`telefono` AS `telefono`,`tc`.`email` AS `email`,`tc`.`pswd` AS `pswd`,`tc`.`attivo` AS `attivo` from (`tbvenditore` `tv` join `tbcredential` `tc` on(`tv`.`idCredential` = `tc`.`idCredential`));

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;