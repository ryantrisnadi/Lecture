--cek data
-- select * from crunchbase_companies_clean_data limit 5;
-- select * from dc_bikeshare_q1_2012 limit 5;

--date formatting
-- update crunchbase_companies_clean_data
-- set founded_at = to_date(founded_at, 'MM/DD/YY');


-- alter table crunchbase_companies_clean_data
-- alter column founded_at type date using founded_at::date;



-- alter table crunchase_companies_clean_data
-- alter column founded_at type date using founded_at::date;

-- -deconstruct date
select 
	extract(month from founded_at) as bulan,
	extract(day from founded_at) as hari,
	extract(year from founded_at) as tahun
from
	crunchbase_companies_clean_data
limit 50;

-- handling missing values
select
	homepage_url,
	coalesce(homepage_url, 'no link')
from
	crunchbase_companies_clean_data;

-------

--LEFT/RIGHT mengamil data dari sisi kiri/kanan 
select
	permalink,
	left(permalink, 9) as contoh_left,
	right(permalink, 5) as contoh_right,
	substring(permalink, 10, 20) as contoh_substring
from
	crunchbase_companies_clean_data;

--substr, mengambil irisan sebuah teks
--trim(LEADING(front) / TRAILING(end) / BOTH(front and end))

select
	bike_number,
	trim(leading '0W' from bike_number) as contoh_lead,
	trim(trailing 'W0' from bike_number) as contoh_trailing,
	trim (both 'W0' from bike_number) as contoh_both
	
from 
	dc_bikeshare_q1_2012;

-- upper and lower
select
	end_station,
	upper(end_station),
	lower(end_station)
from 
	dc_bikeshare_q1_2012;

--position, mengembalikan nilai dari posisi sebuah karakhter
select 
	duration,
	position('M' in duration)
from
	dc_bikeshare_q1_2012;

--concat (untuk merge)
select
	start_station,
	end_station,
	concat(start_station, ' - ' ,end_station) as bike_route

from
	dc_bikeshare_q1_2012;

--case when / SQL Case (untuk categorize beberapa jenis data dengan nama/category)
select
	funding_total_usd,
	case
		when funding_total_usd > 1000000 then 'tinggi'
		when funding_total_usd > 50000 then 'sedang'
		else 'rendah' end as fund_category
from
	crunchbase_companies_clean_data;


--sub-query
select
	name,
	rata2_campus
from
		(select
			s.name,
			s.campus_id,
			avg(a.score) as rata2_campus
		from
			students s
		join assignment_scores a
			on s.id = a.students_id
		group by s.name, s.campus_id) as temptable
where
	rata2_campus > 85;

--subquery di where
select 
	*
from 
	students
where total_grade > (select
						avg(total_grade)
					 from students);




















	







