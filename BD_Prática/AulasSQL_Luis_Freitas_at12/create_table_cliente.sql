create table cliente(
	CPF integer not null,
    Nome varchar(48),
    Rua varchar(30),
    Numero integer,
    Bairro varchar(30),
    Cidade varchar(20),
    UF char(2),
    Sexo char(1),
    Profissao varchar(50),
constraint pk_cliente primary key (CPF)
);