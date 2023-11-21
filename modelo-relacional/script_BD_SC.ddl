-- Generado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   en:        2023-11-21 00:07:02 CST
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE departamentos (
    id_departamento    VARCHAR2(5 CHAR) NOT NULL,
    descripcion        VARCHAR2(100 CHAR),
    tbl_paises_id_pais NUMBER NOT NULL
);

ALTER TABLE departamentos ADD CONSTRAINT departamentos_pk PRIMARY KEY ( id_departamento );

CREATE TABLE tb_album (
    id_album   NUMBER NOT NULL,
    id_artista NUMBER NOT NULL,
    nombre     VARCHAR2(50) NOT NULL,
    anio       NUMBER
);

ALTER TABLE tb_album ADD CONSTRAINT tb_album_pk PRIMARY KEY ( id_album );

CREATE TABLE tb_artistas (
    id_artista  NUMBER NOT NULL,
    descripcion VARCHAR2(50) NOT NULL
);

ALTER TABLE tb_artistas ADD CONSTRAINT tb_artista_pk PRIMARY KEY ( id_artista );

CREATE TABLE tb_canciones (
    id_cancion         NUMBER NOT NULL,
    id_artista         NUMBER NOT NULL,
    id_genero          NUMBER NOT NULL,
    nombre             VARCHAR2(50) NOT NULL,
    duracion           DATE NOT NULL,
    num_reproducciones NUMBER,
    descripcion        VARCHAR2(50) NOT NULL,
    fecha_subida       DATE
);

ALTER TABLE tb_canciones ADD CONSTRAINT tb_cancion_pk PRIMARY KEY ( id_cancion );

CREATE TABLE tb_genero (
    id_genero          NUMBER NOT NULL,
    nombre             VARCHAR2(50) NOT NULL,
    descripcion_genero VARCHAR2(50)
);

ALTER TABLE tb_genero ADD CONSTRAINT tb_genero_pk PRIMARY KEY ( id_genero );

CREATE TABLE tb_membresias (
    id_membresia      NUMBER NOT NULL,
    id_tipo_membresia NUMBER NOT NULL,
    fecha_inicio      DATE NOT NULL,
    fecha_vencimiento DATE NOT NULL
);

ALTER TABLE tb_membresias ADD CONSTRAINT tb_membresia_pk PRIMARY KEY ( id_membresia );

CREATE TABLE tb_oyentes (
    id_oyente          NUMBER NOT NULL,
    descripcion_oyente VARCHAR2(50)
);

ALTER TABLE tb_oyentes ADD CONSTRAINT tb_oyentes_pk PRIMARY KEY ( id_oyente );

CREATE TABLE tb_playlist (
    id_playlist    NUMBER NOT NULL,
    id_oyente      NUMBER NOT NULL,
    nombre         VARCHAR2(30) NOT NULL,
    fecha_creacion NUMBER
);

ALTER TABLE tb_playlist ADD CONSTRAINT tb_playlist_pk PRIMARY KEY ( id_playlist );

CREATE TABLE tb_tipo_membresias (
    id_tipo_membresia NUMBER NOT NULL,
    basica            VARCHAR2(10),
    plata             VARCHAR2(10),
    oro               VARCHAR2(10),
    familiar          VARCHAR2(10),
    activo            CHAR(1)
);

ALTER TABLE tb_tipo_membresias ADD CONSTRAINT tb_tipo_membresia_pk PRIMARY KEY ( id_tipo_membresia );

CREATE TABLE tbl_canciones_x_albumes (
    id_cancion_x_album NUMBER NOT NULL,
    id_cancion         NUMBER NOT NULL,
    id_album           NUMBER NOT NULL
);

ALTER TABLE tbl_canciones_x_albumes ADD CONSTRAINT tbl_canciones_x_albumes_pk PRIMARY KEY ( id_cancion_x_album );

