# MINI PROJECT : PROJECT ON EMPLOYEE DATABASE MANAGEMENT

import mysql.connector as mysql
from django.contrib.admin import display


## -----------------------------------connecting MySQL ----------------------------------------------##
def connect_mysql():
    mysqlobj = mysql.connect(
        host='localhost',
        user= 'root',
        password='',
        database=''

    )
    print('connected successfully')
    return mysqlobj

## -----------------------------------create database ----------------------------------------------##
def create_database(mysqlobj):
    cursor = mysqlobj.cursor()
    cursor.execute('create database IF NOT EXISTS software_industry')
    cursor.execute('show databases')
    records = cursor.fetchall()
    print('List of databases present = ')
    print('-' * 20)
    for i in records:
        print(i)
    print('-' * 20)
    cursor.close()

## -----------------------------------close mysql connection ----------------------------------------------##
def close_connection(mysqlobj):
    print('closing connection')
    mysqlobj.close()
    print('connection closed successfully')

## -----------------------------------create Table ----------------------------------------------##
def create_table(mysqlobj,database =' '):
    cursor = mysqlobj.cursor()
    cursor.execute("use "+database)
    print("using ", database)
    create_table1 = """
    CREATE TABLE IF NOT EXISTS Employee_DB(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    EMP_Name varchar(255),
    Designation varchar(255),
    Salary decimal(20,2),
    Location varchar(255))
    """
    cursor.execute(create_table1)
    cursor.close()

## -----------------------------------show list of tables present in databases --------------------------------------##
def list_table(mysqlobj,database =' '):
    cursor = mysqlobj.cursor()
    cursor.execute('use '+database)
    cursor.execute('show tables')
    records = cursor.fetchall()
    print('list of tables present in ',database)
    print('-' * 20)
    for r in records:
        print(r)
    print('-'*20)
    cursor.close()

## -----------------------------------insert records --------------------------------------##
def insert_record(con=' ',database=' ',table=' '):
    cursor = mysqlobj.cursor()
    cursor.execute('use ' + database)

    name = input('please enter name of employee: ')
    designation = input('please enter designation: ')
    salary = float(input('please enter salary: '))
    loc = input('please enter location: ')
    query = ('INSERT INTO employee_db(emp_name,designation,salary,location)'
             'values(%s,%s,%s,%s)')
    values = [(name,designation,salary,loc)]
    cursor.executemany(query,values)
    mysqlobj.commit()
    cursor.close()

## -----------------------------------update records--------------------------------------------##
def update_record(con = ' ',database=' ',table=' '):
    cursor = mysqlobj.cursor()
    cursor.execute('use '+database)
    print('1. name')
    print('2. designation')
    print('3. salary')
    print('4. location')
    ch = int(input('please enter the choice to update: '))
    if ch>= 1 and ch <=4:
        id = int(input('please enter the record id to update: '))
        boolean = Find_Id(id,con,database,table)
        if boolean != True:
            print('Invalid Id!!!')
            return None

        elif ch == 1:
            name = input('please enter correct name: ')
            query = 'update'+ table + 'set emp_name = %s where' + 'id = %s'
            values = (name,id)
            cursor.execute(query,values)
            mysqlobj.commit()
            print('record updated successfully')
            cursor.close()

        elif (ch ==2):
            designation = input('please enter correct designation: ')
            query = 'update ' + table +'SET designation = %s where' + 'id = %s'
            values = (designation,id)
            cursor.execute(query,values)
            mysqlobj.commit()
            print('record updated successfully')
            cursor.close()

        elif (ch == 3):
            salary = float(input('please enter correct salary: '))
            query = 'update ' + table +'SET salary = %s where'+ 'id = %s'
            values = (salary,id)
            cursor.execute(query, values)
            mysqlobj.commit()
            print('record updated successfully')
            cursor.close()

        elif (ch == 4):
            loc = (input('please enter correct location: '))
            query = 'update ' + table +'SET location = %s where'+ 'id = %s'
            values = (loc,id)
            cursor.execute(query, values)
            mysqlobj.commit()
            print('record updated successfully')
            cursor.close()
        display_rocords(mysqlobj,'software_industry','employee_db')

    else:
        print('Invalid choice: ')
        display_records(con,database,table)

## -----------------------------------Delete records--------------------------------------------##
def delete_record(con = ' ',database = ' ',table = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute('use ' + database)
    id = int(input('please enter id to delete the records: '))
    query = 'delete from' + table + 'where id = %s'
    values = (id,)
    boolean = Find_Id(id,con,database,table)
    if boolean == True:
        cursor.execute(query,values)
        mysqlobj.commit()
        print('record deleted successfully')
        cursor.close()

## -----------------------------------display records--------------------------------------------##
def display_records(con = ' ',database = ' ',table = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute('use ' + database)
    cursor.execute('select * from ' + table)
    records = cursor.fetchall()
    print('list of records present in' + table)
    print('-' * 20)
    print('ID\tName\tdesignation\tsalary\t location')
    for r in records:
        print(r[0],end='\t')
        print(r[1], end='\t')
        print(r[2], end='\t')
        print(r[3], end='\t')
        print(r[4])
    print('-' * 20)
    cursor.close()

## -----------------------------------Find Id--------------------------------------------##
def Find_Id(index,con = ' ',database = ' ',table = ' '):
    list_Id = []
    cursor = mysqlobj.cursor()
    cursor.execute('use ' + database)
    cursor.execute('select id from ' + table)
    records = cursor.fetchall()
    for r in records:
        list_Id.append(r[0])
    if index not in list_Id:
        print(index,'id is not present in table ',table)
    else:
        return True

## -----------------------------------start point of program--------------------------------------------##
if '__main__':
    try:
        mysqlobj = connect_mysql()
        create_database(mysqlobj)
        create_table(mysqlobj,'software_industry')
        list_table(mysqlobj,'software_industry')
        print('1. insert')
        print('2. update')
        print('3. delete')
        print('4. display records')
        print('5. exit')

        ch = int(input('please enter your choice: '))
        if ch == 1:
            try:
                insert_record(mysqlobj,'software_industry','employee_db')
                print('record inserted successfully')
            except Exception as e:
                print('Error: ',e)

        elif ch == 2:
            try:
                display_records(mysqlobj,'software_industry','employee_db')
                update_record(mysqlobj,'software_industry','employee_db')
            except Exception as e:
                print('Error: ',e)

        elif ch == 3:
            try:
                display_records(mysqlobj, 'software_industry', 'employee_db')
                delete_record(mysqlobj, 'software_industry', 'employee_db')
                print('-' * 20)
                display_records(mysqlobj, 'software_industry', 'employee_db')
            except Exception as e:
                print('Error: ',e)

        elif ch == 4:
            try:
                display_records(mysqlobj, 'software_industry', 'employee_db')
            except Exception as e:
                print('Error: ', e)

        elif ch == 5:
            try:
                close_connection(mysqlobj)
            except Exception as e:
                print('Error: ',e)

        else:
            print('invalid choice !!!')
            print('1. insert')
            print('2. update')
            print('3. delete')
            print('4. display records')
            print('5. exit')
            ch = int(input('please enter your choice: '))


    except Exception as e:
        print(e)
