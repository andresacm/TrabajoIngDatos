CREATE TABLE DistritosProvincias(
  id NUMBER(7) PRIMARY KEY,
  nombre VARCHAR2(30) NOT NULL,
  Zona_id NUMBER(2) not null,
  FOREIGN KEY (Zona_id) REFERENCES Zonas
);

ALTER TABLE DistritosProvincias ADD (
  CONSTRAINT DistritosProvincias_pk PRIMARY KEY (id));

CREATE SEQUENCE DistritosProvincias_seq START WITH 1;

CREATE OR REPLACE TRIGGER DistritosProvincias_pk 
BEFORE INSERT ON DistritosProvincias 
FOR EACH ROW

BEGIN
  SELECT Provincias_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/