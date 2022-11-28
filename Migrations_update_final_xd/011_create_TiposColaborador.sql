CREATE TABLE TiposColaborador(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(30) NOT NULL,
  Descripcion VARCHAR2(200)
);

ALTER TABLE TiposColaborador ADD (
  CONSTRAINT TiposColaborador_pk PRIMARY KEY (ID));

CREATE SEQUENCE TiposColaborador_seq START WITH 1;

CREATE OR REPLACE TRIGGER TiposColaborador_pk 
BEFORE INSERT ON TiposColaborador 
FOR EACH ROW

BEGIN
  SELECT TiposColaborador_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/