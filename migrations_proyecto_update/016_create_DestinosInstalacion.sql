CREATE TABLE DestinosInstalacion(
  id NUMBER(7) PRIMARY KEY,
  Cobertura VARCHAR2(2) NOT NULL,
  Direccion VARCHAR2(50) NOT NULL,
  CodigoPostal NUMBER(15) NOT NULL,
  TipoPredio_id NUMBER(2) not null,
  TipoVivienda_id NUMBER(2) not null,
  Distrito_id NUMBER(2) not null,
  FOREIGN KEY (TipoPredio_id) REFERENCES TiposPredio,
  FOREIGN KEY (TipoVivienda_id) REFERENCES TiposVivienda,
  FOREIGN KEY (Distrito_id) REFERENCES Distritos
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