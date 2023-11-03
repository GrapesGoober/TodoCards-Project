DROP DATABASE IF EXISTS TodoCards;
CREATE DATABASE TodoCards;
USE TodoCards;

--
-- Database: `todocards`
--

-- Table for `user`
CREATE TABLE `user` (
    `username` varchar(20) PRIMARY KEY,
    `password` varchar(20) NOT NULL
  );

-- Table for `access`
CREATE TABLE `access` (
    `accessId` int(11) PRIMARY KEY,
    `username` varchar(20) NOT NULL,
    `deckId` int(11) NOT NULL,
    `accessType` varchar(4) NOT NULL
  );

-- Table for `share`
CREATE TABLE `share` (
    `code` varchar(20) PRIMARY KEY,
    `deckId` int(11) NOT NULL,
    `type` varchar(4) NOT NULL,
    `expires` datetime NOT NULL
    );

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `cardId` int(11) NOT NULL,
  `deckId` int(11) NOT NULL,
  `cardName` varchar(50) NOT NULL,
  `cardDescription` text NOT NULL,
  `cardDue` date NOT NULL,
  `cardIsFinished` tinyint(1) NOT NULL,
  `cardColor` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `card`
--

INSERT INTO `card` (`cardId`, `deckId`, `cardName`, `cardDescription`, `cardDue`, `cardIsFinished`, `cardColor`) VALUES
(1, 1, 'Write introduction', '200 words zuzu', '2023-10-17', 0, 'lightblue'),
(2, 1, 'Write abstract', '500 words zuzu', '2023-11-17', 0, 'pink'),
(3, 1, 'Cleaning', 'clean bathroom', '2023-11-15', 0, 'lightgreen');

-- --------------------------------------------------------

--
-- Table structure for table `deck`
--

CREATE TABLE `deck` (
  `deckId` int(11) NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `deck`
--

INSERT INTO `deck` (`deckId`, `deckName`, `deckDescription`) VALUES
(1, 'QuickDeck', 'This is the default deck.');

-- --------------------------------------------------------

--
-- Table structure for table `subcard`
--

CREATE TABLE `subcard` (
  `scardid` int(11) NOT NULL,
  `cardID` int(11) NOT NULL,
  `scardName` varchar(50) NOT NULL,
  `scardIsFinished` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subcard`
--

INSERT INTO `subcard` (`scardid`, `cardID`, `scardName`, `scardIsFinished`) VALUES
(1, 1, 'write intro', 0),
(2, 2, 'find motivation(to do this work)', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`cardid`),
  ADD KEY `deckID` (`deckID`);

--
-- Indexes for table `deck`
--
ALTER TABLE `deck`
  ADD PRIMARY KEY (`deckid`);

--
-- Indexes for table `subcard`
--
ALTER TABLE `subcard`
  ADD PRIMARY KEY (`scardid`),
  ADD KEY `cardID` (`cardID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `card`
--
ALTER TABLE `card`
  MODIFY `cardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `deck`
--
ALTER TABLE `deck`
  MODIFY `deckid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `subcard`
--
ALTER TABLE `subcard`
  MODIFY `scardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `card`
--
ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subcard`
--
ALTER TABLE `subcard`
  ADD CONSTRAINT `subcard_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `card` (`cardid`) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Constraints for table `access`
--
ALTER TABLE `access`
  ADD CONSTRAINT `access_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `access_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;


--
-- Constraints for table `share`
--
ALTER TABLE `share`
  ADD CONSTRAINT `share_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckId`) ON DELETE CASCADE ON UPDATE CASCADE;

COMMIT;

