CREATE DATABASE `sedb` DEFAULT CHARACTER SET utf8mb4;

USE `sedb`;

CREATE TABLE `test_result` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `TimeStamp` DATETIME(3) DEFAULT 0,
  `Browser` char(32) NOT NULL DEFAULT '',
  `BrowserVersion` char(32) NOT NULL DEFAULT '',
  `MetaVersion` char(32) NOT NULL DEFAULT '',
  `Result` char(32) NOT NULL DEFAULT '',
  `URL` char(32) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `step_result` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `TimeStamp` DATETIME(3) DEFAULT 0,
  `ParentTimeStamp` DATETIME(3) DEFAULT 0,
  `ElementID` char(32) NOT NULL DEFAULT '',
  `URL` char(32) NOT NULL DEFAULT '',
  `StepName` char(32) NOT NULL DEFAULT '',
  `StepResult` char(32) NOT NULL DEFAULT '',
  `StepText` varchar(256) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

