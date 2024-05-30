
--contoh:
begin;

drop table if exists campuses, students;

create table if not exists campuses (
	id integer primary key,
	name varchar not null,
	batch varchar not null,
	start_date date
	
);

create table if not exists students (
	id serial primary key,
	name varchar not null,
	age integer not null,
	campus_id integer not null,
	total_grade decimal not null,

	--define foreign key
	foreign key (campus_id) references campuses(id) 
	
);

savepoint "savepoint1";
	
-- Insert data into the campuses table
INSERT INTO campuses (id, name, batch, start_date)
VALUES
    (1, 'Remote', 'RMT-1', '2023-01-01'),
    (2, 'Jakarta', 'HCK-2', '2023-02-01'),
    (3, 'BSD', 'BSD-4', '2023-03-01'),
    (4, 'Surabaya', 'SUB-1', '2023-04-01'),
    (5, 'Singapore', 'SIN-1', '2023-05-01');

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

--rollback to savepoint "savepoint1";

commit;
--atau 
--rollback

select * from students;
