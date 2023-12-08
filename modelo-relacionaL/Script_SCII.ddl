-- Generated by Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   at:        2023-12-07 21:05:04 CST
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE departamentos (
    id_departamento    VARCHAR2(5 CHAR) NOT NULL,
    descripcion        VARCHAR2(100 CHAR),
    tbl_paises_id_pais NUMBER NOT NULL
);

ALTER TABLE departamentos ADD CONSTRAINT departamentos_pk PRIMARY KEY ( id_departamento );

CREATE TABLE tbl_album (
    id_album   NUMBER NOT NULL,
    id_artista NUMBER NOT NULL,
    id_grupo   NUMBER NOT NULL,
    nombre     VARCHAR2(50) NOT NULL,
    anio       NUMBER
);

ALTER TABLE tbl_album ADD CONSTRAINT tbl_album_pk PRIMARY KEY ( id_album );

CREATE TABLE tbl_artistas (
    id_artista     NUMBER NOT NULL,
    nombre_artista VARCHAR2(50) NOT NULL,
    descripcion    VARCHAR2(50) NOT NULL
);

ALTER TABLE tbl_artistas ADD CONSTRAINT tbl_artista_pk PRIMARY KEY ( id_artista );

CREATE TABLE tbl_audios (
    id_audio       NUMBER NOT NULL,
    id_artista     NUMBER NOT NULL,
    id_copyright   NUMBER NOT NULL,
    archivo_mp3    VARCHAR2(4000),
    titulo_cancion VARCHAR2(4000),
    portada        VARCHAR2(4000)
);

ALTER TABLE tbl_audios ADD CONSTRAINT tbl_audios_pk PRIMARY KEY ( id_audio );

CREATE TABLE tbl_canciones (
    id_cancion         NUMBER NOT NULL,
    id_artista         NUMBER NOT NULL,
    id_genero          NUMBER NOT NULL,
    id_grupo           NUMBER NOT NULL,
    nombre             VARCHAR2(50) NOT NULL,
    duracion           DATE NOT NULL,
    num_reproducciones NUMBER,
    descripcion        VARCHAR2(50) NOT NULL,
    fecha_subida       DATE
);

ALTER TABLE tbl_canciones ADD CONSTRAINT tbl_cancion_pk PRIMARY KEY ( id_cancion );

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

CREATE TABLE tbl_copyright (
    id_copyright NUMBER NOT NULL,
    id_cancion   NUMBER NOT NULL,
    id_artista   NUMBER NOT NULL
);

ALTER TABLE tbl_copyright ADD CONSTRAINT tbl_copyright_pk PRIMARY KEY ( id_copyright );

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

CREATE TABLE tbl_facturacion_pagos (
    id_facturacion        NUMBER NOT NULL,
    id_tipo_membresia     NUMBER NOT NULL,
    id_oyente             NUMBER NOT NULL,
    fecha_inicio          DATE,
    fecha_fin             DATE,
    monto                 NUMBER,
    descuento_facturacion NUMBER
);

ALTER TABLE tbl_facturacion_pagos ADD CONSTRAINT tbl_facturacion_pagos_pk PRIMARY KEY ( id_facturacion );

CREATE TABLE tbl_genero (
    id_genero          NUMBER NOT NULL,
    nombre             VARCHAR2(50) NOT NULL,
    descripcion_genero VARCHAR2(50)
);

ALTER TABLE tbl_genero ADD CONSTRAINT tbl_genero_pk PRIMARY KEY ( id_genero );

CREATE TABLE tbl_grupos (
    id_grupo     NUMBER NOT NULL,
    id_persona   NUMBER NOT NULL,
    nombre_banda VARCHAR2(50) NOT NULL,
    descripcion  VARCHAR2(100) NOT NULL
);

ALTER TABLE tbl_grupos ADD CONSTRAINT tbl_grupos_pk PRIMARY KEY ( id_grupo );

CREATE TABLE tbl_idiomas (
    id_idioma     NUMBER NOT NULL,
    nombre_idioma VARCHAR2(100),
    abreviatura   VARCHAR2(5)
);

ALTER TABLE tbl_idiomas ADD CONSTRAINT tbl_idiomas_pk PRIMARY KEY ( id_idioma );

CREATE TABLE tbl_letras_canciones (
    id_letra_cancion NUMBER NOT NULL,
    id_idioma        NUMBER NOT NULL,
    id_cancion       NUMBER NOT NULL,
    descripcion      VARCHAR2(100),
    archivo          BLOB
);

ALTER TABLE tbl_letras_canciones ADD CONSTRAINT tbl_letras_canciones_pk PRIMARY KEY ( id_letra_cancion );

