-- ============================================================
--  Total: 980 figuritas | 48 equipos | 19 especiales FWC | 14 Coca-Cola
--  Generado para el proyecto AlbumMind
-- ============================================================
--  ESTRUCTURA DEL ÁLBUM:
--  • FWC 00 + FWC1–FWC8   : Introducción (Emblema, Mascotas, Sede) — 9 especiales
--  • Equipos (48 × 20)    : 960 figuritas de equipo
--      Cada equipo:  X1 = Escudo | X13 = Foto equipo | X2–X12, X14–X20 = Jugadores
--  • FWC9–FWC19           : FIFA Museum / Historia del Mundial — 11 especiales FOIL
--  • CC1–CC14             : Coca-Cola
-- ============================================================
PRAGMA foreign_keys = ON;
-- ============================================================
-- 1. PÁGINAS
-- ============================================================
-- Páginas de inicio / especiales FWC
INSERT OR IGNORE INTO PAGINA (numPagina) VALUES (0),(1),(2),(3);
-- Páginas de equipos: 2 páginas por equipo × 48 equipos
INSERT OR IGNORE INTO PAGINA (numPagina) VALUES (8),(9),(10),(11),(12),(13),(14),(15),(16),
(17),(18),(19),(20),(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),
(35),(36),(37),(38),(39),(40),(41),(42),(43),(44),(45),(46),(47),(48),(49),(50),(51),(52),
(53),(54),(55),(58),(59),(60),(61),(62),(63),(64),(65),(66),(67),(68),(69),(70),(71),(72),
(73),(74),(75),(76),(77),(78),(79),(80),(81),(82),(83),(84),(85),(86),(87),(88),(89),(90),
(91),(92),(93),(94),(95),(96),(97),(98),(99),(100),(101),(102),(103),(104),(105);
-- Páginas de cierre / especiales FWC 
INSERT OR IGNORE INTO PAGINA (numPagina) VALUES (106),(107),(108),(109);
-- Páginas de Coca-Cola / especiales CC
INSERT OR IGNORE INTO PAGINA (numPagina) VALUES (110),(111);
-- ============================================================
-- 2. PEXTRA (páginas especiales)
-- ============================================================
INSERT OR IGNORE INTO PEXTRA (numPagina, seccion) VALUES
(0, 'Sección Especial introductoria'),
(1, 'Sección Especial introductoria'),
(2, 'Sección Especial introductoria'),
(3, 'Sección Especial introductoria'),
(106, 'Sección Especial de conclusión'),
(107, 'Sección Especial de conclusión'),
(108, 'Sección Especial de conclusión'),
(109, 'Sección Especial de conclusión'),
(110, 'Sección Especial de Coca-Cola'),
(111, 'Sección Especial de Coca-Cola');
-- ============================================================
-- 3. PAÍSES (48 equipos + código ISO-3)
-- ============================================================
INSERT OR IGNORE INTO PAIS (codPais, nombre) VALUES
('MEX', 'Mexico'),
('RSA', 'South Africa'),
('KOR', 'Korea Republic'),
('CZE', 'Czechia'),
('CAN', 'Canada'),
('BIH', 'Bosnia-Herzegovina'),
('QAT', 'Qatar'),
('SUI', 'Switzerland'),
('BRA', 'Brazil'),
('MAR', 'Morocco'),
('HAI', 'Haiti'),
('SCO', 'Scotland'),
('USA', 'USA'),
('PAR', 'Paraguay'),
('AUS', 'Australia'),
('TUR', 'Turkiye'),
('GER', 'Germany'),
('CUW', 'Curacao'),
('CIV', 'Cote d´Ivoire'),
('ECU', 'Ecuador'),
('NED', 'Netherlands'),
('JPN', 'Japan'),
('SWE', 'Sweden'),
('TUN', 'Tunisia'),
('BEL', 'Belgium'),
('EGY', 'Egypt'),
('IRN', 'IR Iran'),
('NZL', 'New Zealand'),
('ESP', 'Spain'),
('CPV', 'Cabo Verde'),
('KSA', 'Saudi Arabia'),
('URU', 'Uruguay'),
('FRA', 'France'),
('SEN', 'Senegal'),
('IRQ', 'Iraq'),
('NOR', 'Norway'),
('ARG', 'Argentina'),
('ALG', 'Algeria'),
('AUT', 'Austria'),
('JOR', 'Jordan'),
('POR', 'Portugal'),
('COD', 'Congo DR'),
('UZB', 'Uzbekistan'),
('COL', 'Colombia'),
('ENG', 'England'),
('CRO', 'Croatia'),
('GHA', 'Ghana'),
('PAN', 'Panama');
-- ============================================================
-- 4. PEQUIPO (2 páginas por equipo)
-- ============================================================
INSERT OR IGNORE INTO PEQUIPO (numPagina, codPais) VALUES
(8,'MEX'),(9,'MEX'),
(10,'RSA'),(11,'RSA'),
(12,'KOR'),(13,'KOR'),
(14,'CZE'),(15,'CZE'),
(16,'CAN'),(17,'CAN'),
(18,'BIH'),(19,'BIH'),
(20,'QAT'),(21,'QAT'),
(22,'SUI'),(23,'SUI'),
(24,'BRA'),(25,'BRA'),
(26,'MAR'),(27,'MAR'),
(28,'HAI'),(29,'HAI'),
(30,'SCO'),(31,'SCO'),
(32,'USA'),(33,'USA'),
(34,'PAR'),(35,'PAR'),
(36,'AUS'),(37,'AUS'),
(38,'TUR'),(39,'TUR'),
(40,'GER'),(41,'GER'),
(42,'CUW'),(43,'CUW'),
(44,'CIV'),(45,'CIV'),
(46,'ECU'),(47,'ECU'),
(48,'NED'),(49,'NED'),
(50,'JPN'),(51,'JPN'),
(52,'SWE'),(53,'SWE'),
(54,'TUN'),(55,'TUN'),
(58,'BEL'),(59,'BEL'),
(60,'EGY'),(61,'EGY'),
(62,'IRN'),(63,'IRN'),
(64,'NZL'),(65,'NZL'),
(66,'ESP'),(67,'ESP'),
(68,'CPV'),(69,'CPV'),
(70,'KSA'),(71,'KSA'),
(72,'URU'),(73,'URU'),
(74,'FRA'),(75,'FRA'),
(76,'SEN'),(77,'SEN'),
(78,'IRQ'),(79,'IRQ'),
(80,'NOR'),(81,'NOR'),
(82,'ARG'),(83,'ARG'),
(84,'ALG'),(85,'ALG'),
(86,'AUT'),(87,'AUT'),
(88,'JOR'),(89,'JOR'),
(90,'POR'),(91,'POR'),
(92,'COD'),(93,'COD'),
(94,'UZB'),(95,'UZB'),
(96,'COL'),(97,'COL'),
(98,'ENG'),(99,'ENG'),
(100,'CRO'),(101,'CRO'),
(102,'GHA'),(103,'GHA'),
(104,'PAN'),(105,'PAN');
-- ============================================================
-- 5. FIGURITAS + FJUGADOR / FESPECIAL
-- ============================================================
INSERT OR IGNORE INTO PAIS (codPais, nombre) VALUES ('FWC', 'FIFA World Cup — Especial');
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(0,'FWC',0),(1,'FWC',1),(2,'FWC',1),(3,'FWC',1),(4,'FWC',1),
(5,'FWC',2),(6,'FWC',2),(7,'FWC',3),(8,'FWC',3);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES
(0,'FWC','Panini Logo'),
(1,'FWC','Emblema Oficial'),
(2,'FWC','Emblema Oficial'),
(3,'FWC','Mascotas Oficiales'),
(4,'FWC','Eslogan Oficial'),
(5,'FWC','Balón Oficial'),
(6,'FWC','Canadá'),
(7,'FWC','México'),
(8,'FWC','USA');
-- ─────────────────────────────────────────────
-- MACRO SECCIÓN: EQUIPOS DEL MUNDIAL
-- ─────────────────────────────────────────────
-- ------------------------------------------------------------
-- GRUPO A
-- ------------------------------------------------------------
-- ============================================================
-- MÉXICO (MEX)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'MEX',8),(2,'MEX',8),(3,'MEX',8),(4,'MEX',8),(5,'MEX',8),(6,'MEX',8),
(7,'MEX',8),(8,'MEX',8),(9,'MEX',8),(10,'MEX',8),(11,'MEX',9),(12,'MEX',9),
(13,'MEX',9),(14,'MEX',9),(15,'MEX',9),(16,'MEX',9),(17,'MEX',9),(18,'MEX',9),
(19,'MEX',9),(20,'MEX',9);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'MEX','Escudo FOIL'),(13,'MEX','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'MEX','Luis','Malagón'),(3,'MEX','Johan','Vasquez'),
(4,'MEX','Jorge','Sánchez'),(5,'MEX','Cesar','Montes'),
(6,'MEX','Jesus','Gallardo'),(7,'MEX','Israel','Reyes'),
(8,'MEX','Diego','Lainez'),(9,'MEX','Carlos','Rodriguez'),
(10,'MEX','Edson','Alvarez'),(11,'MEX','Orbelin','Pineda'),
(12,'MEX','Marcel','Ruiz'),(14,'MEX','Érick','Sánchez'),
(15,'MEX','Hirving','Lozano'),(16,'MEX','Santiago','Giménez'),
(17,'MEX','Raúl','Jiménez'),(18,'MEX','Alexis','Vega'),
(19,'MEX','Roberto','Alvarado'),(20,'MEX','Cesar','Huerta');
-- ============================================================
-- SUDÁFRICA (RSA)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'RSA',10),(2,'RSA',10),(3,'RSA',10),(4,'RSA',10),(5,'RSA',10),(6,'RSA',10),
(7,'RSA',10),(8,'RSA',10),(9,'RSA',10),(10,'RSA',10),(11,'RSA',11),(12,'RSA',11),
(13,'RSA',11),(14,'RSA',11),(15,'RSA',11),(16,'RSA',11),(17,'RSA',11),(18,'RSA',11),
(19,'RSA',11),(20,'RSA',11);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'RSA','Escudo FOIL'),(13,'RSA','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'RSA','Ronwen','Williams'),(3,'RSA','Sipho','Chaine'),
(4,'RSA','Aubrey','Modiba'),(5,'RSA','Samukele','Kabini'),
(6,'RSA','Mbekezeli','Mbokazi'),(7,'RSA','Khulumani','Ndamane'),
(8,'RSA','Siyabonga','Ngezana'),(9,'RSA','Khuliso','Mudau'),
(10,'RSA','Nkosinathi','Sibisi'),(11,'RSA','Teboho','Mokoena'),
(12,'RSA','Thalente','Mbatha'),(14,'RSA','Bathusi','Aubaas'),
(15,'RSA','Yaya','Sithole'),(16,'RSA','Sipho','Mbule'),
(17,'RSA','Lyle','Foster'),(18,'RSA','Iqraam','Rayners'),
(19,'RSA','Mohau','Nkota'),(20,'RSA','Oswin','Appollis');
-- ============================================================
-- KOREA REPUBLIC (KOR)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'KOR',12),(2,'KOR',12),(3,'KOR',12),(4,'KOR',12),(5,'KOR',12),(6,'KOR',12),
(7,'KOR',12),(8,'KOR',12),(9,'KOR',12),(10,'KOR',12),(11,'KOR',13),(12,'KOR',13),
(13,'KOR',13),(14,'KOR',13),(15,'KOR',13),(16,'KOR',13),(17,'KOR',13),(18,'KOR',13),
(19,'KOR',13),(20,'KOR',13);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'KOR','Escudo FOIL'),(13,'KOR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'KOR','Hyeonwoo','Jo'),(3,'KOR','Seunggyu','Kim'),
(4,'KOR','Minjae','Kim'),(5,'KOR','Yumin','Cho'),
(6,'KOR','Youngwoo','Seol'),(7,'KOR','Hanbeom','Lee'),
(8,'KOR','Taeseok','Lee'),(9,'KOR','Myungjae','Lee'),
(10,'KOR','Jaesung','Lee'),(11,'KOR','Inbeom','Hwang'),
(12,'KOR','Kangin','Lee'),(14,'KOR','Seungho','Paik'),
(15,'KOR','Jens','Castrop'),(16,'KOR','Donggyeong','Lee'),
(17,'KOR','Guesung','Cho'),(18,'KOR','Heungmin','Son'),
(19,'KOR','Heechan','Hwang'),(20,'KOR','Hyeongyu','Oh');
-- ============================================================
-- CZECHIA (CZE)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'CZE',14),(2,'CZE',14),(3,'CZE',14),(4,'CZE',14),(5,'CZE',14),(6,'CZE',14),
(7,'CZE',14),(8,'CZE',14),(9,'CZE',14),(10,'CZE',14),(11,'CZE',15),(12,'CZE',15),
(13,'CZE',15),(14,'CZE',15),(15,'CZE',15),(16,'CZE',15),(17,'CZE',15),(18,'CZE',15),
(19,'CZE',15),(20,'CZE',15);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'CZE','Escudo FOIL'),(13,'CZE','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'CZE','Matěj','Kovář'),(3,'CZE','Jindřich','Staněk'),
(4,'CZE','Ladislav','Krejčí'),(5,'CZE','Vladimír','Coufal'),
(6,'CZE','Jaroslav','Zelený'),(7,'CZE','Tomáš','Holeš'),
(8,'CZE','David','Zima'),(9,'CZE','Michal','Sadílek'),
(10,'CZE','Lukáš','Provod'),(11,'CZE','Lukáš','Červ'),
(12,'CZE','Tomáš','Souček'),(14,'CZE','Pavel','Šulc'),
(15,'CZE','Matěj','Vydra'),(16,'CZE','Vasil','Kušej'),
(17,'CZE','Tomáš','Chorý'),(18,'CZE','Václav','Černý'),
(19,'CZE','Adam','Hložek'),(20,'CZE','Patrik','Schick');
-- ------------------------------------------------------------
-- GRUPO B
-- ------------------------------------------------------------
-- ============================================================
-- CANADA (CAN)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'CAN',16),(2,'CAN',16),(3,'CAN',16),(4,'CAN',16),(5,'CAN',16),(6,'CAN',16),
(7,'CAN',16),(8,'CAN',16),(9,'CAN',16),(10,'CAN',16),(11,'CAN',17),(12,'CAN',17),
(13,'CAN',17),(14,'CAN',17),(15,'CAN',17),(16,'CAN',17),(17,'CAN',17),(18,'CAN',17),
(19,'CAN',17),(20,'CAN',17);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'CAN','Escudo FOIL'),(13,'CAN','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'CAN','Dayne','St. Clair'),(3,'CAN','Alphonso','Davies'),
(4,'CAN','Alistair','Johnston'),(5,'CAN','Samuel','Adekugbe'),
(6,'CAN','Richie','Laryea'),(7,'CAN','Derek','Cornelius'),
(8,'CAN','Moïse','Bombito'),(9,'CAN','Kamal','Miller'),
(10,'CAN','Stephen','Eustáquio'),(11,'CAN','Ismaël','Koné'),
(12,'CAN','Jonathan','Osorio'),(14,'CAN','Jacob','Shaffelburg'),
(15,'CAN','Mathieu','Choinière'),(16,'CAN','Niko','Sigur'),
(17,'CAN','Tajon','Buchanan'),(18,'CAN','Liam','Millar'),
(19,'CAN','Cyle','Larin'),(20,'CAN','Jonathan','David');
-- ============================================================
-- BOSNIA-HERZEGOVINA (BIH) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'BIH',18),(2,'BIH',18),(3,'BIH',18),(4,'BIH',18),(5,'BIH',18),(6,'BIH',18),
(7,'BIH',18),(8,'BIH',18),(9,'BIH',18),(10,'BIH',18),(11,'BIH',19),(12,'BIH',19),
(13,'BIH',19),(14,'BIH',19),(15,'BIH',19),(16,'BIH',19),(17,'BIH',19),(18,'BIH',19),
(19,'BIH',19),(20,'BIH',19);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'BIH','Escudo FOIL'),(13,'BIH','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'BIH','Nikola','Vasilj'),(3,'BIH','Amar','Dedić'),
(4,'BIH','Sead','Kolašinac'),(5,'BIH','Tarik','Muharemović'),
(6,'BIH','Nihad','Mujakić'),(7,'BIH','Nikola','Katić'),
(8,'BIH','Amir','Hadžiahmetović'),(9,'BIH','Benjamin','Tahirović'),
(10,'BIH','Armin','Gigović'),(11,'BIH','Ivan','Šunjić'),
(12,'BIH','Ivan','Bašić'),(14,'BIH','Dženis','Burnić'),
(15,'BIH','Esmir','Bajraktarević'),(16,'BIH','Amar','Memić'),
(17,'BIH','Ermedin','Demirović'),(18,'BIH','Edin','Džeko'),
(19,'BIH','Samed','Baždar'),(20,'BIH','Haris','Tabaković');
-- ============================================================
-- QATAR (QAT)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'QAT',20),(2,'QAT',20),(3,'QAT',20),(4,'QAT',20),(5,'QAT',20),(6,'QAT',20),
(7,'QAT',20),(8,'QAT',20),(9,'QAT',20),(10,'QAT',20),(11,'QAT',21),(12,'QAT',21),
(13,'QAT',21),(14,'QAT',21),(15,'QAT',21),(16,'QAT',21),(17,'QAT',21),(18,'QAT',21),
(19,'QAT',21),(20,'QAT',21);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'QAT','Escudo FOIL'),(13,'QAT','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'QAT','Meshaal','Barsham'),(3,'QAT','Sultan','Albrake'),
(4,'QAT','Lucas','Mendes'),(5,'QAT','Homam','Ahmed'),
(6,'QAT','Boualem','Khoukhi'),(7,'QAT','Pedro','Miguel'),
(8,'QAT','Tarek','Salman'),(9,'QAT','Mohammed','Mannai'),
(10,'QAT','Karim','Boudiaf'),(11,'QAT','Assim','Madibo'),
(12,'QAT','Hamed','Fatehi'),(14,'QAT','Mohammed','Waad'),
(15,'QAT','Abdulaziz','Hatem'),(16,'QAT','Hassan','Al-Haydos'),
(17,'QAT','Edmílson','Junior'),(18,'QAT','Akram Hassan','Afif'),
(19,'QAT','Ahmed','Al-Ganehi'),(20,'QAT','Almoez','Ali');
-- ============================================================
-- SWITZERLAND (SUI)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'SUI',22),(2,'SUI',22),(3,'SUI',22),(4,'SUI',22),(5,'SUI',22),(6,'SUI',22),
(7,'SUI',22),(8,'SUI',22),(9,'SUI',22),(10,'SUI',22),(11,'SUI',23),(12,'SUI',23),
(13,'SUI',23),(14,'SUI',23),(15,'SUI',23),(16,'SUI',23),(17,'SUI',23),(18,'SUI',23),
(19,'SUI',23),(20,'SUI',23);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'SUI','Escudo FOIL'),(13,'SUI','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'SUI','Gregor','Kobel'),(3,'SUI','Yvon','Mvogo'),
(4,'SUI','Manuel','Akanji'),(5,'SUI','Ricardo','Rodríguez'),
(6,'SUI','Nico','Elvedi'),(7,'SUI','Aurèle','Amenda'),
(8,'SUI','Silvan','Widmer'),(9,'SUI','Granit','Xhaka'),
(10,'SUI','Denis','Zakaria'),(11,'SUI','Remo','Freuler'),
(12,'SUI','Fabian','Rieder'),(14,'SUI','Ardon','Jashari'),
(15,'SUI','Johan','Manzambi'),(16,'SUI','Michel','Aebischer'),
(17,'SUI','Breel','Embolo'),(18,'SUI','Rubén','Vargas'),
(19,'SUI','Dan','Ndoye'),(20,'SUI','Zeki','Amdouni');
-- ------------------------------------------------------------
-- GRUPO C
-- ------------------------------------------------------------
-- ============================================================
-- BRASIL (BRA)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'BRA',24),(2,'BRA',24),(3,'BRA',24),(4,'BRA',24),(5,'BRA',24),(6,'BRA',24),
(7,'BRA',24),(8,'BRA',24),(9,'BRA',24),(10,'BRA',24),(11,'BRA',25),(12,'BRA',25),
(13,'BRA',25),(14,'BRA',25),(15,'BRA',25),(16,'BRA',25),(17,'BRA',25),(18,'BRA',25),
(19,'BRA',25),(20,'BRA',25);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'BRA','Escudo FOIL'),(13,'BRA','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'BRA','Bento',NULL),(3,'BRA','Alisson',NULL),
(4,'BRA','Danilo',NULL),(5,'BRA','Marquinhos',NULL),
(6,'BRA','Éder','Militão'),(7,'BRA','Gabriel','Magalhães'),
(8,'BRA','Wesley',NULL),(9,'BRA','Lucas','Paquetá'),
(10,'BRA','Casemiro',NULL),(11,'BRA','Bruno','Guimarães'),
(12,'BRA','Luiz','Henrique'),(14,'BRA','Vinícius','Júnior'),
(15,'BRA','Rodrygo',NULL),(16,'BRA','João','Pedro'),
(17,'BRA','Matheus','Cunha'),(18,'BRA','Gabriel','Martinelli'),
(19,'BRA','Raphinha',NULL),(20,'BRA','Estêvão',NULL);
-- ============================================================
-- MOROCCO (MAR) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'MAR',26),(2,'MAR',26),(3,'MAR',26),(4,'MAR',26),(5,'MAR',26),(6,'MAR',26),
(7,'MAR',26),(8,'MAR',26),(9,'MAR',26),(10,'MAR',26),(11,'MAR',27),(12,'MAR',27),
(13,'MAR',27),(14,'MAR',27),(15,'MAR',27),(16,'MAR',27),(17,'MAR',27),(18,'MAR',27),
(19,'MAR',27),(20,'MAR',27);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'MAR','Escudo FOIL'),(13,'MAR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'MAR','Yassine','Bounou'),(3,'MAR','Munir','El Kajoui'),
(4,'MAR','Achraf','Hakimi'),(5,'MAR','Noussair','Mazraoui'),
(6,'MAR','Nayef','Aguerd'),(7,'MAR','Romain','Saïss'),
(8,'MAR','Jawad','El Yamiq'),(9,'MAR','Adam','Masina'),
(10,'MAR','Sofyan','Amrabat'),(11,'MAR','Azzedine','Ounahi'),
(12,'MAR','Eliesse','Ben Seghir'),(14,'MAR','Bilal','El Khannouss'),
(15,'MAR','Ismael','Saibari'),(16,'MAR','Youssef','En-Nesyri'),
(17,'MAR','Abde','Ezzalzouli'),(18,'MAR','Soufiane','Rahimi'),
(19,'MAR','Brahim','Díaz'),(20,'MAR','Ayoub','El Kaabi');
-- ============================================================
-- HAITÍ (HAI)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'HAI',28),(2,'HAI',28),(3,'HAI',28),(4,'HAI',28),(5,'HAI',28),(6,'HAI',28),
(7,'HAI',28),(8,'HAI',28),(9,'HAI',28),(10,'HAI',28),(11,'HAI',29),(12,'HAI',29),
(13,'HAI',29),(14,'HAI',29),(15,'HAI',29),(16,'HAI',29),(17,'HAI',29),(18,'HAI',29),
(19,'HAI',29),(20,'HAI',29);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'HAI','Escudo FOIL'),(13,'HAI','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'HAI','Johny','Placide'),(3,'HAI','Carlens','Arcus'),
(4,'HAI','Martin','Expérience'),(5,'HAI','Jean-Kévin','Duverne'),
(6,'HAI','Ricardo','Adé'),(7,'HAI','Duke','Lacroix'),
(8,'HAI','Garven','Metusala'),(9,'HAI','Hannes','Delcroix'),
(10,'HAI','Leverton','Pierre'),(11,'HAI','Danley','Jean Jacques'),
(12,'HAI','Jean-Ricner','Bellegarde'),(14,'HAI','Christopher','Attys'),
(15,'HAI','Derrick','Etienne Jr.'),(16,'HAI','Josué','Casimir'),
(17,'HAI','Ruben','Providence'),(18,'HAI','Duckens','Nazon'),
(19,'HAI','Louicius','Deedson'),(20,'HAI','Frantzdy','Pierrot');
-- ============================================================
-- SCOTLAND (SCO)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'SCO',30),(2,'SCO',30),(3,'SCO',30),(4,'SCO',30),(5,'SCO',30),(6,'SCO',30),
(7,'SCO',30),(8,'SCO',30),(9,'SCO',30),(10,'SCO',30),(11,'SCO',31),(12,'SCO',31),
(13,'SCO',31),(14,'SCO',31),(15,'SCO',31),(16,'SCO',31),(17,'SCO',31),(18,'SCO',31),
(19,'SCO',31),(20,'SCO',31);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'SCO','Escudo FOIL'),(13,'SCO','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'SCO','Angus','Gunn'),(3,'SCO','Jack','Hendry'),
(4,'SCO','Kieran','Tierney'),(5,'SCO','Aaron','Hickey'),
(6,'SCO','Andrew','Robertson'),(7,'SCO','Scott','McKenna'),
(8,'SCO','John','Souttar'),(9,'SCO','Anthony','Ralston'),
(10,'SCO','Grant','Hanley'),(11,'SCO','Scott','McTominay'),
(12,'SCO','Billy','Gilmour'),(14,'SCO','Lewis','Ferguson'),
(15,'SCO','Ryan','Christie'),(16,'SCO','Kenny','McLean'),
(17,'SCO','John','McGinn'),(18,'SCO','Lyndon','Dykes'),
(19,'SCO','Ché','Adams'),(20,'SCO','Ben','Gannon-Doak');
-- ------------------------------------------------------------
-- GRUPO D
-- ------------------------------------------------------------
-- ============================================================
-- ESTADOS UNIDOS (USA)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'USA',32),(2,'USA',32),(3,'USA',32),(4,'USA',32),(5,'USA',32),(6,'USA',32),
(7,'USA',32),(8,'USA',32),(9,'USA',32),(10,'USA',32),(11,'USA',33),(12,'USA',33),
(13,'USA',33),(14,'USA',33),(15,'USA',33),(16,'USA',33),(17,'USA',33),(18,'USA',33),
(19,'USA',33),(20,'USA',33);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'USA','Escudo FOIL'),(13,'USA','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'USA','Matt','Freese'),(3,'USA','Chris','Richards'),
(4,'USA','Tim','Ream'),(5,'USA','Mark','McKenzie'),
(6,'USA','Alex','Freeman'),(7,'USA','Antonee','Robinson'),
(8,'USA','Tyler','Adams'),(9,'USA','Tanner','Tessmann'),
(10,'USA','Weston','McKennie'),(11,'USA','Cristian','Roldan'),
(12,'USA','Timothy','Weah'),(14,'USA','Diego','Luna'),
(15,'USA','Malik','Tillman'),(16,'USA','Christian','Pulisic'),
(17,'USA','Brenden','Aaronson'),(18,'USA','Ricardo','Pepi'),
(19,'USA','Haji','Wright'),(20,'USA','Folarin','Balogun');
-- ============================================================
-- PARAGUAY (PAR)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'PAR',34),(2,'PAR',34),(3,'PAR',34),(4,'PAR',34),(5,'PAR',34),(6,'PAR',34),
(7,'PAR',34),(8,'PAR',34),(9,'PAR',34),(10,'PAR',34),(11,'PAR',35),(12,'PAR',35),
(13,'PAR',35),(14,'PAR',35),(15,'PAR',35),(16,'PAR',35),(17,'PAR',35),(18,'PAR',35),
(19,'PAR',35),(20,'PAR',35);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'PAR','Escudo FOIL'),(13,'PAR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'PAR','Roberto','Fernández'),(3,'PAR','Orlando','Gill'),
(4,'PAR','Gustavo','Gómez'),(5,'PAR','Fabián','Balbuena'),
(6,'PAR','Juan José','Cáceres'),(7,'PAR','Omar','Alderete'),
(8,'PAR','Júnior','Alonso'),(9,'PAR','Mathías','Villasanti'),
(10,'PAR','Diego','Gómez'),(11,'PAR','Damián','Bobadilla'),
(12,'PAR','Andrés','Cubas'),(14,'PAR','Matías','Galarza Fonda'),
(15,'PAR','Julio','Enciso'),(16,'PAR','Alejandro','Romero Gamarra'),
(17,'PAR','Miguel','Almirón'),(18,'PAR','Ramón','Sosa'),
(19,'PAR','Ángel','Romero'),(20,'PAR','Antonio','Sanabria');
-- ============================================================
-- AUSTRALIA (AUS)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'AUS',36),(2,'AUS',36),(3,'AUS',36),(4,'AUS',36),(5,'AUS',36),(6,'AUS',36),
(7,'AUS',36),(8,'AUS',36),(9,'AUS',36),(10,'AUS',36),(11,'AUS',37),(12,'AUS',37),
(13,'AUS',37),(14,'AUS',37),(15,'AUS',37),(16,'AUS',37),(17,'AUS',37),(18,'AUS',37),
(19,'AUS',37),(20,'AUS',37);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'AUS','Escudo FOIL'),(13,'AUS','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'AUS','Mathew','Ryan'),(3,'AUS','Joe','Gauci'),
(4,'AUS','Harry','Souttar'),(5,'AUS','Alessandro','Circati'),
(6,'AUS','Jordan','Bos'),(7,'AUS','Aziz','Behich'),
(8,'AUS','Cameron','Burgess'),(9,'AUS','Lewis','Miller'),
(10,'AUS','Milos','Degenek'),(11,'AUS','Jackson','Irvine'),
(12,'AUS','Riley','McGree'),(14,'AUS','Aiden','O''Neill'),
(15,'AUS','Connor','Metcalfe'),(16,'AUS','Patrick','Vazbek'),
(17,'AUS','Craig','Goodwin'),(18,'AUS','Kusini','Yengi'),
(19,'AUS','Nestory','Irankunda'),(20,'AUS','Mohamed','Touré');
-- ============================================================
-- TÜRKIYE (TUR)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'TUR',38),(2,'TUR',38),(3,'TUR',38),(4,'TUR',38),(5,'TUR',38),(6,'TUR',38),
(7,'TUR',38),(8,'TUR',38),(9,'TUR',38),(10,'TUR',38),(11,'TUR',39),(12,'TUR',39),
(13,'TUR',39),(14,'TUR',39),(15,'TUR',39),(16,'TUR',39),(17,'TUR',39),(18,'TUR',39),
(19,'TUR',39),(20,'TUR',39);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'TUR','Escudo FOIL'),(13,'TUR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'TUR','Uğurcan','Çakır'),(3,'TUR','Mert','Müldür'),
(4,'TUR','Zeki','Çelik'),(5,'TUR','Abdülkerim','Bardakcı'),
(6,'TUR','Çağlar','Söyüncü'),(7,'TUR','Merih','Demiral'),
(8,'TUR','Ferdi','Kadıoğlu'),(9,'TUR','Kaan','Ayhan'),
(10,'TUR','İsmail','Yüksek'),(11,'TUR','Hakan','Çalhanoğlu'),
(12,'TUR','Orkun','Kökçü'),(14,'TUR','Arda','Güler'),
(15,'TUR','İrfan Can','Kahveci'),(16,'TUR','Yunus','Akgün'),
(17,'TUR','Can','Uzun'),(18,'TUR','Barış Alper','Yılmaz'),
(19,'TUR','Kerem','Aktürkoğlu'),(20,'TUR','Kenan','Yıldız');
-- ------------------------------------------------------------
-- GRUPO E
-- ------------------------------------------------------------
-- ============================================================
-- GERMANY (GER)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'GER',40),(2,'GER',40),(3,'GER',40),(4,'GER',40),(5,'GER',40),(6,'GER',40),
(7,'GER',40),(8,'GER',40),(9,'GER',40),(10,'GER',40),(11,'GER',41),(12,'GER',41),
(13,'GER',41),(14,'GER',41),(15,'GER',41),(16,'GER',41),(17,'GER',41),(18,'GER',41),
(19,'GER',41),(20,'GER',41);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'GER','Escudo FOIL'),(13,'GER','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'GER','Marc-André','ter Stegen'),(3,'GER','Jonathan','Tah'),
(4,'GER','David','Raum'),(5,'GER','Nico','Schlotterbeck'),
(6,'GER','Antonio','Rüdiger'),(7,'GER','Waldemar','Anton'),
(8,'GER','Ridle','Baku'),(9,'GER','Maximilian','Mittelstädt'),
(10,'GER','Joshua','Kimmich'),(11,'GER','Florian','Wirtz'),
(12,'GER','Felix','Nmecha'),(14,'GER','Leon','Goretzka'),
(15,'GER','Jamal','Musiala'),(16,'GER','Serge','Gnabry'),
(17,'GER','Kai','Havertz'),(18,'GER','Leroy','Sané'),
(19,'GER','Karim','Adeyemi'),(20,'GER','Nick','Woltemade');
-- ============================================================
-- CURAÇAO (CUW)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'CUW',42),(2,'CUW',42),(3,'CUW',42),(4,'CUW',42),(5,'CUW',42),(6,'CUW',42),
(7,'CUW',42),(8,'CUW',42),(9,'CUW',42),(10,'CUW',42),(11,'CUW',43),(12,'CUW',43),
(13,'CUW',43),(14,'CUW',43),(15,'CUW',43),(16,'CUW',43),(17,'CUW',43),(18,'CUW',43),
(19,'CUW',43),(20,'CUW',43);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'CUW','Escudo FOIL'),(13,'CUW','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'CUW','Eloy','Room'),(3,'CUW','Armando','Obispo'),
(4,'CUW','Sherel','Floranus'),(5,'CUW','Juriën','Gaari'),
(6,'CUW','Joshua','Brenet'),(7,'CUW','Roshon','van Eijma'),
(8,'CUW','Shurandy','Sambo'),(9,'CUW','Livano','Comenencia'),
(10,'CUW','Godfried','Roemeratoe'),(11,'CUW','Juninho','Bacuna'),
(12,'CUW','Leandro','Bacuna'),(14,'CUW','Tahith','Chong'),
(15,'CUW','Kenji','Gorré'),(16,'CUW','Jearl','Margaritha'),
(17,'CUW','Jürgen','Locadia'),(18,'CUW','Jeremy','Antonisse'),
(19,'CUW','Gervane','Kastaneer'),(20,'CUW','Sontje','Hansen');
-- ============================================================
-- COSTA DE MARFIL (CIV)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'CIV',44),(2,'CIV',44),(3,'CIV',44),(4,'CIV',44),(5,'CIV',44),(6,'CIV',44),
(7,'CIV',44),(8,'CIV',44),(9,'CIV',44),(10,'CIV',44),(11,'CIV',45),(12,'CIV',45),
(13,'CIV',45),(14,'CIV',45),(15,'CIV',45),(16,'CIV',45),(17,'CIV',45),(18,'CIV',45),
(19,'CIV',45),(20,'CIV',45);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'CIV','Escudo FOIL'),(13,'CIV','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'CIV','Yahia','Fofana'),(3,'CIV','Ghislain','Konan'),
(4,'CIV','Wilfried','Singo'),(5,'CIV','Odilon','Kossounou'),
(6,'CIV','Evan','Ndicka'),(7,'CIV','Willy','Boly'),
(8,'CIV','Emmanuel','Agbadou'),(9,'CIV','Ousmane','Diomande'),
(10,'CIV','Franck','Kessié'),(11,'CIV','Seko','Fofana'),
(12,'CIV','Ibrahim','Sangaré'),(14,'CIV','Jean-Philippe','Gbamin'),
(15,'CIV','Amad','Diallo'),(16,'CIV','Sébastien','Haller'),
(17,'CIV','Simon','Adingra'),(18,'CIV','Van','Diomande'),
(19,'CIV','Evann','Guessand'),(20,'CIV','Oumar','Diakité');
-- ============================================================
-- ECUADOR (ECU)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'ECU',46),(2,'ECU',46),(3,'ECU',46),(4,'ECU',46),(5,'ECU',46),(6,'ECU',46),
(7,'ECU',46),(8,'ECU',46),(9,'ECU',46),(10,'ECU',46),(11,'ECU',47),(12,'ECU',47),
(13,'ECU',47),(14,'ECU',47),(15,'ECU',47),(16,'ECU',47),(17,'ECU',47),(18,'ECU',47),
(19,'ECU',47),(20,'ECU',47);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'ECU','Escudo FOIL'),(13,'ECU','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'ECU','Hernán','Galíndez'),(3,'ECU','Gonzalo','Valle'),
(4,'ECU','Piero','Hincapié'),(5,'ECU','Pervis','Estupiñán'),
(6,'ECU','Willian','Pacho'),(7,'ECU','Ángelo','Preciado'),
(8,'ECU','Joel','Ordóñez'),(9,'ECU','Moisés','Caicedo'),
(10,'ECU','Alan','Franco'),(11,'ECU','Kendry','Páez'),
(12,'ECU','Pedro','Vite'),(14,'ECU','John','Yeboah'),
(15,'ECU','Leonardo','Campana'),(16,'ECU','Gonzalo','Plata'),
(17,'ECU','Nilson','Angulo'),(18,'ECU','Alan','Minda'),
(19,'ECU','Kevin','Rodríguez'),(20,'ECU','Enner','Valencia');
-- ------------------------------------------------------------
-- GRUPO F
-- ------------------------------------------------------------
-- ============================================================
-- NETHERLANDS (NED)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'NED',48),(2,'NED',48),(3,'NED',48),(4,'NED',48),(5,'NED',48),(6,'NED',48),
(7,'NED',48),(8,'NED',48),(9,'NED',48),(10,'NED',48),(11,'NED',49),(12,'NED',49),
(13,'NED',49),(14,'NED',49),(15,'NED',49),(16,'NED',49),(17,'NED',49),(18,'NED',49),
(19,'NED',49),(20,'NED',49);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'NED','Escudo FOIL'),(13,'NED','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'NED','Bart','Verbruggen'),(3,'NED','Virgil','van Dijk'),
(4,'NED','Micky','van de Ven'),(5,'NED','Jurriën','Timber'),
(6,'NED','Denzel','Dumfries'),(7,'NED','Nathan','Aké'),
(8,'NED','Jeremie','Frimpong'),(9,'NED','Jan Paul','van Hecke'),
(10,'NED','Tijjani','Reijnders'),(11,'NED','Ryan','Gravenberch'),
(12,'NED','Teun','Koopmeiners'),(14,'NED','Frenkie','de Jong'),
(15,'NED','Xavi','Simons'),(16,'NED','Justin','Kluivert'),
(17,'NED','Memphis','Depay'),(18,'NED','Donyell','Malen'),
(19,'NED','Wout','Weghorst'),(20,'NED','Cody','Gakpo');
-- ============================================================
-- JAPAN (JPN)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'JPN',50),(2,'JPN',50),(3,'JPN',50),(4,'JPN',50),(5,'JPN',50),(6,'JPN',50),
(7,'JPN',50),(8,'JPN',50),(9,'JPN',50),(10,'JPN',50),(11,'JPN',51),(12,'JPN',51),
(13,'JPN',51),(14,'JPN',51),(15,'JPN',51),(16,'JPN',51),(17,'JPN',51),(18,'JPN',51),
(19,'JPN',51),(20,'JPN',51);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'JPN','Escudo FOIL'),(13,'JPN','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'JPN','Zion','Suzuki'),(3,'JPN','Henry Heroki','Mochizuki'),
(4,'JPN','Ayumu','Seko'),(5,'JPN','Junnosuke','Suzuki'),
(6,'JPN','Shogo','Taniguchi'),(7,'JPN','Tsuyoshi','Watanabe'),
(8,'JPN','Kaishu','Sano'),(9,'JPN','Yuki','Soma'),
(10,'JPN','Ao','Tanaka'),(11,'JPN','Daichi','Kamada'),
(12,'JPN','Takefusa','Kubo'),(14,'JPN','Ritsu','Doan'),
(15,'JPN','Keito','Nakamura'),(16,'JPN','Takumi','Minamino'),
(17,'JPN','Shuto','Machino'),(18,'JPN','Junya','Ito'),
(19,'JPN','Koki','Ogawa'),(20,'JPN','Ayase','Ueda');
-- ============================================================
-- SUECIA (SWE)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'SWE',52),(2,'SWE',52),(3,'SWE',52),(4,'SWE',52),(5,'SWE',52),(6,'SWE',52),
(7,'SWE',52),(8,'SWE',52),(9,'SWE',52),(10,'SWE',52),(11,'SWE',53),(12,'SWE',53),
(13,'SWE',53),(14,'SWE',53),(15,'SWE',53),(16,'SWE',53),(17,'SWE',53),(18,'SWE',53),
(19,'SWE',53),(20,'SWE',53);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'SWE','Escudo FOIL'),(13,'SWE','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'SWE','Viktor','Johansson'),(3,'SWE','Isak','Hien'),
(4,'SWE','Gabriel','Gudmundsson'),(5,'SWE','Emil','Holm'),
(6,'SWE','Victor Nilsson','Lindelöf'),(7,'SWE','Gustaf','Lagerbielke'),
(8,'SWE','Lucas','Bergvall'),(9,'SWE','Hugo','Larsson'),
(10,'SWE','Jesper','Karlström'),(11,'SWE','Yasin','Ayari'),
(12,'SWE','Mattias','Svanberg'),(14,'SWE','Daniel','Svensson'),
(15,'SWE','Ken','Sema'),(16,'SWE','Roony','Bardghji'),
(17,'SWE','Dejan','Kulusevski'),(18,'SWE','Anthony','Elanga'),
(19,'SWE','Alexander','Isak'),(20,'SWE','Viktor','Gyökeres');
-- ============================================================
-- TUNISIA (TUN)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'TUN',54),(2,'TUN',54),(3,'TUN',54),(4,'TUN',54),(5,'TUN',54),(6,'TUN',54),
(7,'TUN',54),(8,'TUN',54),(9,'TUN',54),(10,'TUN',54),(11,'TUN',55),(12,'TUN',55),
(13,'TUN',55),(14,'TUN',55),(15,'TUN',55),(16,'TUN',55),(17,'TUN',55),(18,'TUN',55),
(19,'TUN',55),(20,'TUN',55);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'TUN','Escudo FOIL'),(13,'TUN','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'TUN','Bechir','Ben Saïd'),(3,'TUN','Aymen','Dahmen'),
(4,'TUN','Yan','Valery'),(5,'TUN','Montassar','Talbi'),
(6,'TUN','Yassine','Meriah'),(7,'TUN','Ali','Abdi'),
(8,'TUN','Dylan','Bronn'),(9,'TUN','Ellyes','Skhiri'),
(10,'TUN','Aïssa','Laïdouni'),(11,'TUN','Ferjani','Sassi'),
(12,'TUN','Mohamed Ali','Ben Romdhane'),(14,'TUN','Hannibal','Mejbri'),
(15,'TUN','Elias','Achouri'),(16,'TUN','Elias','Saad'),
(17,'TUN','Hazem','Mastouri'),(18,'TUN','Ismaël','Gharbi'),
(19,'TUN','Sayfallah','Ltaief'),(20,'TUN','Naïm','Sliti');
-- ------------------------------------------------------------
-- GRUPO G
-- ------------------------------------------------------------
-- ============================================================
-- BELGIUM (BEL)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'BEL',58),(2,'BEL',58),(3,'BEL',58),(4,'BEL',58),(5,'BEL',58),(6,'BEL',58),
(7,'BEL',58),(8,'BEL',58),(9,'BEL',58),(10,'BEL',58),(11,'BEL',59),(12,'BEL',59),
(13,'BEL',59),(14,'BEL',59),(15,'BEL',59),(16,'BEL',59),(17,'BEL',59),(18,'BEL',59),
(19,'BEL',59),(20,'BEL',59);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'BEL','Escudo FOIL'),(13,'BEL','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'BEL','Thibaut','Courtois'),(3,'BEL','Arthur','Theate'),
(4,'BEL','Timothy','Castagne'),(5,'BEL','Zeno','Debast'),
(6,'BEL','Brandon','Mechele'),(7,'BEL','Maxim','De Cuyper'),
(8,'BEL','Thomas','Meunier'),(9,'BEL','Youri','Tielemans'),
(10,'BEL','Amadou','Onana'),(11,'BEL','Nicolas','Raskin'),
(12,'BEL','Alexis','Saelemaekers'),(14,'BEL','Hans','Vanaken'),
(15,'BEL','Kevin','De Bruyne'),(16,'BEL','Jérémy','Doku'),
(17,'BEL','Charles','De Ketelaere'),(18,'BEL','Leandro','Trossard'),
(19,'BEL','Loïs','Openda'),(20,'BEL','Romelu','Lukaku');
-- ============================================================
-- EGYPT (EGY)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'EGY',60),(2,'EGY',60),(3,'EGY',60),(4,'EGY',60),(5,'EGY',60),(6,'EGY',60),
(7,'EGY',60),(8,'EGY',60),(9,'EGY',60),(10,'EGY',60),(11,'EGY',61),(12,'EGY',61),
(13,'EGY',61),(14,'EGY',61),(15,'EGY',61),(16,'EGY',61),(17,'EGY',61),(18,'EGY',61),
(19,'EGY',61),(20,'EGY',61);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'EGY','Escudo FOIL'),(13,'EGY','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'EGY','Mohamed','Elshenawy'),(3,'EGY','Mohamed','Hany'),
(4,'EGY','Mohamed','Hamdy'),(5,'EGY','Yasser','Ibrahim'),
(6,'EGY','Khaled','Sobhi'),(7,'EGY','Ramy','Rabia'),
(8,'EGY','Hossam','Abdelmaguid'),(9,'EGY','Ahmed','Fatouh'),
(10,'EGY','Marwan','Attia'),(11,'EGY','Zizo',NULL),
(12,'EGY','Hamdy','Fathy'),(14,'EGY','Mohanad','Lasheen'),
(15,'EGY','Emam','Ashour'),(16,'EGY','Osama','Faisal'),
(17,'EGY','Mohamed','Salah'),(18,'EGY','Mostafa','Mohamed'),
(19,'EGY','Trezeguet',NULL),(20,'EGY','Omar','Marmoush');
-- ============================================================
-- IR IRAN (IRN) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'IRN',62),(2,'IRN',62),(3,'IRN',62),(4,'IRN',62),(5,'IRN',62),(6,'IRN',62),
(7,'IRN',62),(8,'IRN',62),(9,'IRN',62),(10,'IRN',62),(11,'IRN',63),(12,'IRN',63),
(13,'IRN',63),(14,'IRN',63),(15,'IRN',63),(16,'IRN',63),(17,'IRN',63),(18,'IRN',63),
(19,'IRN',63),(20,'IRN',63);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'IRN','Escudo FOIL'),(13,'IRN','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'IRN','Alireza','Beiranvand'),(3,'IRN','Morteza','Pouraliganji'),
(4,'IRN','Ehsan','Hajsafi'),(5,'IRN','Milad','Mohammadi'),
(6,'IRN','Shojae','Khalilzadeh'),(7,'IRN','Ramin','Rezaeian'),
(8,'IRN','Hossein','Kanaani'),(9,'IRN','Sadegh','Moharrami'),
(10,'IRN','Saleh','Hardani'),(11,'IRN','Saeed','Ezatolahi'),
(12,'IRN','Saman','Ghoddos'),(14,'IRN','Omid','Noorafkan'),
(15,'IRN','Roozbeh','Cheshmi'),(16,'IRN','Mohammad','Mohebi'),
(17,'IRN','Sardar','Azmoun'),(18,'IRN','Mehdi','Taremi'),
(19,'IRN','Alireza','Jahanbakhsh'),(20,'IRN','Ali','Gholizadeh');
-- ============================================================
-- NEW ZEALAND (NZL) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'NZL',64),(2,'NZL',64),(3,'NZL',64),(4,'NZL',64),(5,'NZL',64),(6,'NZL',64),
(7,'NZL',64),(8,'NZL',64),(9,'NZL',64),(10,'NZL',64),(11,'NZL',65),(12,'NZL',65),
(13,'NZL',65),(14,'NZL',65),(15,'NZL',65),(16,'NZL',65),(17,'NZL',65),(18,'NZL',65),
(19,'NZL',65),(20,'NZL',65);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'NZL','Escudo FOIL'),(13,'NZL','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'NZL','Max','Crocombe'),(3,'NZL','Alex','Paulsen'),
(4,'NZL','Michael','Boxall'),(5,'NZL','Liberato','Cacace'),
(6,'NZL','Tim','Payne'),(7,'NZL','Tyler','Bindon'),
(8,'NZL','Francis','de Vries'),(9,'NZL','Finn','Surman'),
(10,'NZL','Joe','Bell'),(11,'NZL','Sarpreet','Singh'),
(12,'NZL','Ryan','Thomas'),(14,'NZL','Matthew','Garbett'),
(15,'NZL','Marko','Stamenić'),(16,'NZL','Ben','Old'),
(17,'NZL','Chris','Wood'),(18,'NZL','Elijah','Just'),
(19,'NZL','Callum','McCowatt'),(20,'NZL','Kosta','Barbarouses');
-- ------------------------------------------------------------
-- GRUPO H
-- ------------------------------------------------------------
-- ============================================================
-- ESPAÑA (ESP) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'ESP',66),(2,'ESP',66),(3,'ESP',66),(4,'ESP',66),(5,'ESP',66),(6,'ESP',66),
(7,'ESP',66),(8,'ESP',66),(9,'ESP',66),(10,'ESP',66),(11,'ESP',67),(12,'ESP',67),
(13,'ESP',67),(14,'ESP',67),(15,'ESP',67),(16,'ESP',67),(17,'ESP',67),(18,'ESP',67),
(19,'ESP',67),(20,'ESP',67);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'ESP','Escudo FOIL'),(13,'ESP','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'ESP','Unai','Simón'),(3,'ESP','Robin','Le Normand'),
(4,'ESP','Aymeric','Laporte'),(5,'ESP','Dean','Huijsen'),
(6,'ESP','Pedro','Porro'),(7,'ESP','Dani','Carvajal'),
(8,'ESP','Marc','Cucurella'),(9,'ESP','Martín','Zubimendi'),
(10,'ESP','Rodri',NULL),(11,'ESP','Pedri',NULL),
(12,'ESP','Fabián','Ruiz'),(14,'ESP','Mikel','Merino'),
(15,'ESP','Lamine','Yamal'),(16,'ESP','Dani','Olmo'),
(17,'ESP','Nico','Williams'),(18,'ESP','Ferran','Torres'),
(19,'ESP','Álvaro','Morata'),(20,'ESP','Mikel','Oyarzabal');
-- ============================================================
-- CABO VERDE (CPV)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'CPV',68),(2,'CPV',68),(3,'CPV',68),(4,'CPV',68),(5,'CPV',68),(6,'CPV',68),
(7,'CPV',68),(8,'CPV',68),(9,'CPV',68),(10,'CPV',68),(11,'CPV',69),(12,'CPV',69),
(13,'CPV',69),(14,'CPV',69),(15,'CPV',69),(16,'CPV',69),(17,'CPV',69),(18,'CPV',69),
(19,'CPV',69),(20,'CPV',69);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'CPV','Escudo FOIL'),(13,'CPV','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'CPV','Vozinha',NULL),(3,'CPV','Logan','Costa'),
(4,'CPV','Pico',NULL),(5,'CPV','Diney',NULL),
(6,'CPV','Steven','Moreira'),(7,'CPV','Wagner','Pina'),
(8,'CPV','João','Paulo'),(9,'CPV','Yannick','Semedo'),
(10,'CPV','Kevin','Pina'),(11,'CPV','Patrick','Andrade'),
(12,'CPV','Jamiro','Monteiro'),(14,'CPV','Deroy','Duarte'),
(15,'CPV','Garry','Rodrigues'),(16,'CPV','Jovane','Cabral'),
(17,'CPV','Ryan','Mendes'),(18,'CPV','Dailon','Livramento'),
(19,'CPV','Willy','Semedo'),(20,'CPV','Bebé',NULL);
-- ============================================================
-- SAUDI ARABIA (KSA)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'KSA',70),(2,'KSA',70),(3,'KSA',70),(4,'KSA',70),(5,'KSA',70),(6,'KSA',70),
(7,'KSA',70),(8,'KSA',70),(9,'KSA',70),(10,'KSA',70),(11,'KSA',71),(12,'KSA',71),
(13,'KSA',71),(14,'KSA',71),(15,'KSA',71),(16,'KSA',71),(17,'KSA',71),(18,'KSA',71),
(19,'KSA',71),(20,'KSA',71);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'KSA','Escudo FOIL'),(13,'KSA','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'KSA','Nawaf','Alaqidi'),(3,'KSA','Abdulrahman','Alsanbi'),
(4,'KSA','Saud','Abdulhamid'),(5,'KSA','Nawaf','Buwashl'),
(6,'KSA','Jehad','Thikri'),(7,'KSA','Moteb','Alharbi'),
(8,'KSA','Hassan','Altambakti'),(9,'KSA','Musab','Aljuwayr'),
(10,'KSA','Ziyad','Aljohani'),(11,'KSA','Abdullah','Alkhaibari'),
(12,'KSA','Nasser','Aldawsari'),(14,'KSA','Saleh','Abu Alshamat'),
(15,'KSA','Marwan','Alsahafi'),(16,'KSA','Salem','Aldawsari'),
(17,'KSA','Abdulrahman','Alobud'),(18,'KSA','Feras','Albrikan'),
(19,'KSA','Saleh','Alshehri'),(20,'KSA','Abdullah','Alhamdan');
-- ============================================================
-- URUGUAY (URU)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'URU',72),(2,'URU',72),(3,'URU',72),(4,'URU',72),(5,'URU',72),(6,'URU',72),
(7,'URU',72),(8,'URU',72),(9,'URU',72),(10,'URU',72),(11,'URU',73),(12,'URU',73),
(13,'URU',73),(14,'URU',73),(15,'URU',73),(16,'URU',73),(17,'URU',73),(18,'URU',73),
(19,'URU',73),(20,'URU',73);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'URU','Escudo FOIL'),(13,'URU','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'URU','Sergio','Rochet'),(3,'URU','Santiago','Mele'),
(4,'URU','Ronald','Araújo'),(5,'URU','José María','Giménez'),
(6,'URU','Sebastián','Cáceres'),(7,'URU','Mathías','Olivera'),
(8,'URU','Guillermo','Varela'),(9,'URU','Nahitan','Nández'),
(10,'URU','Federico','Valverde'),(11,'URU','Giorgian','De Arrascaeta'),
(12,'URU','Rodrigo','Bentancur'),(14,'URU','Manuel','Ugarte'),
(15,'URU','Nicolás','De La Cruz'),(16,'URU','Maxi','Araújo'),
(17,'URU','Darwin','Núñez'),(18,'URU','Federico','Viñas'),
(19,'URU','Rodrigo','Aguirre'),(20,'URU','Facundo','Pellistri');    
-- ------------------------------------------------------------
-- GRUPO I
-- ------------------------------------------------------------
-- ============================================================
-- FRANCIA (FRA)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'FRA',74),(2,'FRA',74),(3,'FRA',74),(4,'FRA',74),(5,'FRA',74),(6,'FRA',74),
(7,'FRA',74),(8,'FRA',74),(9,'FRA',74),(10,'FRA',74),(11,'FRA',75),(12,'FRA',75),
(13,'FRA',75),(14,'FRA',75),(15,'FRA',75),(16,'FRA',75),(17,'FRA',75),(18,'FRA',75),
(19,'FRA',75),(20,'FRA',75);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'FRA','Escudo FOIL'),(13,'FRA','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'FRA','Mike','Maignan'),(3,'FRA','Théo','Hernández'),
(4,'FRA','William','Saliba'),(5,'FRA','Jules','Koundé'),
(6,'FRA','Ibrahima','Konaté'),(7,'FRA','Dayot','Upamecano'),
(8,'FRA','Lucas','Digne'),(9,'FRA','Aurélien','Tchouaméni'),
(10,'FRA','Eduardo','Camavinga'),(11,'FRA','Manu','Koné'),
(12,'FRA','Adrien','Rabiot'),(14,'FRA','Michael','Olise'),
(15,'FRA','Ousmane','Dembélé'),(16,'FRA','Bradley','Barcola'),
(17,'FRA','Désiré','Doué'),(18,'FRA','Kingsley','Coman'),
(19,'FRA','Hugo','Ekitiké'),(20,'FRA','Kylian','Mbappé');
-- ============================================================
-- SENEGAL (SEN) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'SEN',76),(2,'SEN',76),(3,'SEN',76),(4,'SEN',76),(5,'SEN',76),(6,'SEN',76),
(7,'SEN',76),(8,'SEN',76),(9,'SEN',76),(10,'SEN',76),(11,'SEN',77),(12,'SEN',77),
(13,'SEN',77),(14,'SEN',77),(15,'SEN',77),(16,'SEN',77),(17,'SEN',77),(18,'SEN',77),
(19,'SEN',77),(20,'SEN',77);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'SEN','Escudo FOIL'),(13,'SEN','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'SEN','Édouard','Mendy'),(3,'SEN','Yehvann','Diouf'),
(4,'SEN','Moussa','Niakhaté'),(5,'SEN','Abdoulaye','Seck'),
(6,'SEN','Ismail','Jakobs'),(7,'SEN','El Hadji Malick','Diouf'),
(8,'SEN','Kalidou','Koulibaly'),(9,'SEN','Idrissa Gana','Gueye'),
(10,'SEN','Pape Matar','Sarr'),(11,'SEN','Pape','Gueye'),
(12,'SEN','Habib','Diarra'),(14,'SEN','Lamine','Camara'),
(15,'SEN','Sadio','Mané'),(16,'SEN','Ismaïla','Sarr'),
(17,'SEN','Boulaye','Dia'),(18,'SEN','Iliman','Ndiaye'),
(19,'SEN','Nicolas','Jackson'),(20,'SEN','Krépin','Diatta');
-- ============================================================
-- IRAQ (IRQ) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'IRQ',78),(2,'IRQ',78),(3,'IRQ',78),(4,'IRQ',78),(5,'IRQ',78),(6,'IRQ',78),
(7,'IRQ',78),(8,'IRQ',78),(9,'IRQ',78),(10,'IRQ',78),(11,'IRQ',79),(12,'IRQ',79),
(13,'IRQ',79),(14,'IRQ',79),(15,'IRQ',79),(16,'IRQ',79),(17,'IRQ',79),(18,'IRQ',79),
(19,'IRQ',79),(20,'IRQ',79);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'IRQ','Escudo FOIL'),(13,'IRQ','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'IRQ','Jalal','Hassan'),(3,'IRQ','Rebin','Sulaka'),
(4,'IRQ','Hussein','Ali'),(5,'IRQ','Akam','Hashem'),
(6,'IRQ','Merchas','Doski'),(7,'IRQ','Zaid','Tahseen'),
(8,'IRQ','Manaf','Younis'),(9,'IRQ','Zidane','Iqbal'),
(10,'IRQ','Amir','Al-Ammari'),(11,'IRQ','Ibrahim','Bayesh'),
(12,'IRQ','Ali','Jasim'),(14,'IRQ','Youssef','Amyn'),
(15,'IRQ','Aimar','Sher'),(16,'IRQ','Marko','Farji'),
(17,'IRQ','Osama','Rashid'),(18,'IRQ','Ali','Al-Hamadi'),
(19,'IRQ','Aymen','Hussein'),(20,'IRQ','Mohanad','Ali');
-- ============================================================
-- NORWAY (NOR)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'NOR',80),(2,'NOR',80),(3,'NOR',80),(4,'NOR',80),(5,'NOR',80),(6,'NOR',80),
(7,'NOR',80),(8,'NOR',80),(9,'NOR',80),(10,'NOR',80),(11,'NOR',81),(12,'NOR',81),
(13,'NOR',81),(14,'NOR',81),(15,'NOR',81),(16,'NOR',81),(17,'NOR',81),(18,'NOR',81),
(19,'NOR',81),(20,'NOR',81);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'NOR','Escudo FOIL'),(13,'NOR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'NOR','Ørjan','Nyland'),(3,'NOR','Julian','Ryerson'),
(4,'NOR','Leo','Østigård'),(5,'NOR','Kristoffer Vassbakk','Ajer'),
(6,'NOR','Marcus Holmgren','Pedersen'),(7,'NOR','David Møller','Wolfe'),
(8,'NOR','Torbjørn','Heggem'),(9,'NOR','Morten','Thorsby'),
(10,'NOR','Martin','Ødegaard'),(11,'NOR','Sander','Berge'),
(12,'NOR','Andreas','Schjelderup'),(14,'NOR','Patrick','Berg'),
(15,'NOR','Erling','Haaland'),(16,'NOR','Alexander','Sørloth'),
(17,'NOR','Aron','Dønnum'),(18,'NOR','Jørgen Strand','Larsen'),
(19,'NOR','Antonio','Nusa'),(20,'NOR','Oscar','Bobb');
-- ------------------------------------------------------------
-- GRUPO J
-- ------------------------------------------------------------
-- ============================================================
-- ARGENTINA (ARG) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'ARG',82),(2,'ARG',82),(3,'ARG',82),(4,'ARG',82),(5,'ARG',82),(6,'ARG',82),
(7,'ARG',82),(8,'ARG',82),(9,'ARG',82),(10,'ARG',82),(11,'ARG',83),(12,'ARG',83),
(13,'ARG',83),(14,'ARG',83),(15,'ARG',83),(16,'ARG',83),(17,'ARG',83),(18,'ARG',83),
(19,'ARG',83),(20,'ARG',83);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'ARG','Escudo FOIL'),(13,'ARG','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'ARG','Emiliano','Martínez'),(3,'ARG','Nahuel','Molina'),
(4,'ARG','Cristian','Romero'),(5,'ARG','Nicolás','Otamendi'),
(6,'ARG','Nicolás','Tagliafico'),(7,'ARG','Leonardo','Balerdi'),
(8,'ARG','Enzo','Fernández'),(9,'ARG','Alexis','Mac Allister'),
(10,'ARG','Rodrigo','De Paul'),(11,'ARG','Exequiel','Palacios'),
(12,'ARG','Leandro','Paredes'),(14,'ARG','Nico','Paz'),
(15,'ARG','Franco','Mastantuono'),(16,'ARG','Nico','González'),
(17,'ARG','Lionel','Messi'),(18,'ARG','Lautaro','Martínez'),
(19,'ARG','Julián','Álvarez'),(20,'ARG','Giuliano','Simeone');
-- ============================================================
-- ARGELIA (ALG)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'ALG',84),(2,'ALG',84),(3,'ALG',84),(4,'ALG',84),(5,'ALG',84),(6,'ALG',84),
(7,'ALG',84),(8,'ALG',84),(9,'ALG',84),(10,'ALG',84),(11,'ALG',85),(12,'ALG',85),
(13,'ALG',85),(14,'ALG',85),(15,'ALG',85),(16,'ALG',85),(17,'ALG',85),(18,'ALG',85),
(19,'ALG',85),(20,'ALG',85);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'ALG','Escudo FOIL'),(13,'ALG','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'ALG','Alexis','Guendouz'),(3,'ALG','Ramy','Bensebaini'),
(4,'ALG','Youcef','Atal'),(5,'ALG','Rayan','Aït-Nouri'),
(6,'ALG','Mohamed Amine','Tougai'),(7,'ALG','Aïssa','Mandi'),
(8,'ALG','Ismaël','Bennacer'),(9,'ALG','Houssem','Aouar'),
(10,'ALG','Hicham','Boudaoui'),(11,'ALG','Ramiz','Zerrouki'),
(12,'ALG','Nabil','Bentaleb'),(14,'ALG','Farès','Chaïbi'),
(15,'ALG','Riyad','Mahrez'),(16,'ALG','Saïd','Benrahma'),
(17,'ALG','Anis','Hadj Moussa'),(18,'ALG','Amine','Gouiri'),
(19,'ALG','Baghdad','Bounedjah'),(20,'ALG','Mohamed','Amoura');
-- ============================================================
-- AUSTRIA (AUT)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'AUT',86),(2,'AUT',86),(3,'AUT',86),(4,'AUT',86),(5,'AUT',86),(6,'AUT',86),
(7,'AUT',86),(8,'AUT',86),(9,'AUT',86),(10,'AUT',86),(11,'AUT',87),(12,'AUT',87),
(13,'AUT',87),(14,'AUT',87),(15,'AUT',87),(16,'AUT',87),(17,'AUT',87),(18,'AUT',87),
(19,'AUT',87),(20,'AUT',87);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'AUT','Escudo FOIL'),(13,'AUT','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'AUT','Alexander','Schlager'),(3,'AUT','Patrick','Pentz'),
(4,'AUT','David','Alaba'),(5,'AUT','Kevin','Danso'),
(6,'AUT','Philipp','Lienhart'),(7,'AUT','Stefan','Posch'),
(8,'AUT','Philipp','Mwene'),(9,'AUT','Alexander','Prass'),
(10,'AUT','Xaver','Schlager'),(11,'AUT','Marcel','Sabitzer'),
(12,'AUT','Konrad','Laimer'),(14,'AUT','Florian','Grillitsch'),
(15,'AUT','Nicolas','Seiwald'),(16,'AUT','Romano','Schmid'),
(17,'AUT','Patrick','Wimmer'),(18,'AUT','Christoph','Baumgartner'),
(19,'AUT','Michael','Gregoritsch'),(20,'AUT','Marko','Arnautović');
-- ============================================================
-- JORDAN (JOR)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'JOR',88),(2,'JOR',88),(3,'JOR',88),(4,'JOR',88),(5,'JOR',88),(6,'JOR',88),
(7,'JOR',88),(8,'JOR',88),(9,'JOR',88),(10,'JOR',88),(11,'JOR',89),(12,'JOR',89),
(13,'JOR',89),(14,'JOR',89),(15,'JOR',89),(16,'JOR',89),(17,'JOR',89),(18,'JOR',89),
(19,'JOR',89),(20,'JOR',89);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'JOR','Escudo FOIL'),(13,'JOR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'JOR','Yazeed','Abulaila'),(3,'JOR','Ihsan','Haddad'),
(4,'JOR','Mohammad','Abu Hashish'),(5,'JOR','Yazan','Al-Arab'),
(6,'JOR','Abdallah','Nasib'),(7,'JOR','Saleem','Obaid'),
(8,'JOR','Mohammad','Abualnadi'),(9,'JOR','Ibrahim','Saadeh'),
(10,'JOR','Nizar','Al-Rashdan'),(11,'JOR','Noor','Al-Rawabdeh'),
(12,'JOR','Mohannad','Abu Taha'),(14,'JOR','Amer','Jamous'),
(15,'JOR','Mousa','Al-Taamari'),(16,'JOR','Yazan','Al-Naimat'),
(17,'JOR','Mahmoud','Al-Mardi'),(18,'JOR','Ali','Olwan'),
(19,'JOR','Mohammad','Abu Zrayq'),(20,'JOR','Ibrahim','Sabra');
-- ------------------------------------------------------------
-- GRUPO K
-- ------------------------------------------------------------
-- ============================================================
-- PORTUGAL (POR)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'POR',90),(2,'POR',90),(3,'POR',90),(4,'POR',90),(5,'POR',90),(6,'POR',90),
(7,'POR',90),(8,'POR',90),(9,'POR',90),(10,'POR',90),(11,'POR',91),(12,'POR',91),
(13,'POR',91),(14,'POR',91),(15,'POR',91),(16,'POR',91),(17,'POR',91),(18,'POR',91),
(19,'POR',91),(20,'POR',91);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'POR','Escudo FOIL'),(13,'POR','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'POR','Diogo','Costa'),(3,'POR','Rui','Patrício'),
(4,'POR','Rúben','Dias'),(5,'POR','Pepe',NULL),
(6,'POR','João','Cancelo'),(7,'POR','Nuno','Mendes'),
(8,'POR','Bernardo','Silva'),(9,'POR','Vitinha',NULL),
(10,'POR','Rúben','Neves'),(11,'POR','João','Palhinha'),
(12,'POR','Bruno','Fernandes'),(14,'POR','Cristiano','Ronaldo'),
(15,'POR','Rafael','Leão'),(16,'POR','Diogo','Jota'),
(17,'POR','Pedro','Neto'),(18,'POR','Gonçalo','Ramos'),
(19,'POR','João','Félix'),(20,'POR','Francisco','Conceição');
-- ============================================================
-- CONGO DR (COD) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'COD',92),(2,'COD',92),(3,'COD',92),(4,'COD',92),(5,'COD',92),(6,'COD',92),
(7,'COD',92),(8,'COD',92),(9,'COD',92),(10,'COD',92),(11,'COD',93),(12,'COD',93),
(13,'COD',93),(14,'COD',93),(15,'COD',93),(16,'COD',93),(17,'COD',93),(18,'COD',93),
(19,'COD',93),(20,'COD',93);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'COD','Escudo FOIL'),(13,'COD','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'COD','Joël','Kiassumbua'),(3,'COD','Ben','Kiassumbua'),
(4,'COD','Chancel','Mbemba'),(5,'COD','Arthur','Masuaku'),
(6,'COD','Merveille','Bope Bokadi'),(7,'COD','Marcel','Tisserand'),
(8,'COD','Théo','Bongonda'),(9,'COD','Chadrac','Akolo'),
(10,'COD','Samuel','Bastien'),(11,'COD','Hérita','Ilunga'),
(12,'COD','Nathan','Ilunga'),(14,'COD','Cédric','Bakambu'),
(15,'COD','Yannick','Bolasie'),(16,'COD','Firmin','Mubele'),
(17,'COD','Jonathan','Bolingi'),(18,'COD','Zola','Matumona'),
(19,'COD','Ngita','Mayamba'),(20,'COD','Bijou','Bisseck');
-- ============================================================
-- UZBEKISTÁN (UZB) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'UZB',94),(2,'UZB',94),(3,'UZB',94),(4,'UZB',94),(5,'UZB',94),(6,'UZB',94),
(7,'UZB',94),(8,'UZB',94),(9,'UZB',94),(10,'UZB',94),(11,'UZB',95),(12,'UZB',95),
(13,'UZB',95),(14,'UZB',95),(15,'UZB',95),(16,'UZB',95),(17,'UZB',95),(18,'UZB',95),
(19,'UZB',95),(20,'UZB',95);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'UZB','Escudo FOIL'),(13,'UZB','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'UZB','Utkir','Yusupov'),(3,'UZB','Farrukh','Sayfiev'),
(4,'UZB','Sherzod','Nasrullaev'),(5,'UZB','Umar','Eshmurodov'),
(6,'UZB','Husniddin','Aliqulov'),(7,'UZB','Rustamjon','Ashurmatov'),
(8,'UZB','Khojiakbar','Alijonov'),(9,'UZB','Abdukodir','Khusanov'),
(10,'UZB','Odiljon','Hamrobekov'),(11,'UZB','Otabek','Shukurov'),
(12,'UZB','Jamshid','Iskanderov'),(14,'UZB','Eldor','Shomurodov'),
(15,'UZB','Jasur','Yakhshiboev'),(16,'UZB','Jaloliddin','Masharipov'),
(17,'UZB','Shamsiddin','Karimov'),(18,'UZB','Dostonbek','Tursunov'),
(19,'UZB','Bobur','Abdixoliqov'),(20,'UZB','Khurshid','Tursunov');
-- ============================================================
-- COLOMBIA (COL)
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'COL',96),(2,'COL',96),(3,'COL',96),(4,'COL',96),(5,'COL',96),(6,'COL',96),
(7,'COL',96),(8,'COL',96),(9,'COL',96),(10,'COL',96),(11,'COL',97),(12,'COL',97),
(13,'COL',97),(14,'COL',97),(15,'COL',97),(16,'COL',97),(17,'COL',97),(18,'COL',97),
(19,'COL',97),(20,'COL',97);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'COL','Escudo FOIL'),(13,'COL','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'COL','Camilo','Vargas'),(3,'COL','Kevin','Castaño'),
(4,'COL','Santiago','Arias'),(5,'COL','Davinson','Sánchez'),
(6,'COL','Yerry','Mina'),(7,'COL','Johan','Mojica'),
(8,'COL','Daniel','Muñoz'),(9,'COL','Wilmar','Barrios'),
(10,'COL','Mateus','Uribe'),(11,'COL','Richard','Ríos'),
(12,'COL','James','Rodríguez'),(14,'COL','Luis','Díaz'),
(15,'COL','Rafael','Santos Borré'),(16,'COL','Radamel','Falcao'),
(17,'COL','Jhon','Córdoba'),(18,'COL','Cucho','Hernández'),
(19,'COL','Jhon Jáder','Durán'),(20,'COL','Juan','Camilo Hernández');
-- ------------------------------------------------------------
-- GRUPO L
-- ------------------------------------------------------------
-- ============================================================
-- INGLATERRA (ENG) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'ENG',98),(2,'ENG',98),(3,'ENG',98),(4,'ENG',98),(5,'ENG',98),(6,'ENG',98),
(7,'ENG',98),(8,'ENG',98),(9,'ENG',98),(10,'ENG',98),(11,'ENG',99),(12,'ENG',99),
(13,'ENG',99),(14,'ENG',99),(15,'ENG',99),(16,'ENG',99),(17,'ENG',99),(18,'ENG',99),
(19,'ENG',99),(20,'ENG',99);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'ENG','Escudo FOIL'),(13,'ENG','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'ENG','Jordan','Pickford'),(3,'ENG','Aaron','Ramsdale'),
(4,'ENG','Kyle','Walker'),(5,'ENG','John','Stones'),
(6,'ENG','Harry','Maguire'),(7,'ENG','Luke','Shaw'),
(8,'ENG','Trent','Alexander-Arnold'),(9,'ENG','Declan','Rice'),
(10,'ENG','Jude','Bellingham'),(11,'ENG','Kobbie','Mainoo'),
(12,'ENG','Phil','Foden'),(14,'ENG','Harry','Kane'),
(15,'ENG','Bukayo','Saka'),(16,'ENG','Marcus','Rashford'),
(17,'ENG','Raheem','Sterling'),(18,'ENG','Jack','Grealish'),
(19,'ENG','Jarrod','Bowen'),(20,'ENG','Cole','Palmer');
-- ============================================================
-- CROACIA (CRO) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'CRO',100),(2,'CRO',100),(3,'CRO',100),(4,'CRO',100),(5,'CRO',100),(6,'CRO',100),
(7,'CRO',100),(8,'CRO',100),(9,'CRO',100),(10,'CRO',100),(11,'CRO',101),(12,'CRO',101),
(13,'CRO',101),(14,'CRO',101),(15,'CRO',101),(16,'CRO',101),(17,'CRO',101),(18,'CRO',101),
(19,'CRO',101),(20,'CRO',101);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'CRO','Escudo FOIL'),(13,'CRO','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'CRO','Dominik','Livaković'),(3,'CRO','Ivica','Ivušić'),
(4,'CRO','Josip','Šutalo'),(5,'CRO','Duje','Ćaleta-Car'),
(6,'CRO','Borna','Sosa'),(7,'CRO','Josip','Stanišić'),
(8,'CRO','Luka','Modrić'),(9,'CRO','Mateo','Kovačić'),
(10,'CRO','Marcelo','Brozović'),(11,'CRO','Mario','Pašalić'),
(12,'CRO','Lovro','Majer'),(14,'CRO','Ivan','Perišić'),
(15,'CRO','Andrej','Kramarić'),(16,'CRO','Bruno','Petković'),
(17,'CRO','Marko','Livaja'),(18,'CRO','Luka','Ivanušec'),
(19,'CRO','Petar','Sučić'),(20,'CRO','Antonio-Mirko','Čolak');
-- ============================================================
-- GHANA (GHA) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'GHA',102),(2,'GHA',102),(3,'GHA',102),(4,'GHA',102),(5,'GHA',102),(6,'GHA',102),
(7,'GHA',102),(8,'GHA',102),(9,'GHA',102),(10,'GHA',102),(11,'GHA',103),(12,'GHA',103),
(13,'GHA',103),(14,'GHA',103),(15,'GHA',103),(16,'GHA',103),(17,'GHA',103),(18,'GHA',103),
(19,'GHA',103),(20,'GHA',103);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'GHA','Escudo FOIL'),(13,'GHA','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'GHA','Lawrence','Ati Zigi'),(3,'GHA','Abdul','Manaf Nurudeen'),
(4,'GHA','Daniel','Amartey'),(5,'GHA','Alexander','Djiku'),
(6,'GHA','Tariq','Lamptey'),(7,'GHA','Denis','Odoi'),
(8,'GHA','Thomas','Partey'),(9,'GHA','Baba','Rahman'),
(10,'GHA','André','Ayew'),(11,'GHA','Jordan','Ayew'),
(12,'GHA','Mohammed','Kudus'),(14,'GHA','Inaki','Williams'),
(15,'GHA','Felix','Afena-Gyan'),(16,'GHA','Richmond','Boakye-Yiadom'),
(17,'GHA','Ransford-Yeboah','Königsdörffer'),(18,'GHA','Kamaldeen','Sulemana'),
(19,'GHA','Joseph','Paintsil'),(20,'GHA','Antoine','Semenyo');
-- ============================================================
-- PANAMÁ (PAN) 
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1,'PAN',104),(2,'PAN',104),(3,'PAN',104),(4,'PAN',104),(5,'PAN',104),(6,'PAN',104),
(7,'PAN',104),(8,'PAN',104),(9,'PAN',104),(10,'PAN',104),(11,'PAN',105),(12,'PAN',105),
(13,'PAN',105),(14,'PAN',105),(15,'PAN',105),(16,'PAN',105),(17,'PAN',105),(18,'PAN',105),
(19,'PAN',105),(20,'PAN',105);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES (1,'PAN','Escudo FOIL'),(13,'PAN','Foto de equipo');
INSERT OR IGNORE INTO FJUGADOR (numFigura,codPais,nombre,apellido) VALUES
(2,'PAN','Orlando','Mosquera'),(3,'PAN','Luis','Mejia'),
(4,'PAN','Fidel','Escobar'),(5,'PAN','Andres','Andrade'),
(6,'PAN','Michael Amir','Murillo'),(7,'PAN','Eric','Davis'),
(8,'PAN','Jose','Cordoba'),(9,'PAN','Cesar','Blackman'),
(10,'PAN','Cristian','Martinez'),(11,'PAN','Aníbal','Godoy'),
(12,'PAN','Adalberto','Carrasquilla'),(14,'PAN','Édgar','Bárcenas'),
(15,'PAN','Carlos','Harvey'),(16,'PAN','Ismael','Díaz'),
(17,'PAN','Jose','Fajardo'),(18,'PAN','Cecilio','Waterman'),
(19,'PAN','Jose Luiz','Rodriguez'),(20,'PAN','Alberto','Quintero');
-- ============================================================
-- FIGURITAS ESPECIALES RESTANTES
-- ============================================================
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(9,'FWC',106),(10,'FWC',106),(11,'FWC',107),(12,'FWC',107),(13,'FWC',107),
(14,'FWC',108),(15,'FWC',108),(16,'FWC',109),(17,'FWC',109),(18,'FWC',109),
(19,'FWC',109);
INSERT OR IGNORE INTO FESPECIAL (numFigura, codPais, tipoEspecial) VALUES
(9,'FWC','Italia 1934'),
(10,'FWC','Uruguay 1950'),
(11,'FWC','Alemania Occidental 1954'),
(12,'FWC','Brasil 1962'),
(13,'FWC','Alemania Occidental 1974'),
(14,'FWC','Argentina 1986'),
(15,'FWC','Brasil 1994'),
(16,'FWC','Brasil 2002'),
(17,'FWC','Italia 2006'),
(18,'FWC','Alemania 2014'),
(19,'FWC','Argentina 2022');
-- ============================================================
-- FIGURITAS ESPECIALES COCA-COLA
-- ============================================================
INSERT OR IGNORE INTO PAIS (codPais, nombre) VALUES ('CCL', 'Coca-Cola — Especial');
INSERT OR IGNORE INTO FIGURITA (numFigura, codPais, numPagina) VALUES
(1, 'CCL', 110), (2, 'CCL', 110), (3, 'CCL', 110), (4, 'CCL', 110), (5, 'CCL', 110), 
(6, 'CCL', 110),(7, 'CCL', 111), (8, 'CCL', 111), (9, 'CCL', 111), (10, 'CCL', 111), 
(11, 'CCL', 111), (12, 'CCL', 111), (13, 'CCL', 111), (14, 'CCL', 111);
INSERT OR IGNORE INTO FJUGADOR (numFigura, codPais, nombre, apellido) VALUES
(1, 'CCL', 'Lamine', 'Yamal'),
(2, 'CCL', 'Joshua', 'Kimmich'),
(3, 'CCL', 'Harry', 'Kane'),
(4, 'CCL', 'Santiago', 'Giménez'),
(5, 'CCL', 'Joško', 'Gvardiol'),
(6, 'CCL', 'Federico', 'Valverde'),
(7, 'CCL', 'Jefferson', 'Lerma'),
(8, 'CCL', 'Enner', 'Valencia'),
(9, 'CCL', 'Gabriel', 'Magalhães'),
(10, 'CCL', 'Virgil', 'van Dijk'),
(11, 'CCL', 'Alphonso', 'Davies'),
(12, 'CCL', 'Emiliano', 'Martínez'),
(13, 'CCL', 'Raúl', 'Jiménez'),
(14, 'CCL', 'Lautaro', 'Martínez');
-- ============================================================
-- Total registros FIGURITA: 980
-- Total registros FJUGADOR: ~864 (18 jugadores × 48 equipos)
-- Total registros FESPECIAL: ~116 (escudos + fotos + 20 especiales FWC)
-- ============================================================