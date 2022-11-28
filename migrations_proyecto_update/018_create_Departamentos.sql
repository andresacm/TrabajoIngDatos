CREATE TABLE Departamentos(
  id NUMBER(7) PRIMARY KEY,
  nombre VARCHAR2(20) NOT NULL,
  Provincia_id NUMBER(2) not null,
  FOREIGN KEY (Provincia_id) REFERENCES Provincias
);

ALTER TABLE Departamentos ADD (
  CONSTRAINT Departamentos_pk PRIMARY KEY (id));

CREATE SEQUENCE Departamentos_seq START WITH 1;

CREATE OR REPLACE TRIGGER Departamentos_pk 
BEFORE INSERT ON Departamentos 
FOR EACH ROW

BEGIN
  SELECT Departamentos_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/