-- Create the students table
/*
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    campus_id INTEGER,
    total_grade FLOAT
);

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

-- Create the campus table
CREATE TABLE campus (
    id SERIAL PRIMARY KEY,
    campus_name VARCHAR(50),
    batch VARCHAR(10),
    start_date DATE
);

-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');

*/ 

--select
select * from campus;
select * from students;

-- DISTINC, untuk mengambil nilai unique
select
	id,
-- uniq data yang cuman 
	name
	
from
	students
where
	--start_date > '2023-02-01';
	name ILIKE '__k%';

--like sensitive case
--ilike is not sensitive case
--a% find a in beginning
--%a find a in end
--%a% find a in all 


--like, kolom name, age dan total grade 

-- aggregation
-- count(), berfungsi untuk menghitung baris
--AS itu alias atau title
--(*) for all columns and rows including empty ones. #useful for counting all data. 
select
	count(*) AS jumlah_siswa
from 
	students;

--sum(), menjumlah nilai
select
	sum(total_grade) AS kesuluruhan_nilai
from
	students;

--avg()
select
	avg(total_grade) as rata_rata
from students;

-- min(), max()
select
	min(total_grade) as nilai_terendah,
	max (total_grade) as nilai_tertinggi
from students;














	


