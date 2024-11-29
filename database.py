import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "medical_service"
)

mycursor = mycursor = mydb.cursor()

def run_sql_file(filename, connection):
    with open(filename) as f:
        for query in f.read().split(';'):
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
            except mysql.connector.Error as e:
                print(f"Error executing: {query}\n{e}")
                connection.rollback()

def insert_doctor_db(connection):
    for i in range(5):

        full_name  =  input("Enter Doctor name: \n")
        specialization = input ("Enter Doctor specialization: \n")
        phone_number = int(input("Enter Doctor Phone Number: \n"))
        email = input("Enter Doctor Email: \n")
        years_of_experience = int(input("Enter Doctor Experience Year: \n"))

        sql = "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)"
        val = (full_name, specialization, phone_number, email, years_of_experience)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        print("Inserted doctor data successfully!")

def insert_patient_db(connection):
    for i in range(3):

        full_name  =  input("Enter Patient name: \n")
        date_of_birth = int(input ("Enter Patient date_of_birth: \n"))
        gender = input("Enter Patient gender: \n")
        address = input("Enter Patient address: \n")
        phone_number = int(input("Enter Patient Phone Number: \n"))
        email = input("Enter Patient Email: \n")

        sql = "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)"
        val = (full_name, date_of_birth, gender, phone_number, email, address)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        print("Inserted patient data successfully!")

def insert_appointment_db(connection):
    for i in range(3):

        patient_id = int(input("Enter Patient Id: \n"))
        doctor_id = int(input("Enter Doctor Id: \n"))
        appointment_date = int(input("Enter Appointment date: \n"))
        reason = input("Enter Reason: \n")
        status = input("Enter status: \n")

        sql = "INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES (%s, %s, %s, %s, %s)"
        val = (patient_id, doctor_id, appointment_date, reason, status)
        cursor = connection.cursor()
        cursor.execute(sql, val)
        connection.commit()
        print("Inserted appoitment data successfully!")



print("Connect success")

insert_doctor_db(mydb)

insert_patient_db(mydb)
insert_appointment_db(mydb)

# run sql file:
 
# sql_file = "schema.sql"
# run_sql_file(sql_file, mydb)

mydb.close()