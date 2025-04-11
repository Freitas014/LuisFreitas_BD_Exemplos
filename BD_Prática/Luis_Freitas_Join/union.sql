select * from cliente1 left join profissao on cliente1.Cod_Profissao = profissao.Cod_Profissao
union
select * from cliente1 right join profissao on cliente1.Cod_Profissao = profissao.Cod_Profissao
where cliente1.Cod_Profissao is null;