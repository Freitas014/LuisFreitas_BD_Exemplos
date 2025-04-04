create table colaborador_tarde(
	Cod_Colaborador int not null,
    Primeiro_Nome varchar(40) not null,
    Ultimo_Nome varchar(40) not null,
    Ramal int not null,
    Data_Admissao date not null,
	Nr_Depto int not null,
    Cod_Funcao varchar(40) not null,
    Grau_funcao int not null,
    Local_Trabalho varchar(40) not null,
    Salario double not null,
    Nome_Completo varchar(80) not null,
constraint pk_Colaborador_Tarde primary key(Cod_Colaborador)
) engine = InnoDB;