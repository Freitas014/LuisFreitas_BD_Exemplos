create table compra(
	CodCompra integer not null,
    CPF integer,
    Data_Compra date,
    Tipo_Pagamento char(1),
constraint pk_compra primary key(CodCompra),
constraint fk_compra_CPF foreign key(CPF) references cliente(CPF)
);