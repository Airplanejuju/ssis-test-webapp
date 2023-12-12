-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: dbssis
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblcollege`
--

DROP TABLE IF EXISTS `tblcollege`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblcollege` (
  `code` varchar(20) NOT NULL,
  `name` varchar(90) NOT NULL,
  PRIMARY KEY (`code`),
  UNIQUE KEY `code_UNIQUE` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcollege`
--

LOCK TABLES `tblcollege` WRITE;
/*!40000 ALTER TABLE `tblcollege` DISABLE KEYS */;
INSERT INTO `tblcollege` VALUES ('CASS','College of Arts and Social Sciences'),('CCS','College of Computer Studies'),('CEBA','College of Economics and Business Administration'),('CED','College of Education'),('CHS','College of Health Sciences'),('COE','College of Engineering'),('CSM','College of Science and Mathematics');
/*!40000 ALTER TABLE `tblcollege` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblcourse`
--

DROP TABLE IF EXISTS `tblcourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblcourse` (
  `code` varchar(20) NOT NULL,
  `name` varchar(90) NOT NULL,
  `college` varchar(20) NOT NULL,
  PRIMARY KEY (`code`),
  UNIQUE KEY `code_UNIQUE` (`code`),
  KEY `collegeForeign_idx` (`college`),
  CONSTRAINT `collegeForeign` FOREIGN KEY (`college`) REFERENCES `tblcollege` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcourse`
--

LOCK TABLES `tblcourse` WRITE;
/*!40000 ALTER TABLE `tblcourse` DISABLE KEYS */;
INSERT INTO `tblcourse` VALUES ('BAELS','Bachelor of Arts in English Language Studies','CASS'),('BAF','Bachelor of Arts in Filipino','CASS'),('BAH','Bachelor of Arts in History','CASS'),('BALCS','Bachelor of Arts in Literary and Culture Studies','CASS'),('BAP','Bachelor of Arts in Panitikan','CASS'),('BAPS','Bachelor of Arts in Political Science','CASS'),('BAPsy','Bachelor of Arts in Psychology','CASS'),('BSA','Bachelor of Science in Accountancy','CEBA'),('BSBA-BE','Bachelor of Science in Business Administration major in Business Economics','CEBA'),('BSBA-MM','Bachelor of Science in Business Administration major in Marketing Management','CEBA'),('BSBio','Bachelor of Science in Biology','CSM'),('BSCerE','Bachelor of Science in Ceramics Engineering','COE'),('BSChE','Bachelor of Science in Chemical Engineering','COE'),('BSChem','Bachelor of Science in Chemistry','CSM'),('BSCpE','Bachelor of Science in Computer Engineering','COE'),('BSCS','Bachelor of Science in Computer Science','CCS'),('BSE-Physics','Bachelor of Secondary Education – Physics','CED'),('BSECE','Bachelor of Science in Electronics and Communication Engineering','COE'),('BSEnvE','Bachelor of Science in Environmental Engineering','COE'),('BSIT','Bachelor of Science in Information Technology','CCS'),('BSMetE','Bachelor of Science in Metallurgical Engineering','COE'),('BSMiningE','Bachelor of Science in Mining Engineering','COE'),('BSN','Bachelor of Science in Nursing','CHS'),('BSPsy','Bachelor of Science in Psychology','CASS');
/*!40000 ALTER TABLE `tblcourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblstudent`
--

DROP TABLE IF EXISTS `tblstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblstudent` (
  `id` varchar(9) NOT NULL,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `course` varchar(20) NOT NULL,
  `year` int NOT NULL,
  `gender` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `courseForeign_idx` (`course`),
  CONSTRAINT `courseForeign` FOREIGN KEY (`course`) REFERENCES `tblcourse` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblstudent`
--

LOCK TABLES `tblstudent` WRITE;
/*!40000 ALTER TABLE `tblstudent` DISABLE KEYS */;
INSERT INTO `tblstudent` VALUES ('2020-0000','Klein','Moretti','BALCS',4,'M'),('2020-0001','Alger','Wilson','BSBio',4,'M'),('2020-0098','Jeiel','Dabodabo','BSChE',4,'M'),('2020-0117','Cesar James','Binolirao','BSChE',4,'M'),('2020-0120','Abby Jill','Daligdig','BSChE',4,'F'),('2020-0129','Reymond','Ado','BSChE',4,'M'),('2020-0228','Renefel','Llup','BSChE',4,'M'),('2020-0246','Nelvin','Amonsot','BSChE',4,'M'),('2020-0250','Cale','Henituse','BAPsy',4,'M'),('2020-0261','Cattleya','Micabalo','BSChE',4,'F'),('2020-0289','Shem','Laguda','BSChE',4,'M'),('2020-0297','Kyle David','Paalisbo','BSChE',4,'M'),('2020-0298','Audrey','Pabingwit','BSChE',4,'F'),('2020-0313','Brandon','Ballesteros','BSChE',4,'M'),('2020-0319','Jumaila','Dalandas','BSChE',4,'F'),('2020-0343','Carlo James','Solidor','BSChE',4,'Other'),('2020-1001','Welt','Joyce','BSChE',4,'M'),('2020-1011','Everett','Burns','BSA',4,'M'),('2020-1111','Liam','Zimmermann','BSEnvE',4,'M'),('2020-1134','Frazer','Avila','BSBA-MM',4,'Prefer not to say'),('2020-1236','Ramana','Grahame','BSBA-BE',4,'F'),('2020-1247','Jaelyn','Melton','BSCpE',4,'F'),('2020-1256','Pellehan','Nodira','BSE-Physics',4,'F'),('2020-2344','Christine','Rama','BSECE',4,'F'),('2020-2475','Joshua','Penales','BSCS',4,'M'),('2020-5180','Eden','Dorato','BSCS',4,'F'),('2020-7843','Lacey','Clements','BSN',4,'F'),('2021-0001','Fors','Wall','BAELS',3,'F'),('2021-0002','Audrey','Hall','BSPsy',3,'F'),('2021-0636','Gel','Sevilla','BSCS',3,'F'),('2021-1234','Fern','Sehi','BSChem',3,'F'),('2021-2123','Danielle Verna','Caasi','BSCS',3,'F'),('2021-2323','Bobby','Hobbs','BSMetE',3,'Other'),('2021-4234','Eyla','Wood','BSChem',3,'F'),('2021-4432','Emersson','Collier','BAF',3,'M'),('2021-4578','Lennon','Munoz','BAPS',3,'Other'),('2021-5666','Carson','Wong','BAH',3,'Prefer not to say'),('2022-0011','Kamari','Bernal','BAH',2,'F'),('2022-0013','Emlyn','White','BAPsy',2,'M'),('2022-0014','Logan','McGee','BSMetE',2,'Other'),('2022-1212','Jessie','Calderon','BSCpE',2,'M'),('2022-4319','Austin','Dallas','BAP',2,'M'),('2022-5472','Astrid','Townsent','BSCerE',2,'F'),('2023-0000','Derrick','Berg','BSMiningE',1,'M'),('2023-0010','Kora','Cervates','BAF',1,'F'),('2023-2312','Fitz','Feynapotter','BSN',1,'Other'),('2023-3213','Fisher','Galvan','BSBio',1,'M'),('2023-5632','Alexis','Hinton','BALCS',1,'F'),('2023-7856','Edison','Roman','BSIT',1,'Other'),('2023-8964','Kehlani','Pennington','BSA',1,'F');
/*!40000 ALTER TABLE `tblstudent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-10  9:31:10
