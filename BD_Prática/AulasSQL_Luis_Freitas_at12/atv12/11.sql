select cliente.nome, cliente.profissao, cliente.sexo from cliente join compra on cliente.cpf = compra.cpf join
item on compra.codcompra = item.codcompra join produto on item.codprod = produto.codprod 
where produto.descricao ='Leite' and (item.quantidade > 10) and (produto.valor between 1.00 and 4.75);