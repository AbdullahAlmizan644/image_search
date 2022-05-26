-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 26, 2022 at 11:11 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `image_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `sno` int(12) NOT NULL,
  `writer` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `post_id` int(12) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

CREATE TABLE `person` (
  `sno` int(12) NOT NULL,
  `name` varchar(200) NOT NULL,
  `address` varchar(10000) NOT NULL DEFAULT 'add person address',
  `image` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  `writer` varchar(200) NOT NULL DEFAULT 'writer'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`sno`, `name`, `address`, `image`, `date`, `writer`) VALUES
(3, 'Bill gates', '<h1>This person has been found</h1>\r\n', '1.jpg', '2022-05-15 00:03:57.398087', 'writer'),
(5, 'mark zukerbagh', 'i am mark ', 'mark.jpg', '2022-05-15 00:05:25.676223', 'writer'),
(6, 'elon mask', 'hi i am elon mask', 'mask.jpg', '2022-05-15 00:06:13.857859', 'writer'),
(7, 'Jeff Bezos', '<h1><strong>Jeff Bezos</strong></h1>\r\n\r\n<h3><em><strong>Jeffrey Preston Bezos</strong>&nbsp;(<a href=\"https://en.wikipedia.org/wiki/Help:IPA/English\">/ˈbeɪzoʊs/</a>&nbsp;<a href=\"https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key\">BAY-zohss</a>;<a href=\"https://en.wikipedia.org/wiki/Jeff_Bezos#cite_note-:0-1\">[1]</a>&nbsp;n&eacute;&nbsp;<strong>Jorgensen</strong>; born January 12, 1964) is an American entrepreneur,&nbsp;<a href=\"https://en.wikipedia.org/wiki/Media_proprietor\">media proprietor</a>, investor, computer engineer, and&nbsp;<a href=\"https://en.wikipedia.org/wiki/Commercial_astronaut\">commercial astronaut</a>.<a href=\"https://en.wikipedia.org/wiki/Jeff_Bezos#cite_note-2\">[2]</a><a href=\"https://en.wikipedia.org/wiki/Jeff_Bezos#cite_note-3\">[3]</a>&nbsp;He is the founder, executive chairman and former president and CEO of&nbsp;<a href=\"https://en.wikipedia.org/wiki/Amazon_(company)\">Amazon</a>. With a net worth of around US$140 billion as of May 2022, Bezos is the&nbsp;<a href=\"https://en.wikipedia.org/wiki/The_World%27s_Billionaires\">second-wealthiest person</a>&nbsp;in the world and was the wealthiest from 2017 to 2021 according to both&nbsp;<a href=\"https://en.wikipedia.org/wiki/Bloomberg_L.P.\">Bloomberg</a>&#39;s&nbsp;<a href=\"https://en.wikipedia.org/wiki/Bloomberg_Billionaires_Index\">Billionaires Index</a>&nbsp;and&nbsp;<a href=\"https://en.wikipedia.org/wiki/Forbes\">Forbes</a>.<a href=\"https://en.wikipedia.org/wiki/Jeff_Bezos#cite_note-4\">[4]</a><a href=\"https://en.wikipedia.org/wiki/Jeff_Bezos#cite_note-5\">[5]</a></em></h3>\r\n\r\n<h3><em>Born in&nbsp;<a href=\"https://en.wikipedia.org/wiki/Albuquerque,_New_Mexico\">Albuquerque</a>&nbsp;and raised in&nbsp;<a href=\"https://en.wikipedia.org/wiki/Houston\">Houston</a>&nbsp;and&nbsp;<a href=\"https://en.wikipedia.org/wiki/Miami\">Miami</a>, Bezos graduated from&nbsp;<a href=\"https://en.wikipedia.org/wiki/Princeton_University\">Princeton University</a>&nbsp;in 1986. He holds a degree in&nbsp;<a href=\"https://en.wikipedia.org/wiki/Electrical_engineering\">electrical engineering</a>&nbsp;and&nbsp;<a href=\"https://en.wikipedia.org/wiki/Computer_science\">computer science</a>. He worked on&nbsp;<a href=\"https://en.wikipedia.org/wiki/Wall_Street\">Wall Street</a>&nbsp;in a variety of related fields from 1986 to early 1994. Bezos founded Amazon in late 1994, on road trip from&nbsp;<a href=\"https://en.wikipedia.org/wiki/New_York_City\">New York City</a>&nbsp;to&nbsp;<a href=\"https://en.wikipedia.org/wiki/Seattle\">Seattle</a>. The company began as an online bookstore and has since expanded to a variety of other&nbsp;<a href=\"https://en.wikipedia.org/wiki/E-commerce\">e-commerce</a>&nbsp;products and services, including video and audio streaming,&nbsp;<a href=\"https://en.wikipedia.org/wiki/Cloud_computing\">cloud computing</a>, and&nbsp;<a href=\"https://en.wikipedia.org/wiki/Artificial_intelligence\">artificial intelligence</a>. It is currently the world&#39;s largest online sales company, the&nbsp;<a href=\"https://en.wikipedia.org/wiki/List_of_largest_Internet_companies\">largest Internet company by revenue</a>, and the largest provider of&nbsp;<a href=\"https://en.wikipedia.org/wiki/Virtual_assistant\">virtual assistants</a>&nbsp;and cloud infrastructure services through its&nbsp;<a href=\"https://en.wikipedia.org/wiki/Amazon_Web_Services\">Amazon Web Services</a>&nbsp;branch.</em></h3>\r\n\r\n<h3><em>Bezos founded the&nbsp;<a href=\"https://en.wikipedia.org/wiki/Aerospace_manufacturer\">aerospace manufacturer</a>&nbsp;and&nbsp;<a href=\"https://en.wikipedia.org/wiki/Sub-orbital_spaceflight\">sub-orbital spaceflight</a>&nbsp;services company&nbsp;<a href=\"https://en.wikipedia.org/wiki/Blue_Origin\">Blue Origin</a>&nbsp;in 2000. Blue Origin&#39;s&nbsp;<a href=\"https://en.wikipedia.org/wiki/New_Shepard\">New Shepard</a>&nbsp;vehicle&nbsp;<a href=\"https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n_line\">reached space</a>&nbsp;in 2015, and afterwards successfully landed back on Earth. He also purchased the major American newspaper&nbsp;<a href=\"https://en.wikipedia.org/wiki/The_Washington_Post\">The Washington Post</a>&nbsp;in 2013 for $250&nbsp;million, and manages many other investments through his&nbsp;<a href=\"https://en.wikipedia.org/wiki/Venture_capital\">venture capital</a>&nbsp;firm,&nbsp;<a href=\"https://en.wikipedia.org/wiki/Bezos_Expeditions\">Bezos Expeditions</a>. In September 2021, Bezos co-founded&nbsp;<a href=\"https://en.wikipedia.org/wiki/Biotechnology_company\">biotechnology company</a>&nbsp;<a href=\"https://en.wikipedia.org/wiki/Altos_Labs\">Altos Labs</a>&nbsp;with&nbsp;<a href=\"https://en.wikipedia.org/wiki/Mail.ru\">Mail.ru</a>&nbsp;founder&nbsp;<a href=\"https://en.wikipedia.org/wiki/Yuri_Milner\">Yuri Milner</a>.<a href=\"https://en.wikipedia.org/wiki/Jeff_Bezos#cite_note-Regalado2021-6\">[6]</a></em></h3>\r\n', 'jeff.jpg', '2022-05-15 16:34:57.596073', 'writer');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(12) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'user.png',
  `password` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `person`
--
ALTER TABLE `person`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
