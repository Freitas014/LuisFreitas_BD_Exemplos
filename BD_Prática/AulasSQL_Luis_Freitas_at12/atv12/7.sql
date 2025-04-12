select distinct cliente.nome, produto.descricao, item.quantidade from cliente join compra on cliente.cpf = compra.cpf
join item on compra.codcompra = item.codcompra join produto on item.codprod = produto.codprod
where (produto.descricao = 'Queijo' and item.quantidade > 5) 
or (produto.descricao = 'Leite' and item.quantidade > 3)