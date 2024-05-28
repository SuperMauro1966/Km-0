-- Dump dei dati della tabella km-0.tbcliente: ~1 rows (circa)
DELETE FROM `tbcliente`;
INSERT INTO `tbcliente` (`idCliente`, `citta`, `provincia`, `via`, `nome`, `cognome`, `CF`, `telefono`, `idCredential`) VALUES
	(1, 'Imola', 'BO', 'Via della liberazione', 'Mario', 'Rossi', 'AAA', '+39', 3);

INSERT INTO `tbcredential` (`idCredential`, `pswd`, `email`) VALUES
	(3, '5678', 'Pippo'),
	(4, '5678', 'Pluto');

-- Dump dei dati della tabella km-0.tbvenditore: ~1 rows (circa)
DELETE FROM `tbvenditore`;
INSERT INTO `tbvenditore` (`idVenditore`, `sitoweb`, `partitaIVA`, `ragioneSociale`, `CF`, `idCredential`) VALUES
	(1, 'www.disney.it', 10, 'Topolino', 'BBB', 4);