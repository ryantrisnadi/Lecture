--create user
--create user user1;
--create user user2;

--akses/priviledge: select, insert, update, delete, usage, dsb...

--ngasih akses untuk user1
--akses untuk "lihat data" saja
--grant select on all tables in schema public to user1
--specific table
--grant select on students to user1;
	--dbb_campus_h8

--ngasih akses untuk user2
--akses untuk insert, update, delete saja
grant insert, update, delete on all tables in schema public to user2; 

--cabut akses
revoke update on all tables in schema public from user2; 

--cara ganti user
--set role user2;

--lihat user aktif
--select current_user;

--truncate table campuses cascade; 
--test select
--select * from students;


--test insert
--INSERT INTO campuses (id, name, batch, start_date)
--VALUES (1, 'Remote', 'RMT-1', '2023-01-01')

--test update
--update campuses
--set name = 'online'
--where id = 1;

--delete from campuses;
