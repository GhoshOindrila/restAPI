CREATE DATABASE /*!32312 IF NOT EXISTS*/`restaurants` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `restaurants`;

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `MenuSection`;

CREATE TABLE `MenuSection` (
  `sectionID` int(11) NOT NULL AUTO_INCREMENT,
  `sectionName` varchar(50) NOT NULL,
  PRIMARY KEY (`sectionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `MenuSection` AUTO_INCREMENT=1000;

insert  into `MenuSection` (`sectionName`) values 

('Lunch Specials'),

('Dinner Specials'),

('Weekend Specials'),

('Soups');


DROP TABLE IF EXISTS `ItemSection`;

CREATE TABLE `ItemSection` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `sectionID` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`sectionID`) REFERENCES `menuSection` (`sectionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `ItemSection` AUTO_INCREMENT=100;

insert  into `ItemSection` (`title`, `price`, `sectionID`) values 

('Chicken over Rice', '13.50', '1000'),

('Lamb over Rice', '14.50', '1000' ),

('Anything over Rice', '15.50', '1000'),

('Chicken with Salad', '11.50', '1001'),

('Lamb with Salad', '12.80', '1001' ),

('Anything with Salad', '14.25', '1001');
