create table func(
	nrMatric integer not null,
    nmFunc varchar(35),
    dtAdm date,
    sexo char,
    cdCargo integer,
    cdDepto integer,
constraint pk_func primary key(nrMatric),
constraint fk_func_cdCargo foreign key(cdCargo) references cargo(cdCargo),
constraint fk_func_cdDepto foreign key(cdDepto) references depto(cdDepto)
);