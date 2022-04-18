CREATE TABLE "pessoa_fisica"(
    "id_pf" INTEGER NOT NULL,
    "cpf" INTEGER NOT NULL,
    "nome_pf" TEXT NOT NULL,
    "rg" INTEGER NOT NULL,
    "endereco" TEXT NOT NULL,
    "telefone" INTEGER NOT NULL,
    "email" TEXT NOT NULL
);
ALTER TABLE
    "pessoa_fisica" ADD PRIMARY KEY("id_pf");
CREATE TABLE "pessoa_jurídica"(
    "id_pj" INTEGER NOT NULL,
    "cnpj" INTEGER NOT NULL,
    "nome_pj" TEXT NOT NULL,
    "endereco" TEXT NOT NULL,
    "telefone" INTEGER NOT NULL,
    "email" TEXT NOT NULL,
    "incricao_estadual" INTEGER NOT NULL
);
ALTER TABLE
    "pessoa_jurídica" ADD PRIMARY KEY("id_pj");
CREATE TABLE "endereco"(
    "endereco" TEXT NOT NULL,
    "id_pf" INTEGER NOT NULL,
    "id_pj" INTEGER NOT NULL,
    "id_imovel" INTEGER NOT NULL
);
ALTER TABLE
    "endereco" ADD PRIMARY KEY("endereco");
CREATE TABLE "telefone"(
    "telefone" INTEGER NOT NULL,
    "id_pf" INTEGER NOT NULL,
    "id_pj" INTEGER NOT NULL
);
ALTER TABLE
    "telefone" ADD PRIMARY KEY("telefone");
CREATE TABLE "email"(
    "email" TEXT NOT NULL,
    "id_pf" INTEGER NOT NULL,
    "id_pj" INTEGER NOT NULL
);
ALTER TABLE
    "email" ADD PRIMARY KEY("email");
CREATE TABLE "imovel"(
    "id_imovel" INTEGER NOT NULL,
    "matricula" INTEGER NOT NULL,
    "endereco" TEXT NOT NULL,
    "metragem" DOUBLE PRECISION NOT NULL,
    "inscricao_municipal" INTEGER NOT NULL
);
ALTER TABLE
    "imovel" ADD PRIMARY KEY("id_imovel");
CREATE TABLE "contrato"(
    "id_contrato" INTEGER NOT NULL,
    "locador" INTEGER NOT NULL,
    "locatario" INTEGER NOT NULL,
    "imovel" INTEGER NOT NULL,
    "duracao" INTEGER NOT NULL,
    "valor" INTEGER NOT NULL,
    "forma_pagamento" INTEGER NOT NULL
);
ALTER TABLE
    "contrato" ADD PRIMARY KEY("id_contrato");
CREATE INDEX "contrato_locador_index" ON
    "contrato"("locador");
CREATE INDEX "contrato_locatario_index" ON
    "contrato"("locatario");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_locador_foreign" FOREIGN KEY("locador") REFERENCES "pessoa_fisica"("id_pf");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_locador_foreign" FOREIGN KEY("locador") REFERENCES "pessoa_jurídica"("id_pj");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_locatario_foreign" FOREIGN KEY("locatario") REFERENCES "pessoa_jurídica"("id_pj");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_locatario_foreign" FOREIGN KEY("locatario") REFERENCES "pessoa_fisica"("id_pf");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_imovel_foreign" FOREIGN KEY("imovel") REFERENCES "imovel"("id_imovel");
ALTER TABLE
    "endereco" ADD CONSTRAINT "endereco_id_imovel_foreign" FOREIGN KEY("id_imovel") REFERENCES "imovel"("id_imovel");
ALTER TABLE
    "imovel" ADD CONSTRAINT "imovel_endereco_foreign" FOREIGN KEY("endereco") REFERENCES "endereco"("endereco");
ALTER TABLE
    "email" ADD CONSTRAINT "email_id_pf_foreign" FOREIGN KEY("id_pf") REFERENCES "pessoa_fisica"("id_pf");
ALTER TABLE
    "telefone" ADD CONSTRAINT "telefone_id_pf_foreign" FOREIGN KEY("id_pf") REFERENCES "pessoa_fisica"("id_pf");
ALTER TABLE
    "endereco" ADD CONSTRAINT "endereco_id_pf_foreign" FOREIGN KEY("id_pf") REFERENCES "pessoa_fisica"("id_pf");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_endereco_foreign" FOREIGN KEY("endereco") REFERENCES "endereco"("endereco");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_telefone_foreign" FOREIGN KEY("telefone") REFERENCES "telefone"("telefone");
ALTER TABLE
    "pessoa_fisica" ADD CONSTRAINT "pessoa_fisica_email_foreign" FOREIGN KEY("email") REFERENCES "email"("email");
ALTER TABLE
    "telefone" ADD CONSTRAINT "telefone_id_pj_foreign" FOREIGN KEY("id_pj") REFERENCES "pessoa_jurídica"("id_pj");
ALTER TABLE
    "endereco" ADD CONSTRAINT "endereco_id_pj_foreign" FOREIGN KEY("id_pj") REFERENCES "pessoa_jurídica"("id_pj");
ALTER TABLE
    "email" ADD CONSTRAINT "email_id_pj_foreign" FOREIGN KEY("id_pj") REFERENCES "pessoa_jurídica"("id_pj");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_endereco_foreign" FOREIGN KEY("endereco") REFERENCES "endereco"("endereco");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_telefone_foreign" FOREIGN KEY("telefone") REFERENCES "telefone"("telefone");
ALTER TABLE
    "pessoa_jurídica" ADD CONSTRAINT "pessoa_jurídica_email_foreign" FOREIGN KEY("email") REFERENCES "email"("email");