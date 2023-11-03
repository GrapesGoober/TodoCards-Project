DROP DATABASE IF EXISTS TodoCards;
CREATE DATABASE TodoCards;
USE TodoCards;

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `accessId` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `deckId` int(11) NOT NULL,
  `accessType` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `cardid` int(11) NOT NULL,
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

INSERT INTO `card` (`cardid`, `deckId`, `cardName`, `cardDescription`, `cardDue`, `cardIsFinished`, `cardColor`) VALUES
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
-- Table structure for table `share`
--

CREATE TABLE `share` (
  `code` varchar(20) NOT NULL,
  `deckId` int(11) NOT NULL,
  `type` varchar(4) NOT NULL,
  `expires` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`) VALUES
('bob', '4cbeba55bcfada7cf0142c53c101d9ac770abb26d02235b6f71a77d6d7f86bb10ac1e543dd8cbafcf8952c2d40528297'),
('cindy', '42e97aa817224cb8b2d50562f2fb2933bef91495f6166b1e7f33701765db0cac598fd8abd828b5a92ae56a8d17f5eb3b'),
('dean', '782b68900f3f74ac2d5eeccf5791ea19f0ff5f9d21309be379b24a6767836f1cafedcaa379ab923f8ce28dfe441b87f8'),
('fay', '1429511ebd6b934780d07ae90f6715c018f97ace7001302dac2488e8a74ce8f311f1212d3c3154943757be6e80897a09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`accessId`),
  ADD KEY `access_ibfk_1` (`deckId`),
  ADD KEY `access_ibfk_2` (`username`);

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`cardid`),
  ADD KEY `deckID` (`deckId`);

--
-- Indexes for table `deck`
--
ALTER TABLE `deck`
  ADD PRIMARY KEY (`deckid`);

--
-- Indexes for table `share`
--
ALTER TABLE `share`
  ADD PRIMARY KEY (`code`),
  ADD KEY `share_ibfk_1` (`deckId`);

--
-- Indexes for table `subcard`
--
ALTER TABLE `subcard`
  ADD PRIMARY KEY (`scardid`),
  ADD KEY `cardID` (`cardID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

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
-- Constraints for table `access`
--
ALTER TABLE `access`
  ADD CONSTRAINT `access_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `access_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `card`
--
ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `share`
--
ALTER TABLE `share`
  ADD CONSTRAINT `share_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subcard`
--
ALTER TABLE `subcard`
  ADD CONSTRAINT `subcard_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `card` (`cardid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
