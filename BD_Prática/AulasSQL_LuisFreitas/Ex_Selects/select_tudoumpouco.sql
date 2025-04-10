select Nr_Depto, avg(salario) as salario_avg from colaborador_tarde group by Nr_Depto having avg(salario) 
> (select avg(salario) from colaborador_tarde);