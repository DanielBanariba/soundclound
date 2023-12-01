--Crea un directorio en la base de datos para el audio (Aqui es donde tiene que ir el directiorio del proyecto)
CREATE DIRECTORY SOUNDS_AND_VOICES AS 'C:\Users\banar\Desktop\soundclound\backend\audios';
GRANT READ, WRITE ON DIRECTORY SOUNDS_AND_VOICES TO HR;

--Nos permite ver si pudimos crear excitosamennte el directorio
SELECT * FROM DBA_DIRECTORIES;

--Crea la tabla donde se va almacenar los audios
CREATE TABLE AUDIOS(
    id NUMBER PRIMARY KEY,
    TITULO_CANCION VARCHAR2(4000),
    PORTADA VARCHAR2(4000),
    archivo_mp3 VARCHAR2(4000)
);

-- Consulta para ver si se creo la tabla
SELECT * FROM system.AUDIOS;
DROP TABLE system.AUDIOS;

--Crea la secuencia para el id de la tabla
CREATE SEQUENCE id_audios_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

-- Consulta para ver si se creo la secuencia
SELECT table_name FROM all_tables WHERE table_name = 'AUDIOS';

select table_name, owner from all_tables where table_name = 'AUDIOS'
