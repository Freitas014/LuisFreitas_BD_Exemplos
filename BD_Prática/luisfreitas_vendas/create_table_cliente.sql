create table cliente(
	CodCliente integer not null, 
    NomeCliente varchar(50),
    Endereco varchar(80),
    Cidade varchar(50),
    CEP varchar(10),
    UF char(2),
    CNPJ varchar(30),
    InscEstadual integer (10),
constraint pk_cliente primary key (CodCliente)
);