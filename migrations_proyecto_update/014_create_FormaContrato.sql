CREATE TABLE FormaContrato(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(15) NOT NULL
);

ALTER TABLE FormaContrato ADD (
  CONSTRAINT FormaContrato_pk PRIMARY KEY (ID));

CREATE SEQUENCE FormaContrato_seq START WITH 1;

CREATE OR REPLACE TRIGGER FormaContrato_pk 
BEFORE INSERT ON FormaContrato 
FOR EACH ROW

BEGIN
  SELECT FormaContrato_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/