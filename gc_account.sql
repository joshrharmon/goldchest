DROP TABLE IF EXISTS `gc_account`;

CREATE TABLE `gc_account`(
    `userEmail` varchar(255) NOT NULL,
    `userName`  varchar(30) NOT NULL,
    `watchlist` varchar(255) NOT NULL,
    `genres`    varchar(255) NOT NULL,
    `pastPurchases` varchar(255) NOT NULL,
    PRIMARY KEY (`userName`)
)
