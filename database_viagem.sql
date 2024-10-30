CREATE DATABASE viagem;

CREATE TABLE cidade(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(50),
	pais VARCHAR(50)
);

CREATE TABLE pessoa(
	id INTEGER PRIMARY KEY,
	nome VARCHAR(50),
	sobrenome VARCHAR(50),
	ano_nascimento INTEGER,
	sexo CHAR, 
	ano_formacao_superior INTEGER,
	cidade_nasceu INTEGER,
	FOREIGN KEY (cidade_nasceu) REFERENCES cidade(id)
);

CREATE TABLE viagem(
	id_pessoa INTEGER,
	id_cidade INTEGER,
	data DATE,
	custo FLOAT,
	PRIMARY KEY (id_pessoa, id_cidade),
	FOREIGN KEY (id_pessoa) REFERENCES pessoa(id),
	FOREIGN KEY (id_cidade) REFERENCES cidade(id)
);

SELECT * FROM cidade;