CREATE TABLE TiposContrato(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(15) NOT NULL,
  Descripcion VARCHAR2(200)
);

ALTER TABLE TiposContrato ADD (
  CONSTRAINT TiposContrato_pk PRIMARY KEY (ID));

CREATE SEQUENCE TiposContrato_seq START WITH 1;

CREATE OR REPLACE TRIGGER TiposContrato_pk 
BEFORE INSERT ON TiposContrato 
FOR EACH ROW

BEGIN
  SELECT TiposContrato_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/