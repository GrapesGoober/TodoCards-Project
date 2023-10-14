DROP DATABASE IF EXISTS TodoCards;
CREATE DATABASE TodoCards;
USE TodoCards;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `card` (
  `cardid` int(11) NOT NULL,
  `deckID` int(10) NOT NULL,
  `cardName` varchar(50) NOT NULL,
  `cardDescription` text NOT NULL,
  `cardDue` date NOT NULL,
  `cardIsFinished` tinyint(1) NOT NULL,
  `cardcolor` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



INSERT INTO `card` (`cardid`, `deckID`, `cardName`, `cardDescription`, `cardDue`, `cardIsFinished`, `cardcolor`) VALUES
(1, 1, 'Write introduction', '200 words zuzu', '2023-10-17', 0, 'lightblue'),
(2, 1, 'Write abstract', '500 words zuzu', '2023-11-17', 0, 'pink'),
(3, 1, 'Cleaning', 'clean bathroom', '2023-11-15', 0, 'lightgreen');


CREATE TABLE `deck` (
  `deckid` int(11) NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



INSERT INTO `deck` (`deckid`, `deckName`, `deckDescription`) VALUES
(1, 'QuickDeck', 'This is the default deck.');



CREATE TABLE `subcard` (
  `scardid` int(11) NOT NULL,
  `cardID` int(10) NOT NULL,
  `scardName` varchar(50) NOT NULL,
  `scardDescription` text NOT NULL,
  `scardDue` date NOT NULL,
  `scardIsFinished` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



INSERT INTO `subcard` (`scardid`, `cardID`, `scardName`, `scardDescription`, `scardDue`, `scardIsFinished`) VALUES
(1, 1, 'write intro', 'make it formal', '2023-11-01', 0),
(2, 2, 'find motivation(to do this work)', 'just go to temple', '2023-11-01', 0);


ALTER TABLE `card`
  ADD PRIMARY KEY (`cardid`),
  ADD KEY `deckID` (`deckID`);


ALTER TABLE `deck`
  ADD PRIMARY KEY (`deckid`),
  ADD UNIQUE KEY `deckName` (`deckName`);


ALTER TABLE `subcard`
  ADD PRIMARY KEY (`scardid`),
  ADD KEY `cardID` (`cardID`);


ALTER TABLE `card`
  MODIFY `cardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;


ALTER TABLE `deck`
  MODIFY `deckid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;


ALTER TABLE `subcard`
  MODIFY `scardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;




ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deckID`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE `subcard`
  ADD CONSTRAINT `subcard_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `card` (`cardid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

