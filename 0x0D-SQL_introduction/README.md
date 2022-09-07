# SQL - Introduction
## Resources
[What is Database & SQL?](https://alx-intranet.hbtn.io/rltoken/yyRKTEdRkYEVlRgZPbasjw)
[A Basic MySQL Tutorial](https://alx-intranet.hbtn.io/rltoken/sV2PtK5YfQsXWW1malRZ5Q)
[Basic SQL statements: DDL and DML](https://alx-intranet.hbtn.io/rltoken/IUKo4-UaRZSKPvXr5u9oBw)
[Basic queries: SQL and RA](https://alx-intranet.hbtn.io/rltoken/rXKvu2u7vg1Hj6bnX7UgMg)
[SQL technique: functions](https://alx-intranet.hbtn.io/rltoken/-Riv_dzSYsJyvy-LlaO6Mg)
[SQL technique: subqueries](https://alx-intranet.hbtn.io/rltoken/QpIXoR--8eBIaidgSWYsBQ)
[What makes the big difference between a backtick and an apostrophe?](https://alx-intranet.hbtn.io/rltoken/Gt0nFJPJRwW2Y0izzwbVrw)
[MySQL Cheat Sheet](https://alx-intranet.hbtn.io/rltoken/wLQZvDtRCG9eQ69c8jvYVA)
[MySQL 8.0 SQL Statement Syntax](https://alx-intranet.hbtn.io/rltoken/HmdmLiYBM0Q34iCYPWd9XQ)

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
### Use “container-on-demand” to run MySQL
In the container, credentials are root/root
- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database
information_schema
mysql
performance_schema                                   sys                      
$
```
In the container, credentials are ```root/root```

## Tasks
Files | Description
----- | -----------
[0-list_databases.sql](./0-list_databases.sql) | sql script that lists all databases of your MySQL server
[1-create_database_if_missing.sql](./1-create_database_if_missing.sql) | sql script that creates the database hbtn_0c_0 in your MySQL server
[2-remove_database.sql](./2-remove_database.sql) | sql script that deletes the database hbtn_0c_0 in your MySQL server
[3-list_tables.sql](./3-list_tables.sql) | sql script that lists all the tables of a database in your MySQL server
[4-first_table.sql](./4-first_table.sql) | sql script that creates a table called first_table in the current database in your MySQL server
[5-full_table.sql](./5-full_table.sql) | sql script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server
[6-list_values.sql](./6-list_values.sql) | sql script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
[7-insert_value.sql](./7-insert_value.sql) | sql script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server
[8-count_89.sql](./8-count_89.sql) | sql script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server
[9-full_creation.sql](./9-full_creation.sql) | sql script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
[10-top_score.sql](./10-top_score.sql) | sql script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
[11-best_score.sql](./11-best_score.sql) | sql script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server
[12-no_cheating.sql](./12-no_cheating.sql) | sql script that updates the score of Bob to 10 in the table second_table
[13-change_class.sql](./13-change_class.sql) | sql script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server
[14-average.sql](./14-average.sql) | sql script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server
[15-groups.sql](./15-groups.sql) | sql script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
[16-no_link.sql](./16-no_link.sql) | sql script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
[100-move_to_utf8.sql](./100-move_to_utf8.sql) | sql script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
[101-avg_temperatures.sql](./101-avg_temperatures.sql) | sql script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
[102-top_city.sql](./102-top_city.sql) | sql script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
[103-max_state.sql](./103-max_state.sql) | sql script that displays the max temperature of each state (ordered by State name)
Footer
