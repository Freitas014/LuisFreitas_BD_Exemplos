select cliente.NomeCliente, cliente.CodCliente, item_pedido.NumPedido from cliente join pedido
on cliente.CodCliente = pedido.CodCliente join item_pedido on pedido.NumPedido = item_pedido.NumPedido