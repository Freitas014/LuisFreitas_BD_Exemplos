select item.quantidade, cliente.cidade, cliente.nome from cliente join compra on cliente.CPF = compra.CPF join item on compra.CodCompra = item.CodCompra join produto on item.codprod = produto.CodProd
where (produto.descricao = 'Queijo') and (cliente.cidade = 'Guarapuava');
