select produto.lote, produto.validade, produto.descricao, item.quantidade from produto
left join item on produto.codprod = item.codprod
where item.codcompra is null;