CREATE TABLE Ventas(
  id NUMBER(7) PRIMARY KEY,
  FechaVenta VARCHAR2(10) NOT NULL,
  Colaborador_id NUMBER(7) not null,
  Cliente_id NUMBER(7) not null,
  DestinoInstalacion_id NUMBER(7) not null,
  FormaContrato_id NUMBER(7) not null,
  Plan_id NUMBER(7) not null,
  FOREIGN KEY (Colaborador_id) REFERENCES Colaboradores,
  FOREIGN KEY (Cliente_id) REFERENCES Clientes,
  FOREIGN KEY (DestinoInstalacion_id) REFERENCES DestinosInstalacion,
  FOREIGN KEY (FormaContrato_id) REFERENCES FormasContrato,
  FOREIGN KEY (Plan_id) REFERENCES Planes
);

ALTER TABLE Ventas ADD (
  CONSTRAINT Ventas_pk PRIMARY KEY (id));

CREATE SEQUENCE Ventas_seq START WITH 1;

CREATE OR REPLACE TRIGGER Ventas_pk 
BEFORE INSERT ON Ventas 
FOR EACH ROW

BEGIN
  SELECT Ventas_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/