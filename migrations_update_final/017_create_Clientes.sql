CREATE TABLE Clientes(
  id NUMBER(7) PRIMARY KEY,
  nombre VARCHAR2(30) NOT NULL,
  ApellidoPaterno VARCHAR2(30) NOT NULL,
  ApellidoMaterno VARCHAR2(30) NOT NULL,
  Correo VARCHAR2(60) NOT NULL,
  Telefono NUMBER(9) NOT NULL,
  NumeroDocumento NUMBER(9) NOT NULL,
  TipoDocumento_id NUMBER(7) not null,
  FOREIGN KEY (TipoDocumento_id) REFERENCES TiposDocumento
);

ALTER TABLE Clientes ADD (
  CONSTRAINT Clientes_pk PRIMARY KEY (id));

CREATE SEQUENCE Clientes_seq START WITH 1;

CREATE OR REPLACE TRIGGER Clientes_pk 
BEFORE INSERT ON Clientes 
FOR EACH ROW

BEGIN
  SELECT Clientes_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/