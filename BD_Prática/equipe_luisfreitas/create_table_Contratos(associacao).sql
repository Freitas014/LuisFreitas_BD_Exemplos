create table contratos(
	cdJogador integer not null,
    cdTime integer not null,
	dtRecisao integer not null,
    dtContrato integer not null,
constraint pk_contratos primary key (cdJogador, cdTime),
constraint fk_contratos_cdJogador foreign key (cdJogador) references Jogadores(cdJogador),
constraint fk_contratos_cdTime foreign key (cdTime) references Times(cdTime)
);
	