# test-repo-01
testing repo functions - easy mod
create or replace table t_radka_matouchova_project_SQL_primary_final as /*první úkol-mezivýpočet*/
select
	`name`,
	`payroll_year`,
	`payroll_quarter`,
	`value`,
	`value` - lag(`value`) OVER (PARTITION BY `name` order by `payroll_year`,`payroll_quarter`) as `vsechny_prirustky`
from czechia_payroll cp
join czechia_payroll_industry_branch cpib
	on cp.industry_branch_code = cpib.code;
