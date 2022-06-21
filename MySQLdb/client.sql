-- phpMyAdmin SQL Dump
-- version 4.1.4
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Dim 22 Avril 2018 à 23:20
-- Version du serveur :  5.6.15-log
-- Version de PHP :  5.5.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `client`
--

-- --------------------------------------------------------

--
-- Structure de la table `liste`
--

CREATE TABLE IF NOT EXISTS `liste` (
  `CIN` int(8) NOT NULL,
  `nom` varchar(60) NOT NULL,
  `prenom` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `photo` varchar(60) NOT NULL,
  `motPasse` varchar(60) NOT NULL,
  PRIMARY KEY (`CIN`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contenu de la table `liste`
--

INSERT INTO `liste` (`CIN`, `nom`, `prenom`, `email`, `photo`, `motPasse`) VALUES
(11095111, 'maalej', 'rahma', 'rahmamaalej1234@gmail.com', '', '11095111'),
(11073578, 'gharbi', 'mariem', 'rahmamaalej1234@gmail.com', 'escs.png', '11073578'),
(11095455, 'maalej', 'ali', 'rahmamaalej1234@gmail.com', '1t.jpg', '11095455'),
(14567896, 'maalej', 'ahlem', 'maalejahlem@yahoo.fr', 'escs.png', '14567896');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
