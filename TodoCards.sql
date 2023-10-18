DROP DATABASE IF EXISTS TodoCards;
CREATE DATABASE TodoCards;
USE TodoCards;

--
-- Database: `todocards`
--

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `cardid` int(11) NOT NULL,
  `deckID` int(10) NOT NULL,
  `cardName` varchar(50) NOT NULL,
  `cardDescription` text NOT NULL,
  `cardDue` date NOT NULL,
  `cardIsFinished` tinyint(1) NOT NULL,
  `cardcolor` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `card`
--

INSERT INTO `card` (`cardid`, `deckID`, `cardName`, `cardDescription`, `cardDue`, `cardIsFinished`, `cardcolor`) VALUES
(1, 1, 'Write introduction', '200 words zuzu', '2023-10-17', 0, 'lightblue'),
(2, 1, 'Write abstract', '500 words zuzu', '2023-11-17', 0, 'pink'),
(3, 1, 'Cleaning', 'clean bathroom', '2023-11-15', 0, 'lightgreen');

-- --------------------------------------------------------

--
-- Table structure for table `deck`
--

CREATE TABLE `deck` (
  `deckid` int(11) NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `deck`
--

INSERT INTO `deck` (`deckid`, `deckName`, `deckDescription`) VALUES
(1, 'QuickDeck', 'This is the default deck.');

-- --------------------------------------------------------

--
-- Table structure for table `subcard`
--

CREATE TABLE `subcard` (
  `scardid` int(11) NOT NULL,
  `cardID` int(10) NOT NULL,
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
  ADD PRIMARY KEY (`deckid`),
  ADD UNIQUE KEY `deckName` (`deckName`);

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
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deckID`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subcard`
--
ALTER TABLE `subcard`
  ADD CONSTRAINT `subcard_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `card` (`cardid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

