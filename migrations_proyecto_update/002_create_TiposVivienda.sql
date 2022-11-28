CREATE TABLE TiposVivienda(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(20)
);

ALTER TABLE TiposVivienda ADD (
  CONSTRAINT TiposVivienda_pk PRIMARY KEY (ID));

CREATE SEQUENCE TiposVivienda_seq START WITH 1;

CREATE OR REPLACE TRIGGER TiposVivienda_pk 
BEFORE INSERT ON TiposVivienda 
FOR EACH ROW

BEGIN
  SELECT TiposVivienda_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/