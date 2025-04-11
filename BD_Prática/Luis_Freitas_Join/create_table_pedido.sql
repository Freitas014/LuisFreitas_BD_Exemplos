create table pedido(
	Num_Pedido integer not null,
    Cod_Cliente integer,
    Tot_Pedido decimal(10,2),
primary key (Num_Pedido),
foreign key (Cod_Cliente) references cliente1(Cod_Cliente)
);
    