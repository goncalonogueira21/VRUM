-- -----------------------------------------------------
-- Schema VRUM
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `vrum` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `vrum` ;

-- -----------------------------------------------------
-- Table `VRUM`.`utilizador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`utilizador` (
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `firstName` VARCHAR(45) NOT NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `nrTelemovel` VARCHAR(9) NOT NULL,
  `rating` INT NOT NULL,
  `morada` VARCHAR(45) NOT NULL,
  `dataNascimento` DATE NOT NULL,
  `avatar` VARBINARY(8000) NOT NULL,
  `aboutME` VARCHAR(200) NULL,
  PRIMARY KEY (`username`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VRUM`.`carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`carro` (
  `matricula` VARCHAR(45) NOT NULL,
  `fk_Utilizador_username` VARCHAR(45) NOT NULL,
  `modelo` VARCHAR(45) NOT NULL,
  `ano` INT NOT NULL,
  `tipoFuel` VARCHAR(45) NOT NULL,
  `cor` VARCHAR(45) NOT NULL,
  `lugares` INT NOT NULL,
  `foto` VARBINARY(8000) NULL,
  PRIMARY KEY (`matricula`),
  INDEX `FK_Carro_2` (`fk_Utilizador_username` ASC) VISIBLE,
  CONSTRAINT `FK_Carro_2`
    FOREIGN KEY (`fk_Utilizador_username`)
    REFERENCES `vrum`.`utilizador` (`username`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VRUM`.`viagem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`viagem` (
  `idViagem` INT NOT NULL AUTO_INCREMENT,
  `fk_Carro_matricula` VARCHAR(45) NOT NULL,
  `dataInicio` DATETIME NOT NULL,
  `kmsViagem` FLOAT NOT NULL,
  `custoPessoa` FLOAT NOT NULL,
  `localInicio` VARCHAR(45) NOT NULL,
  `bagagem` TINYINT(1) NOT NULL,
  `localDestino` VARCHAR(45) NOT NULL,
  `nrLugares` INT NOT NULL,
  `lugaresDisp` INT NOT NULL,
  `regularidade` VARCHAR(45) NOT NULL,
  `idCondutor` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(200) NULL,
  PRIMARY KEY (`idViagem`),
  INDEX `FK_Viagem_2` (`fk_Carro_matricula` ASC) VISIBLE,
  CONSTRAINT `FK_Viagem_2`
    FOREIGN KEY (`fk_Carro_matricula`)
    REFERENCES `vrum`.`carro` (`matricula`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VRUM`.`avaliacoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`avaliacoes` (
  `idAvaliacao` INT NOT NULL AUTO_INCREMENT,
  `fk_Viagem_idViagem` INT NOT NULL,
  `conteudo` VARCHAR(45) NOT NULL,
  `dataAvaliacao` DATETIME NOT NULL,
  `utilizador` VARCHAR(45) NOT NULL,
  INDEX `FK_Avaliacoes_1` (`fk_Viagem_idViagem` ASC) VISIBLE,
  PRIMARY KEY (`idAvaliacao`),
  CONSTRAINT `FK_Avaliacoes_1`
    FOREIGN KEY (`fk_Viagem_idViagem`)
    REFERENCES `vrum`.`viagem` (`idViagem`)
    ON DELETE CASCADE
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VRUM`.`pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `fk_Utilizador_username` VARCHAR(45) NOT NULL,
  `fk_Viagem_idViagem` INT NOT NULL,
  `nrPessoas` INT NOT NULL,
  `pickupLocal` VARCHAR(45) NOT NULL,
  `localDestino` VARCHAR(45) NOT NULL,
  `aceite` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idPedido`),
  INDEX `FK_Pedido_2` (`fk_Utilizador_username` ASC) VISIBLE,
  INDEX `FK_Pedido_3` (`fk_Viagem_idViagem` ASC) VISIBLE,
  CONSTRAINT `FK_Pedido_2`
    FOREIGN KEY (`fk_Utilizador_username`)
    REFERENCES `vrum`.`utilizador` (`username`)
    ON DELETE CASCADE,
  CONSTRAINT `FK_Pedido_3`
    FOREIGN KEY (`fk_Viagem_idViagem`)
    REFERENCES `vrum`.`viagem` (`idViagem`)
    )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VRUM`.`usufrui`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`usufrui` (
  `fk_Utilizador_username` VARCHAR(45) NOT NULL,
  `fk_Viagem_idViagem` INT NOT NULL,
  `custoPago` FLOAT NOT NULL,
  INDEX `FK_usufrui_1` (`fk_Utilizador_username` ASC) VISIBLE,
  INDEX `FK_usufrui_2` (`fk_Viagem_idViagem` ASC) VISIBLE,
  CONSTRAINT `FK_usufrui_1`
    FOREIGN KEY (`fk_Utilizador_username`)
    REFERENCES `vrum`.`utilizador` (`username`)
    ON DELETE RESTRICT,
  CONSTRAINT `FK_usufrui_2`
    FOREIGN KEY (`fk_Viagem_idViagem`)
    REFERENCES `vrum`.`viagem` (`idViagem`)
    )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `VRUM`.`mensagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`mensagens` (
  `idMensagens` INT NOT NULL AUTO_INCREMENT,
  `conteudo` VARCHAR(250) NOT NULL,
  `userOrigem` VARCHAR(45) NOT NULL,
  `userDestino` VARCHAR(45) NOT NULL,
  `data` DATETIME NOT NULL,
  PRIMARY KEY (`idMensagens`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VRUM`.`mailBox`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vrum`.`mailBox` (
  `idMailBox` INT NOT NULL AUTO_INCREMENT,
  `fk_Utilizador_username` VARCHAR(45) NOT NULL,
  `fk_Mensagens_idMensagens` INT NOT NULL,
  `mailbox` VARCHAR(45) NOT NULL,
  INDEX `fk_mailBox_Utilizador1_idx` (`fk_Utilizador_username` ASC) VISIBLE,
  INDEX `fk_mailBox_Mensagens1_idx` (`fk_Mensagens_idMensagens` ASC) VISIBLE,
  PRIMARY KEY (`idMailBox`),
  CONSTRAINT `fk_mailBox_Utilizador1`
    FOREIGN KEY (`fk_Utilizador_username`)
    REFERENCES `vrum`.`utilizador` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mailBox_Mensagens1`
    FOREIGN KEY (`fk_Mensagens_idMensagens`)
    REFERENCES `vrum`.`mensagens` (`idMensagens`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;