CREATE TABLE tbl_likes (
    id_like    NUMBER NOT NULL,
    id_oyente  NUMBER NOT NULL,
    id_cancion NUMBER NOT NULL,
    fecha_like DATE
);

ALTER TABLE tbl_likes ADD CONSTRAINT tbl_likes_pk PRIMARY KEY ( id_like );

CREATE TABLE tbl_membresias (
    id_membresia      NUMBER NOT NULL,
    id_tipo_membresia NUMBER NOT NULL,
    fecha_inicio      DATE NOT NULL,
    fecha_vencimiento DATE NOT NULL
);

ALTER TABLE tbl_membresias ADD CONSTRAINT tbl_membresia_pk PRIMARY KEY ( id_membresia );

CREATE TABLE tbl_oyentes (
    id_oyente          NUMBER NOT NULL,
    descripcion_oyente VARCHAR2(50)
);

ALTER TABLE tbl_oyentes ADD CONSTRAINT tbl_oyentes_pk PRIMARY KEY ( id_oyente );

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

CREATE TABLE tbl_plataformas (
    id_plataforma     NUMBER NOT NULL,
    nombre_plataforma VARCHAR2(50),
    url_plataforma    VARCHAR2(50)
);

ALTER TABLE tbl_plataformas ADD CONSTRAINT tbl_plataformas_pk PRIMARY KEY ( id_plataforma );

CREATE TABLE tbl_playlist (
    id_playlist    NUMBER NOT NULL,
    id_oyente      NUMBER NOT NULL,
    nombre         VARCHAR2(30) NOT NULL,
    fecha_creacion NUMBER
);

ALTER TABLE tbl_playlist ADD CONSTRAINT tbl_playlist_pk PRIMARY KEY ( id_playlist );

CREATE TABLE tbl_shares (
    id_share      NUMBER NOT NULL,
    id_plataforma NUMBER NOT NULL,
    id_oyente     NUMBER NOT NULL,
    id_playlist   NUMBER NOT NULL,
    id_cancion    NUMBER NOT NULL,
    fecha_share   DATE
);

ALTER TABLE tbl_shares ADD CONSTRAINT tbl_shares_pk PRIMARY KEY ( id_share );

CREATE TABLE tbl_tipo_membresias (
    id_tipo_membresia NUMBER NOT NULL,
    basica            VARCHAR2(10),
    plata             VARCHAR2(10),
    oro               VARCHAR2(10),
    familiar          VARCHAR2(10),
    activo            CHAR(1)
);

ALTER TABLE tbl_tipo_membresias ADD CONSTRAINT tbl_tipo_membresia_pk PRIMARY KEY ( id_tipo_membresia );

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
    id_grupo        NUMBER NOT NULL,
    nombre_usuario  VARCHAR2(50 CHAR),
    fecha_registro  DATE NOT NULL,
    clave           VARCHAR2(30 CHAR)
);

ALTER TABLE tbl_usuarios ADD CONSTRAINT tbl_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE departamentos
    ADD CONSTRAINT departamentos_tbl_paises_fk FOREIGN KEY ( tbl_paises_id_pais )
        REFERENCES tbl_paises ( id_pais );

ALTER TABLE tbl_album
    ADD CONSTRAINT tbl_album_tb_artistas_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_artistas ( id_artista );

ALTER TABLE tbl_album
    ADD CONSTRAINT tbl_album_tbl_grupos_fk FOREIGN KEY ( id_grupo )
        REFERENCES tbl_grupos ( id_grupo );

ALTER TABLE tbl_artistas
    ADD CONSTRAINT tbl_artista_tbl_persona_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_personas ( id_persona );

ALTER TABLE tbl_audios
    ADD CONSTRAINT tbl_audios_tb_artistas_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_artistas ( id_artista );

ALTER TABLE tbl_audios
    ADD CONSTRAINT tbl_audios_tbl_copyright_fk FOREIGN KEY ( id_copyright )
        REFERENCES tbl_copyright ( id_copyright );

ALTER TABLE tbl_canciones_x_albumes
    ADD CONSTRAINT tbl_can_x_albm_tb_albm_fk FOREIGN KEY ( id_album )
        REFERENCES tbl_album ( id_album );

ALTER TABLE tbl_canciones_x_albumes
    ADD CONSTRAINT tbl_can_x_albm_tb_can_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_canciones_x_playlists
    ADD CONSTRAINT tbl_can_x_plts_tb_can_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_canciones_x_playlists
    ADD CONSTRAINT tbl_can_x_plts_tb_plts_fk FOREIGN KEY ( id_playlist )
        REFERENCES tbl_playlist ( id_playlist );

ALTER TABLE tbl_canciones
    ADD CONSTRAINT tbl_canciones_tb_artistas_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_artistas ( id_artista );

