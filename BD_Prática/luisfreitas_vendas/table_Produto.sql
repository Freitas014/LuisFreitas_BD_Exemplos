create table produto(
	CodProduto integer not null,
    uniProduto varchar(10),
    descProduto varchar(50),
    valorUnitario decimal (10,2),
constraint pk_produto primary key (CodProduto)
);