CREATE TABLE TiposPlan(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(25)
);

ALTER TABLE TiposPlan ADD (
  CONSTRAINT TiposPlan_pk PRIMARY KEY (ID));

CREATE SEQUENCE TiposPlan_seq START WITH 1;

CREATE OR REPLACE TRIGGER TiposPlan_pk 
BEFORE INSERT ON TiposPlan 
FOR EACH ROW

BEGIN
  SELECT TiposPlan_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/