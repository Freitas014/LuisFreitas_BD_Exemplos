select cliente.NomeCliente, item_pedido.NumPedido, item_pedido.QtdeProduto from cliente join pedido 
on cliente.CodCliente = pedido.CodCliente join item_pedido on pedido.NumPedido = item_pedido.NumPedido
where item_pedido.QtdeProduto > 3;