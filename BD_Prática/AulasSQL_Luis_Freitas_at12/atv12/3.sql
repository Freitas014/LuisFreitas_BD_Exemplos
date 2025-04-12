select distinct cliente.cidade from cliente join compra on cliente.CPF = compra.CPF join item 
on compra.Codcompra = item.CodCompra join produto on item.CodProd = produto.CodProd
where produto.Validade < 2025-07-11;
