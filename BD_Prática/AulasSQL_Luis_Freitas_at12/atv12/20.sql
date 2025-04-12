select distinct compra.Data_Compra, item.quantidade, cliente.cidade, cliente.nome from cliente join compra on cliente.CPF = compra.CPF 
join item on compra.CodCompra = item.CodCompra join produto on item.codprod = produto.CodProd
where (produto.descricao = 'Leite') and (cliente.cidade = 'Guarapuava' or cliente.cidade ='Curitiba');