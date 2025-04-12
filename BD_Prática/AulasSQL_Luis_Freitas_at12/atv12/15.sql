select sum(produto.valor * item.quantidade) as total_compras from cliente join compra on cliente.cpf = compra.cpf join item on
item.CodCompra = compra.CodCompra join produto on item.CodProd = produto.CodProd 
where cliente.cidade = 'Curitiba';
