CREATE TABLE TiposDocumento(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(10)
);

ALTER TABLE TiposDocumento ADD (
  CONSTRAINT TiposDocumento_pk PRIMARY KEY (ID));

CREATE SEQUENCE TiposDocumento_seq START WITH 1;

CREATE OR REPLACE TRIGGER TiposDocumento_pk 
BEFORE INSERT ON TiposDocumento 
FOR EACH ROW

BEGIN
  SELECT TiposDocumento_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/