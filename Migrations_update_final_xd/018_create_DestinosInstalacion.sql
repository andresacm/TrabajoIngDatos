CREATE TABLE DestinosInstalacion(
  id NUMBER(7) PRIMARY KEY,
  Direccion VARCHAR2(100) NOT NULL,
  TipoPredio_id NUMBER(2) not null,
  TipoVivienda_id NUMBER(2) not null,
  DistritoProvincia_id NUMBER(2) not null,
  FOREIGN KEY (TipoPredio_id) REFERENCES TiposPredio,
  FOREIGN KEY (TipoVivienda_id) REFERENCES TiposVivienda,
  FOREIGN KEY (DistritoProvincia_id) REFERENCES DistritosProvincias
);

ALTER TABLE DestinosInstalacion ADD (
  CONSTRAINT DestinosInstalacion_pk PRIMARY KEY (id));

CREATE SEQUENCE DestinosInstalacion_seq START WITH 1;

CREATE OR REPLACE TRIGGER DestinosInstalacion_pk 
BEFORE INSERT ON DestinosInstalacion 
FOR EACH ROW

BEGIN
  SELECT DestinosInstalacion_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/