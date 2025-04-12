select cliente.Nome from cliente join compra on cliente.CPF = compra.CPF join item 
on item.CodCompra = compra.CodCompra join produto on item.CodProd = produto.CodProd 
where produto.Descricao='Queijo' and item.Quantidade > 23;