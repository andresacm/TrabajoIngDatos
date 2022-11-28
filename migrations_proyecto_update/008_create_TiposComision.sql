CREATE TABLE TiposComision(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(15) NOT NULL,
  Descripcion VARCHAR2(200)
);

ALTER TABLE TiposComision ADD (
  CONSTRAINT TiposComision_pk PRIMARY KEY (ID));

CREATE SEQUENCE TiposComision_seq START WITH 1;

CREATE OR REPLACE TRIGGER TiposComision_pk 
BEFORE INSERT ON TiposComision 
FOR EACH ROW

BEGIN
  SELECT TiposComision_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/