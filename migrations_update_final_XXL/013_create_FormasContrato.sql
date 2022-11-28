CREATE TABLE FormasContrato(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(15) NOT NULL
);

ALTER TABLE FormasContrato ADD (
  CONSTRAINT FormasContrato_pk PRIMARY KEY (ID));

CREATE SEQUENCE FormasContrato_seq START WITH 1;

CREATE OR REPLACE TRIGGER FormasContrato_pk 
BEFORE INSERT ON FormasContrato 
FOR EACH ROW

BEGIN
  SELECT FormasContrato_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/