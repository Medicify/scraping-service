-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 08 Bulan Mei 2023 pada 10.52
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drug_capstone`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `drugs`
--

CREATE TABLE `drugs` (
  `id` varchar(32) DEFAULT(UUID()) PRIMARY KEY,
  `image` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `product_url` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `indication` text DEFAULT NULL,
  `compotition` varchar(255) DEFAULT NULL,
  `dose` text DEFAULT NULL,
  `how_to_use` varchar(255) DEFAULT NULL,
  `attention` text DEFAULT NULL,
  `indication_contra` text DEFAULT NULL,
  `side_effect` text DEFAULT NULL,
  `product_class` varchar(255) DEFAULT NULL,
  `package` varchar(255) DEFAULT NULL,
  `manufactur` varchar(25) DEFAULT NULL,
  `bpom` varchar(255) DEFAULT NULL,
  UNIQUE KEY (product_url)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
