create table item(
	CodItem integer not null primary key,
    CodCompra integer,
    CodProd integer,
    Quantidade integer,
 Foreign key (CodCompra) references compra(CodCompra),
 foreign key (CodProd) references produto(CodProd)
 );