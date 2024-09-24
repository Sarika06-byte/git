create database user;
create database admin;
show databases ;
drop database user;
drop database admin;
show databases ;

create database abc_tech;
use abc_tech ;
show databases ;
create table shipping_data(product_id varchar(20),sales_man_id varchar(10),commission float,delivery_person_name varchar(11),shipping_date date ,amount_received double,mode_of_payment varchar(20),delivery_address varchar(20));
create table product_data(product_id int,sales_man_id varchar(10),selling_date  date,production_head varchar(20),product_type varchar(20),product_cost double,sales_person varchar(20),city varchar(20),ach_per int,unach_per int);
create table customer_data(product_id varchar(20),customer_name varchar(10), customer_id int,buying_date date,product_type varchar(20),product_cost double,customer_address varchar(20),grade int,sales_man_id varchar(10));
create table sales_data(name varchar(20),id int,city varchar(20),commision float);
insert into shipping_data values (1,11,0.04,'ram','2024-01-01',2000.2,'cash','mohali'),(2,22,0.56,'sam','2024-02-01',345.34,'upi','verka'),(4,44,1.23,'dev','2024-04-14',100.89,'cash','asr');
insert into product_data values(1000,11,'2024-01-01','manager','clothes',5000.2,'paul_adam','london',89,11),(5700,22,'2024-02-01','manager','top',345.34,'ramesh','london',60,40),(7899,33,'2024-04-14','manager','hair_pins',100.89,'suresh','asr',75,25),(4,44,'2024-01-01','manager','cooler',10000.2,'mahesh','asr',49,51);
insert into customer_data values(1,'riya',3007,'2024-01-01','clothes',2000.2,'new_york',110,11),(2,'divya',201,'2024-02-01','top',345.34,'verka',50,22),(3,'jiya',22,'2024-04-14','hair_pins',100.89,'asr',129,33);
insert into sales_data values('hetal',567,'luchnow',0.50),('vishal',564,'delhi',0.67),('raghav',568,'paris',0.11),('karan',569,'hamirpur',0.12);

select * from shipping_data;
select * from product_data;
select * from customer_data;
-- drop table product_data;
-- truncate table sales_data;

-- SUBQUERY :

-- 1..RETURN product_no, rd_date, purch_amount, salesman_name where sales_person="paul_adam":
select product_id as product_no, selling_date as ord_date,product_cost as purch_amount,sales_person as salesman_name from product_data
 where sales_person= (select sales_person from product_data where sales_person="paul_adam");
-- 2..RETURN product_no, rd_date, purch_amount, salesman_name where sales_person_address="london":
select product_id as product_no, selling_date as ord_date,product_cost as purch_amount,sales_person as salesman_name from product_data
 where city= (select city from product_data where city="london");
-- 3..RETURN product_no, rd_date, purch_amount, salesman_name where customer_id=3007:
select product_id as product_no, buying_date as ord_date,product_cost as purch_amount,sales_man_id,customer_id from customer_data
 where customer_id= (select customer_id from customer_data where customer_id=3007);
-- 4..RETURN product_no, order_date, purch_amount, salesman_name where order>avg(order) on '2024-04-14' :
select product_id as product_no, buying_date as ord_date,product_cost as purch_amount,sales_man_id,customer_id from customer_data
 where product_cost  = (select avg(product_cost)  from customer_data where buying_date ='2024-04-14');
-- 5..RETURN commission where sales_man_city='paris' :
select name, commision,city from sales_data
 where commision  = (select commision  from sales_data where city='paris' );
-- 6..RETURN grade,no of custoemrs where no of custoemr>gradein new york' :
select grade,count(customer_id) from customer_data 
 where   count(customer_id) >  (select grade  from customer_data where customer_address ="new_york" group by grade,custoemr_id) ;




-- 1..to display customer name,id,city,sales_man_id,grade where grade>100 :
select customer_name , customer_id,customer_address as city,sales_man_id,grade from customer_data where grade>100;

-- 2..find custoemr in new york  and having grade >100 amd display customer name,id,city,grade,sales_man_id :
select customer_name , customer_id,customer_address as city,sales_man_id,grade from customer_data where grade>100 and customer_address="new_york";

-- 3..find custoemr in new york  or having grade >100 amd display customer name,id,city,grade,sales_man_id :
select customer_name , customer_id,customer_address as city,sales_man_id,grade from customer_data where grade>100 or customer_address="new_york";

