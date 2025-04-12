select cliente.nome, cliente.cidade, compra.data_compra, compra.Tipo_Pagamento, item.quantidade, produto.descricao
from cliente join compra on cliente.cpf = compra.cpf join item on compra.codcompra = item.codcompra join produto 
on item.codprod = produto.codprod order by cliente.nome desc;
