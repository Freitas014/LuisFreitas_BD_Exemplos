select compra.Data_Compra, cliente.nome from cliente join compra on cliente.cpf = compra.cpf
where month(compra.data_compra) in (1,2);