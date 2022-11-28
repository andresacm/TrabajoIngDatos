CREATE TABLE Provincias(
  id NUMBER(7) PRIMARY KEY,
  nombre VARCHAR2(20) NOT NULL,
  Distrito_id NUMBER(2) not null,
  FOREIGN KEY (Distrito_id) REFERENCES Distritos
);

ALTER TABLE Provincias ADD (
  CONSTRAINT Provincias_pk PRIMARY KEY (id));

CREATE SEQUENCE Provincias_seq START WITH 1;

CREATE OR REPLACE TRIGGER Provincias_pk 
BEFORE INSERT ON Provincias 
FOR EACH ROW

BEGIN
  SELECT Provincias_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/