CREATE TABLE tbl_canciones_x_playlists (
    id_cancion_x_playlist NUMBER NOT NULL,
    id_playlist           NUMBER NOT NULL,
    id_cancion            NUMBER NOT NULL
);

ALTER TABLE tbl_canciones_x_playlists ADD CONSTRAINT tbl_canciones_x_playlists_pk PRIMARY KEY ( id_cancion_x_playlist );

CREATE TABLE tbl_ciudades (
    id_ciudad                     VARCHAR2(30 CHAR) NOT NULL,
    descripcion                   VARCHAR2(100 CHAR),
    departamentos_id_departamento VARCHAR2(5 CHAR) NOT NULL
);

ALTER TABLE tbl_ciudades ADD CONSTRAINT tbl_ciudades_pk PRIMARY KEY ( id_ciudad );

CREATE TABLE tbl_direccion (
    id_direccion VARCHAR2(100) NOT NULL,
    id_ciudad    VARCHAR2(30 CHAR) NOT NULL,
    pais         VARCHAR2(30)
);

ALTER TABLE tbl_direccion ADD CONSTRAINT tbl_direccion_pk PRIMARY KEY ( id_direccion );

CREATE TABLE tbl_escuchas (
    id_escucha    NUMBER NOT NULL,
    id_oyente     NUMBER NOT NULL,
    id_cancion    NUMBER NOT NULL,
    fecha_escucha DATE NOT NULL
);

ALTER TABLE tbl_escuchas ADD CONSTRAINT tbl_escuchas_pk PRIMARY KEY ( id_escucha );

CREATE TABLE tbl_likes (
    id_like    NUMBER NOT NULL,
    id_oyente  NUMBER NOT NULL,
    id_cancion NUMBER NOT NULL,
    fecha_like DATE
);

ALTER TABLE tbl_likes ADD CONSTRAINT tbl_likes_pk PRIMARY KEY ( id_like );

CREATE TABLE tbl_paises (
    id_pais     NUMBER NOT NULL,
    nombre_pais VARCHAR2(50) NOT NULL
);

ALTER TABLE tbl_paises ADD CONSTRAINT tbl_paises_pk PRIMARY KEY ( id_pais );

CREATE TABLE tbl_personas (
    id_persona          NUMBER NOT NULL,
    nombre              VARCHAR2(30),
    apellido            VARCHAR2(30),
    fecha_de_nacimiento DATE,
    correo              VARCHAR2(30),
    telefono            NUMBER
);

ALTER TABLE tbl_personas ADD CONSTRAINT tbl_persona_pk PRIMARY KEY ( id_persona );

CREATE TABLE tbl_tipo_usuario (
    id_tipo_usuario NUMBER NOT NULL,
    oyente          VARCHAR2(30 CHAR) NOT NULL,
    admin           VARCHAR2(30 CHAR) NOT NULL,
    artista         VARCHAR2(30) NOT NULL
);

ALTER TABLE tbl_tipo_usuario ADD CONSTRAINT tbl_tipo_usuario_pk PRIMARY KEY ( id_tipo_usuario );

CREATE TABLE tbl_usuarios (
    id_usuario      NUMBER NOT NULL,
    id_tipo_usuario NUMBER NOT NULL,
    id_membresia    NUMBER NOT NULL,
    id_artista      NUMBER NOT NULL,
    id_oyente       NUMBER NOT NULL,
    id_direccion    VARCHAR2(100) NOT NULL,
    nombre_usuario  VARCHAR2(50 CHAR),
    fecha_registro  DATE NOT NULL,
    clave           VARCHAR2(30 CHAR)
);

ALTER TABLE tbl_usuarios ADD CONSTRAINT tbl_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE departamentos
    ADD CONSTRAINT departamentos_tbl_paises_fk FOREIGN KEY ( tbl_paises_id_pais )
        REFERENCES tbl_paises ( id_pais );

ALTER TABLE tb_album
    ADD CONSTRAINT tb_album_tb_artistas_fk FOREIGN KEY ( id_artista )
        REFERENCES tb_artistas ( id_artista );

