--create database petshop
create table cat (
	id int not null identity primary key,
	name varchar(255),
	age int,
	favoriteFood varchar(255)
)

create table dog (
	id int not null identity primary key,
	name varchar(255),
	age int,
	favoriteFood varchar(255)
)

insert into dbo.cat (name)
VALUES ('Snuffaluffagus')

insert into dbo.cat (name, age, favoriteFood)
VALUES ('Snuffaluffagus2', 709, 'spinach'),
	   ('Snuffaluffagus2', 709, 'spinach'),
       (NULL, NULL, NULL);

insert into dbo.cat
DEFAULT VALUES;