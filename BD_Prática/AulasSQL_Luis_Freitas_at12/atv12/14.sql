select distinct cliente.nome, cliente.cidade from cliente join compra on cliente.cpf = compra.cpf join item on
item.CodCompra = compra.CodCompra join produto on item.CodProd = produto.CodProd 
where cliente.cidade = 'Curitiba' and item.quantidade > 5;
