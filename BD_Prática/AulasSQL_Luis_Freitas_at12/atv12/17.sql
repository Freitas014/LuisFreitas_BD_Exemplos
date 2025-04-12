select distinct produto.lote, cliente.nome, cliente.cidade from cliente join compra on cliente.cpf = compra.cpf 
join item on compra.CodCompra = item.CodCompra join produto on item.CodProd = produto.CodProd
where cliente.cidade = 'Guarapuava';