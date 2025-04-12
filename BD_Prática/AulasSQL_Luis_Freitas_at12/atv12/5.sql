select cliente.Nome, cliente.Cidade, cliente.Sexo from cliente where cliente.Cidade like 'G%' 
or cliente.Cidade like 'C%' and cliente.Sexo = 'M';
