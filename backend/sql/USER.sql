CREATE USER C##SOUNDCLOUD
  IDENTIFIED BY "root1234"
  DEFAULT TABLESPACE USERS
  TEMPORARY TABLESPACE TEMP;

--asignar cuota ilimitada al tablespace por defecto
ALTER USER C##SOUNDCLOUD QUOTA UNLIMITED ON USERS;

--Asignar privilegios basicos
GRANT CREATE SESSION TO C##SOUNDCLOUD;
GRANT CREATE TABLE TO C##SOUNDCLOUD;
GRANT CREATE VIEW TO C##SOUNDCLOUD;
GRANT CREATE ANY TRIGGER TO C##SOUNDCLOUD;
GRANT CREATE ANY PROCEDURE TO C##SOUNDCLOUD;
GRANT CREATE SEQUENCE TO C##SOUNDCLOUD;
GRANT CREATE SYNONYM TO C##SOUNDCLOUD;