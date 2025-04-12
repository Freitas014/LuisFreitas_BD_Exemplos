select produto.descricao, produto.lote from cliente join compra on cliente.cpf = compra.cpf join item 
on compra.codcompra = item.codcompra join produto on item.codprod = produto.codprod
where item.quantidade = 4;