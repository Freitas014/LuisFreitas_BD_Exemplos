select cliente.nome, cliente.profissao from cliente join compra 
on cliente.cpf = compra.cpf join item on compra.codcompra = item.codcompra join produto on item.codprod = produto.codprod 
where produto.descricao in ('Leite', 'Queijo')
group by cliente.cpf, cliente.nome, cliente.profissao
having COUNT(distinct produto.descricao) = 2
order by cliente.nome asc;
