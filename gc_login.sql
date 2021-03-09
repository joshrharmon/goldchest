DROP TABLE IF EXISTS `gc_login`;

CREATE TABLE `gc_login` (
    `userID` int NOT NULL AUTO_INCREMENT,
    `username` varchar(30) NOT NULL,
    `password` varchar(255) NOT NULL,
    `salt1` varchar(255) NOT NULL,
    `salt2` varchar(255) NOT NULL,
    PRIMARY KEY (`userID`)
)
