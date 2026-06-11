
PRAGMA foreign_keys = ON;

-- 1. PAÍS
CREATE TABLE IF NOT EXISTS PAIS (
    codPais     CHAR(3)      NOT NULL,
    nombre      VARCHAR(50)  NOT NULL,
    PRIMARY KEY (codPais)
);

-- 2. PÁGINA
CREATE TABLE IF NOT EXISTS PAGINA (
    numPagina   INTEGER      NOT NULL,
    PRIMARY KEY (numPagina)
);

-- 3. PEQUIPO
CREATE TABLE IF NOT EXISTS PEQUIPO (
    numPagina   INTEGER      NOT NULL,
    codPais     CHAR(3)      NOT NULL,
    PRIMARY KEY (numPagina),
    FOREIGN KEY (numPagina) REFERENCES PAGINA(numPagina),
    FOREIGN KEY (codPais)   REFERENCES PAIS(codPais)
);

-- 4. PEXTRA 
CREATE TABLE IF NOT EXISTS PEXTRA (
    numPagina   INTEGER      NOT NULL,
    seccion     VARCHAR(50),           
    PRIMARY KEY (numPagina),
    FOREIGN KEY (numPagina) REFERENCES PAGINA(numPagina)
);

-- 5. FIGURITA
CREATE TABLE IF NOT EXISTS FIGURITA (
    numFigura   INTEGER      NOT NULL,
    codPais     CHAR(3)      NOT NULL,
    numPagina   INTEGER      NOT NULL,
    PRIMARY KEY (numFigura, codPais),
    FOREIGN KEY (codPais)   REFERENCES PAIS(codPais),
    FOREIGN KEY (numPagina) REFERENCES PAGINA(numPagina)
);

-- 6. FJUGADOR
CREATE TABLE IF NOT EXISTS FJUGADOR (
    numFigura       INTEGER      NOT NULL,
    codPais         CHAR(3)      NOT NULL,
    nombre          VARCHAR(50),
    apellido        VARCHAR(50),
    pesoKg          REAL,
    alturaM         REAL,
    anioNacimiento  INTEGER,
    PRIMARY KEY (numFigura, codPais),
    FOREIGN KEY (numFigura, codPais) REFERENCES FIGURITA(numFigura, codPais)
);

-- 7. FESPECIAL
CREATE TABLE IF NOT EXISTS FESPECIAL (
    numFigura       INTEGER      NOT NULL,
    codPais         CHAR(3)      NOT NULL,
    tipoEspecial    VARCHAR(50),         
    PRIMARY KEY (numFigura, codPais),
    FOREIGN KEY (numFigura, codPais) REFERENCES FIGURITA(numFigura, codPais)
);

-- 8. COLECCION — el corazón del usuario
CREATE TABLE IF NOT EXISTS COLECCION (
    numFigura   INTEGER      NOT NULL,
    codPais     CHAR(3)      NOT NULL,
    pegada      INTEGER      NOT NULL DEFAULT 0,
    cantidad    INTEGER      NOT NULL DEFAULT 0, 
    PRIMARY KEY (numFigura, codPais),
    FOREIGN KEY (numFigura, codPais) REFERENCES FIGURITA(numFigura, codPais)
);