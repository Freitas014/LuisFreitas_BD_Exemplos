select cliente.nome, produto.descricao, compra.Data_Compra, item.quantidade from cliente join compra 
on cliente.cpf = compra.cpf join item on item.CodCompra = compra.CodCompra join produto 
on item.codprod = produto.codprod where produto.Descricao = 'Queijo';