-- MySQL dump 10.13  Distrib 5.7.20, for osx10.13 (x86_64)
--
-- Host: localhost    Database: openfood
-- ------------------------------------------------------
-- Server version 5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `User_search`
--

DROP TABLE IF EXISTS `User_search`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_search` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `id_to_substitue` bigint(30) unsigned NOT NULL,
  `id_substitued` bigint(30) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_id_to_substitue` (`id_to_substitue`),
  KEY `fk_id_substitued` (`id_substitued`),
  CONSTRAINT `fk_id_substitued` FOREIGN KEY (`id_substitued`) REFERENCES `food` (`id_openfood`),
  CONSTRAINT `fk_id_to_substitue` FOREIGN KEY (`id_to_substitue`) REFERENCES `food` (`id_openfood`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_search`
--

LOCK TABLES `User_search` WRITE;
/*!40000 ALTER TABLE `User_search` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_search` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorie` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `cat` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie`
--

LOCK TABLES `categorie` WRITE;
/*!40000 ALTER TABLE `categorie` DISABLE KEYS */;
INSERT INTO `categorie` VALUES (1,'jus_de_fruits'),(2,'charcuteries'),(3,'snacks_sucrés'),(4,'soupes'),(5,'fromages'),(6,'plats_prepares');
/*!40000 ALTER TABLE `categorie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food` (
  `id_openfood` bigint(30) unsigned NOT NULL,
  `food_name` text NOT NULL,
  `category_id` smallint(5) unsigned NOT NULL,
  `nutrition_grade` char(1) NOT NULL,
  `food_link` text NOT NULL,
  `store` text,
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ind_idopen_name` (`id_openfood`),
  KEY `fk_food_categoie_id` (`category_id`),
  CONSTRAINT `fk_food_categoie_id` FOREIGN KEY (`category_id`) REFERENCES `categorie` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131429 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`