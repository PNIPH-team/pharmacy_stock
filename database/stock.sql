-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 13, 2023 at 09:15 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stock`
--

-- --------------------------------------------------------

--
-- Table structure for table `row_data_frequently`
--

CREATE TABLE `row_data_frequently` (
  `id` int(11) NOT NULL,
  `event_id` varchar(20) NOT NULL,
  `tei` varchar(20) NOT NULL,
  `program` varchar(20) NOT NULL,
  `stage` varchar(20) NOT NULL,
  `orgunit` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `m1` varchar(20) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `m2` varchar(20) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `m3` varchar(20) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `m4` varchar(20) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `m5` varchar(20) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  `m6` varchar(20) DEFAULT NULL,
  `q6` int(11) DEFAULT NULL,
  `m7` varchar(20) DEFAULT NULL,
  `q7` int(11) DEFAULT NULL,
  `m8` varchar(20) DEFAULT NULL,
  `q8` int(11) DEFAULT NULL,
  `m9` varchar(20) DEFAULT NULL,
  `q9` int(11) DEFAULT NULL,
  `m10` varchar(20) DEFAULT NULL,
  `q10` int(11) DEFAULT NULL,
  `m11` varchar(20) DEFAULT NULL,
  `q11` int(11) DEFAULT NULL,
  `m12` varchar(20) DEFAULT NULL,
  `q12` int(11) DEFAULT NULL,
  `m13` varchar(20) DEFAULT NULL,
  `q13` int(11) DEFAULT NULL,
  `m14` varchar(20) DEFAULT NULL,
  `q14` int(11) DEFAULT NULL,
  `m15` varchar(20) DEFAULT NULL,
  `q15` int(11) DEFAULT NULL,
  `m16` varchar(20) DEFAULT NULL,
  `q16` int(11) DEFAULT NULL,
  `m17` varchar(20) DEFAULT NULL,
  `q17` int(11) DEFAULT NULL,
  `m18` varchar(20) DEFAULT NULL,
  `q18` int(11) DEFAULT NULL,
  `m19` varchar(20) DEFAULT NULL,
  `q19` int(11) DEFAULT NULL,
  `m20` varchar(20) DEFAULT NULL,
  `q20` int(11) DEFAULT NULL,
  `m21` varchar(20) DEFAULT NULL,
  `q21` int(11) DEFAULT NULL,
  `m22` varchar(20) DEFAULT NULL,
  `q22` int(11) DEFAULT NULL,
  `m23` varchar(20) DEFAULT NULL,
  `q23` int(11) DEFAULT NULL,
  `m24` varchar(20) DEFAULT NULL,
  `q24` int(11) DEFAULT NULL,
  `m25` varchar(20) DEFAULT NULL,
  `q25` int(11) DEFAULT NULL,
  `m26` varchar(20) DEFAULT NULL,
  `q26` int(11) DEFAULT NULL,
  `m27` varchar(20) DEFAULT NULL,
  `q27` int(11) DEFAULT NULL,
  `m28` varchar(20) DEFAULT NULL,
  `q28` int(11) DEFAULT NULL,
  `m29` varchar(20) DEFAULT NULL,
  `q29` int(11) DEFAULT NULL,
  `m30` varchar(20) DEFAULT NULL,
  `q30` int(11) DEFAULT NULL,
  `m31` varchar(20) DEFAULT NULL,
  `q31` int(11) DEFAULT NULL,
  `m32` varchar(20) DEFAULT NULL,
  `q32` int(11) DEFAULT NULL,
  `m33` varchar(20) DEFAULT NULL,
  `q33` int(11) DEFAULT NULL,
  `m34` varchar(20) DEFAULT NULL,
  `q34` int(11) DEFAULT NULL,
  `m35` varchar(20) DEFAULT NULL,
  `q35` int(11) DEFAULT NULL,
  `m36` varchar(20) DEFAULT NULL,
  `q36` int(11) DEFAULT NULL,
  `m37` varchar(20) DEFAULT NULL,
  `q37` int(11) DEFAULT NULL,
  `m38` varchar(20) DEFAULT NULL,
  `q38` int(11) DEFAULT NULL,
  `m39` varchar(20) DEFAULT NULL,
  `q39` int(11) DEFAULT NULL,
  `m40` varchar(20) DEFAULT NULL,
  `q40` int(11) DEFAULT NULL,
  `m41` varchar(20) DEFAULT NULL,
  `q41` int(11) DEFAULT NULL,
  `m42` varchar(20) DEFAULT NULL,
  `q42` int(11) DEFAULT NULL,
  `m43` varchar(20) DEFAULT NULL,
  `q43` int(11) DEFAULT NULL,
  `m44` varchar(20) DEFAULT NULL,
  `q44` int(11) DEFAULT NULL,
  `last_update` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `row_data_prescribed`
--

CREATE TABLE `row_data_prescribed` (
  `id` int(11) NOT NULL,
  `event_id` varchar(20) NOT NULL,
  `tei` varchar(20) NOT NULL,
  `program` varchar(20) NOT NULL,
  `stage` varchar(20) NOT NULL,
  `orgunit` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `m1` varchar(20) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `m2` varchar(20) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `m3` varchar(20) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `m4` varchar(20) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `m5` varchar(20) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  `m6` varchar(20) DEFAULT NULL,
  `q6` int(11) DEFAULT NULL,
  `m7` varchar(20) DEFAULT NULL,
  `q7` int(11) DEFAULT NULL,
  `m8` varchar(20) DEFAULT NULL,
  `q8` int(11) DEFAULT NULL,
  `m9` varchar(20) DEFAULT NULL,
  `q9` int(11) DEFAULT NULL,
  `m10` varchar(20) DEFAULT NULL,
  `q10` int(11) DEFAULT NULL,
  `m11` varchar(20) DEFAULT NULL,
  `q11` int(11) DEFAULT NULL,
  `last_update` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `stock_data`
--

CREATE TABLE `stock_data` (
  `id` int(11) NOT NULL,
  `event_id` varchar(20) NOT NULL,
  `tei` varchar(20) NOT NULL,
  `program` varchar(20) NOT NULL,
  `stage` varchar(20) NOT NULL,
  `orgunit` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `dataElement` varchar(20) NOT NULL,
  `m` varchar(11) NOT NULL,
  `q` int(11) NOT NULL,
  `edit_date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `row_data_frequently`
--
ALTER TABLE `row_data_frequently`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `row_data_prescribed`
--
ALTER TABLE `row_data_prescribed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_data`
--
ALTER TABLE `stock_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `row_data_frequently`
--
ALTER TABLE `row_data_frequently`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `row_data_prescribed`
--
ALTER TABLE `row_data_prescribed`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stock_data`
--
ALTER TABLE `stock_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
