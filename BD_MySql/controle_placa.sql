create database controle_placa;

create table historico(
	
	data_hora datetime,
	placa varchar(8),
	permitido char
);

create table usuario(

login varchar(10),
senha varchar(10)

);

create table cadastro(

ID_Carro integer PRIMARY KEY AUTO_INCREMENT,
modelo varchar(20),
marca varchar(20),
placa varchar(8),
cor varchar(10)

);

insert into cadastro(modelo, marca, placa, cor) value();

insert into usuario(login, senha)
values("python", "123456");

insert into usuario(login, senha)
values("vinicius", "654321");

SELECT * FROM usuario
where login = "vinicius" and senha = "654321";

INSERT INTO placas(placa)
VALUES("FQF9941");

INSERT INTO placas(placa)
VALUES("ABC1234");

INSERT INTO historico(placa) VALUES('ABC1284');

INSERT INTO historico(data_hora, placa, permitido) VALUES (NOW(), 'ATS1356', 'x'); 

DELETE FROM historico WHERE placa = 'PXS1444';


