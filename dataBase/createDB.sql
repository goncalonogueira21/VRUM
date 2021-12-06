CREATE DATABASE vrum;

USE vrum;

/* Lógico_1: */

CREATE TABLE Carro (
    ano int,
    tipoFuel varchar(255),
    cor varchar(255),
    matricula varchar(255) PRIMARY KEY,
    modelo varchar(255),
    lugares int,
    fk_Utilizador_username varchar(255)
);

CREATE TABLE Avaliacoes (
    conteudo varchar(255),
    dataAvaliacao datetime,
    utilizador varchar(255),
    fk_Viagem_idViagem int
);

CREATE TABLE Viagem (
    dataInicio DateTime,
    kmsViagem float,
    custo float,
    localInicio varchar(255),
    bagagem boolean,
    localDestino varchar(255),
    lugaresDisp int,
    regularidade varchar(255),
    idViagem int PRIMARY KEY,
    custoMinimo float,
    idCondutor varchar(255),
    fk_Carro_matricula varchar(255)
);

CREATE TABLE Pedido (
    nrPessoas int,
    localFinal varchar(255),
    idPedido int PRIMARY KEY,
    pickupLocal varchar(255),
    aceite boolean,
    fk_Utilizador_username varchar(255),
    fk_Viagem_idViagem int
);

CREATE TABLE Utilizador (
    rating int,
    email varchar(255),
    nrTelemovel int,
    morada varchar(255),
    username varchar(255) PRIMARY KEY,
    password varchar(255),
    dataNascimento DateTime
);

CREATE TABLE usufrui (
    fk_Utilizador_username varchar(255),
    fk_Viagem_idViagem int,
    custoPago varchar(255)
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