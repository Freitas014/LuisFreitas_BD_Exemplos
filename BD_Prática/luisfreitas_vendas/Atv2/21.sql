select item_pedido.NumPedido ,produto.descProduto, produto.CodProduto from cliente join pedido on cliente.CodCliente = pedido.CodCliente
join item_pedido on pedido.NumPedido = item_pedido.NumPedido join produto on item_pedido.CodProduto = produto.CodProduto
where descProduto = 'Vinho' 