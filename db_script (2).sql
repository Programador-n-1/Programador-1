create database ispc_proyectointegrador;
use ispc_proyectointegrador;
CREATE TABLE CATEGORIA
(
 id_categoria    integer NOT NULL auto_increment PRIMARY KEY,
 categoria varchar(50) NOT NULL

);
CREATE TABLE TIPO_NORMATIVA
(
 id_tipo_normativa        integer NOT NULL auto_increment PRIMARY KEY,
 normativa varchar(50) NOT NULL
);
CREATE TABLE ORGANO_LEGISLATIVO
(
 id_organo     integer NOT NULL auto_increment PRIMARY KEY,
 organo varchar(50) NOT NULL

);
CREATE TABLE JURISDICCION
(
 id_jurisdiccion    integer NOT NULL auto_increment PRIMARY KEY,
 poder                 varchar(50) NOT NULL,
 id_organo integer NOT NULL,

 CONSTRAINT FK_5 FOREIGN KEY (id_organo) REFERENCES ORGANO_LEGISLATIVO ( id_organo )
);


CREATE TABLE NORMATIVA
(
 id_normativa         integer NOT NULL auto_increment PRIMARY KEY,
 fecha                 date NOT NULL,
 descripcion           varchar(425) NOT NULL,
 nro_normativa         integer NOT NULL,
 id_tipo_normativa     integer NOT NULL,
 id_categoria          integer NOT NULL,
 id_jurisdiccion       integer NOT NULL,
 id_organo integer NOT NULL,
 palabras_clave varchar(255) NOT NULL,

 CONSTRAINT FK_1 FOREIGN KEY ( id_tipo_normativa ) REFERENCES TIPO_NORMATIVA ( id_tipo_normativa ),
 CONSTRAINT FK_2 FOREIGN KEY ( id_categoria ) REFERENCES CATEGORIA ( id_categoria ),
 CONSTRAINT FK_3 FOREIGN KEY ( id_jurisdiccion ) REFERENCES JURISDICCION ( id_jurisdiccion ),
 CONSTRAINT FK_4 FOREIGN KEY ( id_organo ) REFERENCES JURISDICCION ( id_organo )
);

create table USUARIO (Id int not null auto_increment primary key, usuario varchar(255) not null, permisos varchar(255) not null);
insert into USUARIO (usuario, permisos) values ('admin', 'todos');
insert into USUARIO (usuario, permisos) values ('user', 'lectura');

insert into ORGANO_LEGISLATIVO (organo) values ('Congreso de la Nación');
insert into ORGANO_LEGISLATIVO (organo) values ('Legislatura de Córdoba');

insert into JURISDICCION (poder, id_organo) values ('Nacional', 1);
insert into JURISDICCION (poder, id_organo) values ('Provincial', 2);

insert into TIPO_NORMATIVA (normativa) values ('Ley');
insert into TIPO_NORMATIVA (normativa) values ('Decreto');
insert into TIPO_NORMATIVA (normativa) values ('Resolución');

insert into CATEGORIA (categoria) values ('Laboral');
insert into CATEGORIA (categoria) values ('Penal');
insert into CATEGORIA (categoria) values ('Civil');
insert into CATEGORIA (categoria) values ('Comercial');
insert into CATEGORIA (categoria) values ('Familia y Sucesiones');
insert into CATEGORIA (categoria) values ('Agrario y Ambiental');
insert into CATEGORIA (categoria) values ('Minería');
insert into CATEGORIA (categoria) values ('Derecho Informático');


INSERT INTO NORMATIVA (nro_normativa, fecha, descripcion, id_tipo_normativa, id_categoria, id_jurisdiccion, id_organo, palabras_clave) 
VALUES (20744, 27/09/21974, "Ley de Contrato de Trabajo:Establece los derechos y obligaciones de empleadores y empleados. Regula la jornada laboral, salarios, descansos y vacaciones. Protege contra la discriminación y establece licencias por maternidad y enfermedad. Establece indemnizaciones por despido y procedimientos para la terminación del contrato. Reconoce los derechos sindicales y la negociación colectiva.", 1, 1, 1, 1, "trabajo, empleado, remuneracion, jornada, aportes");
INSERT INTO NORMATIVA (nro_normativa, fecha, descripcion, id_tipo_normativa, id_categoria, id_jurisdiccion, id_organo, palabras_clave) 
VALUES (27555, 30/07/2020, "Ley de Teletrabajo. Ley del Teletrabajo tiene como objetivo regular esta modalidad de prestación de servicios tanto en las entidades públicas como en las empresas privadas, estableciendo un marco de trabajo entre las labores profesionales y la vida personal.", 1, 1, 1, 1, "contrato, teletrabajo, distancia, tic, jornada, derechos");
INSERT INTO NORMATIVA (nro_normativa, fecha, descripcion, id_tipo_normativa, id_categoria, id_jurisdiccion, id_organo, palabras_clave) 
VALUES (7642, 10/01/1998, "Regula las condiciones para el ejercicio profesional de ciencias informaticas  en Cordoba y la constitucion del consejo de profesionales.", 1, 8, 2, 2, "profesional, cordoba, informatica, colegio, derechos");