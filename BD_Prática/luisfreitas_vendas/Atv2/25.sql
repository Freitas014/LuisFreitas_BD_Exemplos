select produto.descProduto, item_pedido.NumPedido, item_pedido.QtdeProduto from produto join item_pedido 
on produto.CodProduto = item_pedido.CodProduto join pedido on item_pedido.NumPedido = pedido.NumPedido;
