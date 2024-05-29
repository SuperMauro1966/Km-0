-- Dump dei dati della tabella km-0.tbcredential: ~7 rows (circa)
-- DELETE FROM `tbcredential`;
INSERT INTO `tbcredential` (`idCredential`, `pswd`, `email`, `attivo`) VALUES
	(3, '5678', 'Pippo', 1),
	(4, '5678', 'Pluto', 1),
	(5, '10', 'Paperino', 0),
	(6, '11', 'Topolino', 0),
	(7, '12', 'Pluto2', 0);

-- Dump dei dati della tabella km-0.tbcliente: ~1 rows (circa)
DELETE FROM `tbcliente`;
INSERT INTO `tbcliente` (`idCliente`, `citta`, `provincia`, `via`, `nome`, `cognome`, `CF`, `telefono`, `idCredential`) VALUES
	(1, 'Imola', 'BO', 'Via della liberazione', 'Mario', 'Rossi', 'AAA', '+39', 3),
	(2, 'Imola', 'BO', 'Via della liberazione', 'Mario', 'Rossi', 'AAA', '+39', 5);

-- Dump dei dati della tabella km-0.tbvenditore: ~2 rows (circa)
DELETE FROM `tbvenditore`;
INSERT INTO `tbvenditore` (`idVenditore`, `sitoweb`, `partitaIVA`, `ragioneSociale`, `CF`, `idCredential`) VALUES
	(1, 'www.disney.it', 10, 'Topolino', 'BBB', 4),
	(2, 'www.disney.it', 10, 'Topolino', 'BBB', 6);