ALTER TABLE tb_artistas
    ADD CONSTRAINT tb_artista_tbl_persona_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_personas ( id_persona );

ALTER TABLE tb_canciones
    ADD CONSTRAINT tb_canciones_tb_artistas_fk FOREIGN KEY ( id_artista )
        REFERENCES tb_artistas ( id_artista );

ALTER TABLE tb_canciones
    ADD CONSTRAINT tb_canciones_tb_genero_fk FOREIGN KEY ( id_genero )
        REFERENCES tb_genero ( id_genero );

ALTER TABLE tb_membresias
    ADD CONSTRAINT tb_mbs_tb_tipo_mbs_fk FOREIGN KEY ( id_tipo_membresia )
        REFERENCES tb_tipo_membresias ( id_tipo_membresia );

ALTER TABLE tb_playlist
    ADD CONSTRAINT tb_playlist_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tb_oyentes ( id_oyente );

ALTER TABLE tbl_ciudades
    ADD CONSTRAINT tbl_ciudades_departamentos_fk FOREIGN KEY ( departamentos_id_departamento )
        REFERENCES departamentos ( id_departamento );

ALTER TABLE tbl_canciones_x_albumes
    ADD CONSTRAINT tbl_cs_x_alb_tb_alb_fk FOREIGN KEY ( id_album )
        REFERENCES tb_album ( id_album );

ALTER TABLE tbl_canciones_x_albumes
    ADD CONSTRAINT tbl_cs_x_alb_tb_cs_fk FOREIGN KEY ( id_cancion )
        REFERENCES tb_canciones ( id_cancion );

ALTER TABLE tbl_canciones_x_playlists
    ADD CONSTRAINT tbl_cs_x_plylt_tb_cs_fk FOREIGN KEY ( id_cancion )
        REFERENCES tb_canciones ( id_cancion );

ALTER TABLE tbl_canciones_x_playlists
    ADD CONSTRAINT tbl_cs_x_plylt_tb_plylt_fk FOREIGN KEY ( id_playlist )
        REFERENCES tb_playlist ( id_playlist );

ALTER TABLE tbl_direccion
    ADD CONSTRAINT tbl_direccion_tbl_ciudades_fk FOREIGN KEY ( id_ciudad )
        REFERENCES tbl_ciudades ( id_ciudad );

ALTER TABLE tbl_escuchas
    ADD CONSTRAINT tbl_escuchas_tb_canciones_fk FOREIGN KEY ( id_cancion )
        REFERENCES tb_canciones ( id_cancion );

ALTER TABLE tbl_escuchas
    ADD CONSTRAINT tbl_escuchas_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tb_oyentes ( id_oyente );

ALTER TABLE tbl_likes
    ADD CONSTRAINT tbl_likes_tb_canciones_fk FOREIGN KEY ( id_cancion )
        REFERENCES tb_canciones ( id_cancion );

ALTER TABLE tbl_likes
    ADD CONSTRAINT tbl_likes_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tb_oyentes ( id_oyente );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usr_tbl_tipo_usr_fk FOREIGN KEY ( id_tipo_usuario )
        REFERENCES tbl_tipo_usuario ( id_tipo_usuario );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuario_tb_artista_fk FOREIGN KEY ( id_artista )
        REFERENCES tb_artistas ( id_artista );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuario_tb_membresia_fk FOREIGN KEY ( id_membresia )
        REFERENCES tb_membresias ( id_membresia );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuario_tbl_persona_fk FOREIGN KEY ( id_usuario )
        REFERENCES tbl_personas ( id_persona );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuarios_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tb_oyentes ( id_oyente );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuarios_tbl_direccion_fk FOREIGN KEY ( id_direccion )
        REFERENCES tbl_direccion ( id_direccion );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            19
-- CREATE INDEX                             0
-- ALTER TABLE                             42
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
