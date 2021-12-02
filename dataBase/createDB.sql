CREATE DATABASE user_authentication;

USE user_authentication;

/* Lógico_1: */

CREATE TABLE Carro (
    ano int,
    tipoFuel varchar,
    cor varchar,
    matricula varchar PRIMARY KEY,
    modelo varchar,
    lugares int,
    fk_Utilizador_username varchar
);

CREATE TABLE Avaliacoes (
    conteudo varchar,
    dataAvaliacao datetime,
    utilizador varchar,
    fk_Viagem_idViagem int
);

CREATE TABLE Viagem (
    dataInicio DateTime,
    kmsViagem float,
    custo float,
    localInicio varchar,
    bagagem boolean,
    localDestino varchar,
    lugaresDisp int,
    regularidade varchar,
    idViagem int PRIMARY KEY,
    custoMinimo float,
    idCondutor varchar,
    fk_Carro_matricula varchar
);

CREATE TABLE Pedido (
    nrPessoas int,
    localFinal varchar,
    idPedido int PRIMARY KEY,
    pickupLocal varchar,
    aceite boolean,
    fk_Utilizador_username varchar,
    fk_Viagem_idViagem int
);

CREATE TABLE Utilizador (
    rating int,
    email varchar,
    nrTelemovel int,
    morada varchar,
    username varchar PRIMARY KEY,
    password varchar,
    dataNascimento DateTime
);

CREATE TABLE usufrui (
    fk_Utilizador_username varchar,
    fk_Viagem_idViagem int,
    custoPago varchar
);

ALTER TABLE Carro ADD CONSTRAINT FK_Carro_2
    FOREIGN KEY (fk_Utilizador_username)
    REFERENCES Utilizador (username)
    ON DELETE CASCADE;

ALTER TABLE Avaliacoes ADD CONSTRAINT FK_Avaliacoes_1
    FOREIGN KEY (fk_Viagem_idViagem)
    REFERENCES Viagem (idViagem)
    ON DELETE CASCADE;

ALTER TABLE Viagem ADD CONSTRAINT FK_Viagem_2
    FOREIGN KEY (fk_Carro_matricula)
    REFERENCES Carro (matricula)
    ON DELETE CASCADE;

ALTER TABLE Pedido ADD CONSTRAINT FK_Pedido_2
    FOREIGN KEY (fk_Utilizador_username)
    REFERENCES Utilizador (username)
    ON DELETE CASCADE;

ALTER TABLE Pedido ADD CONSTRAINT FK_Pedido_3
    FOREIGN KEY (fk_Viagem_idViagem)
    REFERENCES Viagem (idViagem)
    ON DELETE SET NULL;

ALTER TABLE usufrui ADD CONSTRAINT FK_usufrui_1
    FOREIGN KEY (fk_Utilizador_username)
    REFERENCES Utilizador (username)
    ON DELETE RESTRICT;

ALTER TABLE usufrui ADD CONSTRAINT FK_usufrui_2
    FOREIGN KEY (fk_Viagem_idViagem)
    REFERENCES Viagem (idViagem)
    ON DELETE SET NULL;