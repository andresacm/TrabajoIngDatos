CREATE TABLE Colaboradores(
  id NUMBER(7) PRIMARY KEY,
  id_Win NUMBER(7) NOT NULL,
  nombre VARCHAR2(20) NOT NULL,
  ApellidoPaterno VARCHAR2(15) NOT NULL,
  ApellidoMaterno VARCHAR2(15) NOT NULL,
  Correo VARCHAR2(50) NOT NULL,
  FechaNacimiento DATE NOT NULL,
  Telefono NUMBER(9) NOT NULL,
  FechaIngreso DATE NOT NULL,
  EstadoWIN VARCHAR2(2) NOT NULL,
  EstadoSUMMUN VARCHAR2(2) NOT NULL,
  Feedback VARCHAR2(100) NOT NULL,
  NumeroDocumento NUMBER(9) NOT NULL,
  Genero_id NUMBER(2) not null,
  Equipo_id NUMBER(2) not null,
  TipoDocumento_id NUMBER(2) not null,
  TipoComision_id NUMBER(2) not null,
  TipoContrato_id NUMBER(2) not null,
  Nacionalidad_id NUMBER(2) not null,
  TipoColaborador_id NUMBER(2) not null,
  Categoria_id NUMBER(2) not null,
  Distrito_id NUMBER(2) not null,
  FOREIGN KEY (Genero_id) REFERENCES Generos,
  FOREIGN KEY (Equipo_id) REFERENCES Equipos,
  FOREIGN KEY (TipoDocumento_id) REFERENCES TiposDocumento,
  FOREIGN KEY (TipoComision_id) REFERENCES TiposComision,
  FOREIGN KEY (TipoContrato_id) REFERENCES TiposContrato,
  FOREIGN KEY (Nacionalidad_id) REFERENCES Nacionalidades,
  FOREIGN KEY (TipoColaborador_id) REFERENCES TiposColaborador,
  FOREIGN KEY (Categoria_id) REFERENCES Categorias,
  FOREIGN KEY (Distrito_id) REFERENCES Distritos
);

ALTER TABLE Colaboradores ADD (
  CONSTRAINT Colaboradores_pk PRIMARY KEY (id));

CREATE SEQUENCE Colaboradores_seq START WITH 1;

CREATE OR REPLACE TRIGGER Colaboradores_pk 
BEFORE INSERT ON Colaboradores 
FOR EACH ROW

BEGIN
  SELECT Colaboradores_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/