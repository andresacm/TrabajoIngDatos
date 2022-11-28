CREATE TABLE Colaboradores_Bancos(
  id NUMBER(7) PRIMARY KEY,
  CC VARCHAR2(30) NOT NULL,
  CCI VARCHAR2(20) NOT NULL,
  Colaborador_id NUMBER(7) not null,
  Banco_id NUMBER(7) not null,
  FOREIGN KEY (Colaborador_id) REFERENCES Colaboradores,
  FOREIGN KEY (Banco_id) REFERENCES Bancos
);

ALTER TABLE Colaboradores_Bancos ADD (
  CONSTRAINT Colaboradores_Bancos_pk PRIMARY KEY (id));

CREATE SEQUENCE Colaboradores_Bancos_seq START WITH 1;

CREATE OR REPLACE TRIGGER Colaboradores_Bancos_pk 
BEFORE INSERT ON Colaboradores_Bancos 
FOR EACH ROW

BEGIN
  SELECT Colaboradores_Bancos_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/