CREATE TABLE "cadastro"(
    "id_cadastro" INTEGER NOT NULL,
    "pessoa_física" TEXT NOT NULL,
    "pessoa_juridica" TEXT NOT NULL,
    "imovel" INTEGER NOT NULL,
    "contrato" INTEGER NOT NULL
);
ALTER TABLE
    "cadastro" ADD PRIMARY KEY("id_cadastro");
CREATE INDEX "cadastro_pessoa_física_index" ON
    "cadastro"("pessoa_física");
CREATE INDEX "cadastro_pessoa_juridica_index" ON
    "cadastro"("pessoa_juridica");
CREATE INDEX "cadastro_imovel_index" ON
    "cadastro"("imovel");
CREATE INDEX "cadastro_contrato_index" ON
    "cadastro"("contrato");
CREATE TABLE "pessoa_fisica"(
    "id_cadastro" INTEGER NOT NULL,
    "cpf" INTEGER NOT NULL,
    "nomepf" TEXT NOT NULL,
    "rg" TEXT NOT NULL,
    "endereco" TEXT NOT NULL,
    "telefone" INTEGER NOT NULL,
    "email" INTEGER NOT NULL
);
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_id_cadastro_unique" UNIQUE("id_cadastro");
ALTER TABLE
    "pessoa_fisica" ADD PRIMARY KEY("cpf");
CREATE INDEX "pessoa_fisica_nomepf_index" ON
    "pessoa_fisica"("nomepf");
CREATE INDEX "pessoa_fisica_rg_index" ON
    "pessoa_fisica"("rg");
CREATE TABLE "pessoa_jurídica"(
    "id_cadastro" INTEGER NOT NULL,
    "cnpj" INTEGER NOT NULL,
    "nomepj" INTEGER NOT NULL,
    "endereco" TEXT NOT NULL,
    "telefone" INTEGER NOT NULL,
    "email" INTEGER NOT NULL,
    "incricao_estadual" INTEGER NOT NULL
);
ALTER TABLE
    "pessoa_jurídica" ADD PRIMARY KEY("id_cadastro");
CREATE INDEX "pessoa_jurídica_cnpj_index" ON
    "pessoa_jurídica"("cnpj");
CREATE INDEX "pessoa_jurídica_nomepj_index" ON
    "pessoa_jurídica"("nomepj");
CREATE TABLE "endereco"(
    "id_cadastro" INTEGER NOT NULL,
    "endereco" TEXT NOT NULL
);
ALTER TABLE
    "endereco" ADD CONSTRAINT "endereco_id_cadastro_unique" UNIQUE("id_cadastro");
ALTER TABLE
    "endereco" ADD PRIMARY KEY("endereco");
CREATE TABLE "telefone"(
    "id_cadastro" INTEGER NOT NULL,
    "telefone" INTEGER NOT NULL
);
ALTER TABLE
    "telefone" ADD CONSTRAINT "telefone_id_cadastro_unique" UNIQUE("id_cadastro");
ALTER TABLE
    "telefone" ADD PRIMARY KEY("telefone");
CREATE TABLE "email"(
    "id_cadastro" INTEGER NOT NULL,
    "email" TEXT NOT NULL
);
ALTER TABLE
    "email" ADD CONSTRAINT "email_id_cadastro_unique" UNIQUE("id_cadastro");
ALTER TABLE
    "email" ADD PRIMARY KEY("email");
CREATE TABLE "imovel"(
    "id_cadastro" INTEGER NOT NULL,
    "matricula" INTEGER NOT NULL,
    "endereco" INTEGER NOT NULL,
    "metragem" INTEGER NOT NULL,
    "inscricao_municipal" INTEGER NOT NULL,
    "id_proprietario" INTEGER NOT NULL
);
ALTER TABLE
    "imovel" ADD CONSTRAINT "imovel_id_cadastro_unique" UNIQUE("id_cadastro");
ALTER TABLE
    "imovel" ADD PRIMARY KEY("matricula");
CREATE INDEX "imovel_endereco_index" ON
    "imovel"("endereco");
