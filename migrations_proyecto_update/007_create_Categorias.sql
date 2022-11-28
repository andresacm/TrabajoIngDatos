CREATE TABLE Categorias(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(15) NOT NULL,
  Descripcion VARCHAR2(200)
);

ALTER TABLE Categorias ADD (
  CONSTRAINT Categorias_pk PRIMARY KEY (ID));

CREATE SEQUENCE Categorias_seq START WITH 1;

CREATE OR REPLACE TRIGGER Categorias_pk 
BEFORE INSERT ON Categorias 
FOR EACH ROW

BEGIN
  SELECT Categorias_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/