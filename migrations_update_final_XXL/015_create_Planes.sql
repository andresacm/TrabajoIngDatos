CREATE TABLE Planes(
  id NUMBER(7) PRIMARY KEY,
  CantMegas NUMBER(15) NOT NULL,
  PrecioMensual FLOAT NOT NULL,
  TipoPlan_id NUMBER(7) NOT NULL,
  FOREIGN KEY (TipoPlan_id) REFERENCES TiposPlan

);

ALTER TABLE Planes ADD (
  CONSTRAINT Planes_pk PRIMARY KEY (id));

CREATE SEQUENCE Planes_seq START WITH 1;

CREATE OR REPLACE TRIGGER Planes_pk 
BEFORE INSERT ON Planes 
FOR EACH ROW

BEGIN
  SELECT Planes_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/