CREATE INDEX "imovel_metragem_index" ON
    "imovel"("metragem");
CREATE INDEX "imovel_inscricao_municipal_index" ON
    "imovel"("inscricao_municipal");
CREATE INDEX "imovel_id_proprietario_index" ON
    "imovel"("id_proprietario");
CREATE TABLE "contrato"(
    "id_cadastro" INTEGER NOT NULL,
    "locador" INTEGER NOT NULL,
    "locatario" INTEGER NOT NULL,
    "duracao" INTEGER NOT NULL,
    "termos_e_condicoes" INTEGER NOT NULL,
    "valor" INTEGER NOT NULL,
    "forma_pagamento" INTEGER NOT NULL
);
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_id_cadastro_unique" UNIQUE("id_cadastro");
ALTER TABLE
    "contrato" ADD PRIMARY KEY("locador");
ALTER TABLE
    "contrato" ADD PRIMARY KEY("locatario");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "cadastro"("id_cadastro");
ALTER TABLE
    "cadastro" ADD CONSTRAINT "cadastro_pessoa_física_foreign" FOREIGN KEY("pessoa_física") REFERENCES "pessoa_fisica"("cpf");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_nomepf_foreign" FOREIGN KEY("nomepf") REFERENCES "contrato"("locador");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_cnpj_foreign" FOREIGN KEY("cnpj") REFERENCES "contrato"("locador");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_nomepj_foreign" FOREIGN KEY("nomepj") REFERENCES "contrato"("locador");
ALTER TABLE
    "cadastro" ADD CONSTRAINT "cadastro_pessoa_física_foreign" FOREIGN KEY("pessoa_física") REFERENCES "contrato"("locador");
ALTER TABLE
    "cadastro" ADD CONSTRAINT "cadastro_pessoa_física_foreign" FOREIGN KEY("pessoa_física") REFERENCES "contrato"("locador");
ALTER TABLE
    "cadastro" ADD CONSTRAINT "cadastro_pessoa_juridica_foreign" FOREIGN KEY("pessoa_juridica") REFERENCES "contrato"("locador");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_nomepf_foreign" FOREIGN KEY("nomepf") REFERENCES "contrato"("locatario");
ALTER TABLE
    "cadastro" ADD CONSTRAINT "cadastro_pessoa_juridica_foreign" FOREIGN KEY("pessoa_juridica") REFERENCES "contrato"("locatario");
ALTER TABLE
    "imovel" ADD CONSTRAINT "imovel_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "cadastro"("id_cadastro");
ALTER TABLE
    "imovel" ADD CONSTRAINT "imovel_endereco_foreign" FOREIGN KEY("endereco") REFERENCES "endereco"("endereco");
ALTER TABLE
    "imovel" ADD CONSTRAINT "imovel_id_proprietario_foreign" FOREIGN KEY("id_proprietario") REFERENCES "cadastro"("id_cadastro");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "cadastro"("id_cadastro");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_endereco_foreign" FOREIGN KEY("endereco") REFERENCES "endereco"("endereco");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_telefone_foreign" FOREIGN KEY("telefone") REFERENCES "telefone"("telefone");
ALTER TABLE
    "endereco" ADD CONSTRAINT "endereco_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "pessoa_jurídica"("id_cadastro");
ALTER TABLE
    "email" ADD CONSTRAINT "email_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "pessoa_jurídica"("id_cadastro");
ALTER TABLE
    "telefone" ADD CONSTRAINT "telefone_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "pessoa_jurídica"("id_cadastro");
ALTER TABLE
    "imovel" ADD CONSTRAINT "imovel_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "pessoa_jurídica"("id_cadastro");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_id_cadastro_foreign" FOREIGN KEY("id_cadastro") REFERENCES "pessoa_jurídica"("id_cadastro");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_endereco_foreign" FOREIGN KEY("endereco") REFERENCES "endereco"("endereco");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_telefone_foreign" FOREIGN KEY("telefone") REFERENCES "telefone"("telefone");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_email_foreign" FOREIGN KEY("email") REFERENCES "email"("email");