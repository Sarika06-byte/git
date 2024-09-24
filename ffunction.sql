use abc_tech;
create table employee_personal_data(id varchar(10),name varchar(10),address varchar(10),mob varchar(10),age int,dob date,job varchar(20));
create table emp(job_avail varchar(20),dept varchar (20),salary double);
create table dept(emp_name1 varchar(10),desig_sales varchar(10),date_of_joining_sales date,emp_name2 varchar(10),desig_program varchar(10),date_of_joining_exe date);
create table account_details(sales_emp_id varchar(10),desig_sales varchar(10),sales_acc_no varchar(10),sales_salary double,program_emp_id varchar(20),desig_program varchar(10),program_acc_no float,program_salary double);
create table math(value int,exp int);
insert into employee values(11,'  suhana  ','asr',898990,21,'2003-01-01'),(12,'  enakshi  ','asr',565678,22,'2002-11-16'),(13,'  diya  ','majitha',454523,20,'2004-08-23');
insert into dept values('suhana','manager','2024-08-23','diksha','manager','2024-01-04'),('enakshi','hod','2020-12-03','dev','programmer','2024-03-04'),('diya','assistant','2024-01-24','hena','programmer','2024-11-24'),('riya','analyst','2024-01-24','nia','coder','2024-11-24');
insert into account_details values(11,'manager',234567,70000.32,21,'manager',232323,80000.56),(12,'hod',676789,90000.09,22,'programer',656789,70000.56),(13,'clerk',567567,25000.59,23,'programer',789098,2000.35),(14,'analyst',906789,50000.09,24,'coder',654449,30000.56);
insert into math values(20,2),(45,4),(78,3),(34,2);
insert into emp values('manager','sales',80000.34),('clerk','sales',10000.34),('hod','sales',40000.34);


-- SELECT STATMENT : 
select * from emp;
select * from employee_personal_data;
select * from dept;
select * from account_details;

-- list no of jobs available :
select job_avail from emp;

-- total salary pay t oemployees : 
select sum(sales_salary)+sum(program_salary) from account_details;          -- FOR SALARY

-- minimum, maximum, average salary from both sales and programming department : 
select min(sales_salary)+min(program_salary),max(sales_salary)+max(program_salary),avg(sales_salary)+avg(program_salary) from account_details;          -- FOR MIN , MAX ,AVG SALARY
 
 -- maximum salrary of employee working as programmer : 
 select max(program_salary) from account_details where desig_program='programmer' ;    -- MAX SALARY OF PROGRAMMER
 
 -- average salary of employee and no of  employees working in both dept :
 select avg(sales_salary)+avg(program_salary),count(sales_emp_id)+count(program_emp_id) from account_details;          -- FOR SALARY AND COUNTING EMPLOYEES

-- highest ,lowest ,average salary of all employees: 
select min(sales_salary),max(sales_salary),avg(sales_salary),min(program_salary),max(sales_salary),avg(program_salary) from account_details;          

-- both have same job in different dept: 
 select emp_name1,emp_name2 from dept where desig_sales=desig_program;    -- in sales & programming dept

-- both have same job in same dept: 
 select emp_name1 from dept where desig_sales;       -- in sales dept
  select emp_name2 from dept where desig_program;    -- in programming dept
  
  -- difference between highest and lowest salary : 
  select max(sales_salary)-min(sales_salary) from account_details    ;      -- FROM SALES DEPT 
 select  max(program_salary)-min(program_salary) from account_details;      -- FROM PROGRAM DEPT    
 
 -- dispaly manager id and salry of lowest paid employee fro that manager:
 select sales_emp_id from account_details where desig_sales='manager';
  select program_emp_id from account_details where desig_program='manager';

-- display dept_id and total salary paid in each dept:
 select sum(sales_salary),sum(program_salary) from account_details ;

-- to display avg salary of all employee excluding programmer;
 select avg(program_salary) from account_details where desig_sales!='programmer';

 










-- AGGREGATE FUNTIONS IN SQL :
-- LENGTH FUNTION :
select name,length(name) from employee;
-- MIN,MAX,AVG FUNTION : 
select min(age),max(age),avg(age) from employee;                          -- FOR AGE
select min(salary),max(salary),avg(salary) from account_details;          -- FOR SALARY
-- SUM FUNTION :
select sum(salary) from account_details;          -- FOR SALARY
select sum(gst) from account_details;          -- FOR GST
select sum(bonus) from account_details;          -- FOR BONUS
-- COUNT FUNTION : 
select count(emp_id) from account_details;  

-- STRING  FUNTIONS : 
-- CONCATENATION :
select name,concat(name,"_kaur") from employee; 
-- LOWER, UPPER, MID/SUBSRRING :
select name,lower(name),ucase(name),substring(name,3) from employee;          
-- TRIM, LTRIM, RTRIM :
select name,trim(name),ltrim(name),rtrim(name) from employee; 
-- LEFT ,RIGHT :
select name,left(name,4),right(name,4),mid(name,5) from  employee;         

-- DATE/MONTH function : 
-- DATE, DAY, MONTH, YEAR FUNTION :
select id,name,date(dob),day(dob),month(dob),year(dob) from employee; 
-- DAYNAME,MONTHNAME FUNTION :
select name,dayname(dob),monthname(dob) from employee; 

-- MATH FUNTION :
-- ROUND :
select emp_id,round(salary) from account_details ; 
-- POWER :
select power(value,exp) from math ; 
-- MOD :
select mod(value,exp) from  math; 
	

        