ALTER TABLE tbl_canciones
    ADD CONSTRAINT tbl_canciones_tb_genero_fk FOREIGN KEY ( id_genero )
        REFERENCES tbl_genero ( id_genero );

ALTER TABLE tbl_canciones
    ADD CONSTRAINT tbl_canciones_tbl_grupos_fk FOREIGN KEY ( id_grupo )
        REFERENCES tbl_grupos ( id_grupo );

ALTER TABLE tbl_ciudades
    ADD CONSTRAINT tbl_ciudades_departamentos_fk FOREIGN KEY ( departamentos_id_departamento )
        REFERENCES departamentos ( id_departamento );

ALTER TABLE tbl_copyright
    ADD CONSTRAINT tbl_copyright_tb_artistas_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_artistas ( id_artista );

ALTER TABLE tbl_copyright
    ADD CONSTRAINT tbl_copyright_tb_canciones_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_direccion
    ADD CONSTRAINT tbl_direccion_tbl_ciudades_fk FOREIGN KEY ( id_ciudad )
        REFERENCES tbl_ciudades ( id_ciudad );

ALTER TABLE tbl_escuchas
    ADD CONSTRAINT tbl_escuchas_tb_canciones_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_escuchas
    ADD CONSTRAINT tbl_escuchas_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tbl_oyentes ( id_oyente );

ALTER TABLE tbl_facturacion_pagos
    ADD CONSTRAINT tbl_fact_pag_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tbl_oyentes ( id_oyente );

ALTER TABLE tbl_facturacion_pagos
    ADD CONSTRAINT tbl_fact_pag_tb_tp_memb_fk FOREIGN KEY ( id_tipo_membresia )
        REFERENCES tbl_tipo_membresias ( id_tipo_membresia );

ALTER TABLE tbl_grupos
    ADD CONSTRAINT tbl_grupos_tbl_personas_fk FOREIGN KEY ( id_persona )
        REFERENCES tbl_personas ( id_persona );

ALTER TABLE tbl_letras_canciones
    ADD CONSTRAINT tbl_let_can_tb_can_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_letras_canciones
    ADD CONSTRAINT tbl_let_can_tbl_idiom_fk FOREIGN KEY ( id_idioma )
        REFERENCES tbl_idiomas ( id_idioma );

ALTER TABLE tbl_likes
    ADD CONSTRAINT tbl_likes_tb_canciones_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_likes
    ADD CONSTRAINT tbl_likes_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tbl_oyentes ( id_oyente );

ALTER TABLE tbl_membresias
    ADD CONSTRAINT tbl_memb_tbl_tp_memb_fk FOREIGN KEY ( id_tipo_membresia )
        REFERENCES tbl_tipo_membresias ( id_tipo_membresia );

ALTER TABLE tbl_playlist
    ADD CONSTRAINT tbl_playlist_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tbl_oyentes ( id_oyente );

ALTER TABLE tbl_shares
    ADD CONSTRAINT tbl_shares_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tbl_oyentes ( id_oyente );

ALTER TABLE tbl_shares
    ADD CONSTRAINT tbl_shares_tb_playlist_fk FOREIGN KEY ( id_playlist )
        REFERENCES tbl_playlist ( id_playlist );

ALTER TABLE tbl_shares
    ADD CONSTRAINT tbl_shares_tbl_canciones_fk FOREIGN KEY ( id_cancion )
        REFERENCES tbl_canciones ( id_cancion );

ALTER TABLE tbl_shares
    ADD CONSTRAINT tbl_shares_tbl_plataformas_fk FOREIGN KEY ( id_plataforma )
        REFERENCES tbl_plataformas ( id_plataforma );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usr_tbl_tp_usr_fk FOREIGN KEY ( id_tipo_usuario )
        REFERENCES tbl_tipo_usuario ( id_tipo_usuario );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuario_tb_artista_fk FOREIGN KEY ( id_artista )
        REFERENCES tbl_artistas ( id_artista );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuario_tb_membresia_fk FOREIGN KEY ( id_membresia )
        REFERENCES tbl_membresias ( id_membresia );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuario_tbl_persona_fk FOREIGN KEY ( id_usuario )
        REFERENCES tbl_personas ( id_persona );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuarios_tb_oyentes_fk FOREIGN KEY ( id_oyente )
        REFERENCES tbl_oyentes ( id_oyente );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuarios_tbl_direccion_fk FOREIGN KEY ( id_direccion )
        REFERENCES tbl_direccion ( id_direccion );

ALTER TABLE tbl_usuarios
    ADD CONSTRAINT tbl_usuarios_tbl_grupos_fk FOREIGN KEY ( id_grupo )
        REFERENCES tbl_grupos ( id_grupo );



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                            27
-- CREATE INDEX                             0
-- ALTER TABLE                             66
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