-- 4..find custoemr in new york  or having grade <100 amd display customer name,id,city,grade,sales_man_id :
select customer_name , customer_id,customer_address as city,sales_man_id,grade from customer_data where grade<100 or customer_address="new_york";

-- 5.. find custoemr who not belongs to new york  or  having grade >100 amd display customer name,id,city,grade,sales_man_id :
select customer_name , customer_id,customer_address as city,sales_man_id,grade from customer_data where grade>100 and customer_address!="new_york";

-- 6..find order details of orders where product_id>5005 and selling_date='2024-02-01' or product_cost>200 :
select   product_id,selling_date as purcahing_date,sales_man_id,product_cost as puchasing_amount from product_data 
where product_id>5005 and selling_date='2024-02-01' or product_cost>200;

-- 7.. display sales man data where commission ranges between 0.10 to 0.12 :
select name,id,city,commision from sales_data where commision between 0.10 and 0.12;

-- 8..find order details of orders where buying_date>='2024-02-01' or product_cost<200 and customer_id <3009; :
select   customer_id,buying_date as purcahing_date,sales_man_id,product_cost as puchasing_amount from customer_data 
where  buying_date>='2024-02-01' or product_cost<200 and customer_id <3009;

-- 9..find order details of orders where product_id>5005 and selling_date='2024-02-01' or product_cost>200 :
select   customer_id,buying_date as purcahing_date,sales_man_id,product_cost as puchasing_amount from customer_data 
where  buying_date='2024-02-01' or product_cost<1000 and customer_id >3005;
 
 -- 10..display order where profit > 50 % of targert of 6000;
select   product_id,selling_date as purcahing_date,product_cost as puchasing_amount,ach_per as achieved_precentage,unach_per as unachieved_precentage from product_data 
where product_cost>3000 and ach_per>50;

-- 11.. display emp datails who work at dept 47 or 63 :
select * from employee_personal_data;
select id,name,address,dept_no from employee_personal_data where dept_no=47 or dept_no= 63;











-- 1...total puchase of all product: 
select sum(product_cost) as total_puchase_of_products from  product_data  ; 
-- 2... average purchase amount:
select avg(product_cost) as average_puchase_of_products from  product_data  ; 
-- 3... count no of unique sales person :
select sales_person,count(*) as count_sales__person from  product_data group by sales_person ; 
-- 6...count no of customers:
select customer_name,count(*) as count_no_of_customer from  customer_data group by customer_name ;
-- 5... maximum purcahse amount :
select max(product_cost) as maximum_purchase_amount  from customer_data;
select product_cost as maximum_purchase_amount  from  customer_data group by product_cost having max(product_cost);
-- 7.. minimum purcahse amount :
select min(product_cost) as maximum_purchase_amount  from customer_data;
-- 8...find highest grade of customer ijn each city :
select customer_address as city,grade as highest_grade  from  customer_data group by customer_address,grade;
-- 9..highest puchase amount made by each sales man on 2024-01-01 :
select sales_person ,(product_cost)  as no_of_purchases_on_2024_01_01 from  product_data where selling_date='2024-01-01' group by sales_person,product_cost having max(product_cost);
-- 10...return nsales man id and puchase amount: 
select sales_man_id ,product_cost  as purchases_amount from  product_data   ;
-- 11...count all order generated on 20204-01-01 :
select count(product_no)  as no_of_purchases_on_2024_01_01 from  product_data where selling_date='2024-01-01';
-- 12...no of salesperson i na city :
select city,count(sales_person)  as sales_person_in_each_city from  product_data   group by city;


select *   from product_data;







select * from customer_data cd inner join product_data pd on cd.product_id=pd.product_id inner join shipping_data sd on  cd.product_id=sd.product_id ;
select * from customer_data cd left join product_data pd on  cd.product_id=pd.product_id left join shipping_data sd on  cd.product_id =sd.product_id ;
select * from customer_data cd right join product_data pd on  cd.product_id=pd.product_id right join shipping_data sd on  cd.product_id =sd.product_id;
select * from customer_data  cd  join customer_data  sd;
select * from customer_data cd left join product_data pd on  cd.product_id=pd.product_id left join shipping_data sd on  cd.product=sd.product_id union
select * from customer_data cd right join product_data pd on  cd.product_id=pd.product_id right join shipping_data sd  on  cd.product_id=sd.product_id ;
alter  table student_details drop primary key;
desc  student_admission_form;
alter table emp_details drop foreign key std_id ;
drop table emp_details;
create table data(id int primary key,age int check(age>=18));
desc data;
alter table data drop primary key;