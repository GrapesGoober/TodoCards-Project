DROP DATABASE IF EXISTS TodoCards;
CREATE DATABASE TodoCards;
USE TodoCards;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `card` (
  `cardID` int(10) NOT NULL,
  `deckID` int(10) NOT NULL,
  `cardName` varchar(50) NOT NULL,
  `cardDescription` text NOT NULL,
  `cardDue` date NOT NULL,
  `cardIsFinished` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

CREATE TABLE `deck` (
  `deckID` int(10) NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

CREATE TABLE `subcard` (
  `scardID` int(10) NOT NULL,
  `cardID` int(10) NOT NULL,
  `scardName` varchar(50) NOT NULL,
  `scardDescription` text NOT NULL,
  `scardDue` date NOT NULL,
  `scardIsFinished` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ---------------------------------------------------
ALTER TABLE `card`
  ADD PRIMARY KEY (`cardID`),
  ADD KEY `deckID` (`deckID`);

ALTER TABLE `deck`
  ADD PRIMARY KEY (`deckID`),
  ADD UNIQUE KEY `deckName` (`deckName`);


ALTER TABLE `subcard`
  ADD PRIMARY KEY (`scardID`),
  ADD KEY `cardID` (`cardID`);

ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deckID`) REFERENCES `deck` (`deckID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `subcard`
  ADD CONSTRAINT `subcard_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `card` (`cardID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
