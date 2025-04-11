create table cliente1 (
Cod_Cliente integer not null,
Nome_Cliente varchar(60) not null,
Data_Nascimento date,
Telefone char(9),
Cod_Profissao integer,
primary key (Cod_Cliente),
foreign key (Cod_Profissao) references profissao (Cod_Profissao)
);