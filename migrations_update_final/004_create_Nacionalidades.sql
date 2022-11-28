CREATE TABLE Nacionalidades(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(15)
);

ALTER TABLE Nacionalidades ADD (
  CONSTRAINT Nacionalidades_pk PRIMARY KEY (ID));

CREATE SEQUENCE Nacionalidades_seq START WITH 1;

CREATE OR REPLACE TRIGGER Nacionalidades_pk 
BEFORE INSERT ON Nacionalidades 
FOR EACH ROW

BEGIN
  SELECT Nacionalidades_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/