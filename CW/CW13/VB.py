import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='vb', user='postgres',
        password='1234')

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)
    HospitalName = 'emam'
    cur.execute('INSERT INTO hospital(hospital_id, hospital_name) VALUES (%s, %s)', (1, 'emam',))
    con.commit()
    cur.execute('SELECT * FROM hospital')
    data = cur.fetchall()
    print(data)


    cur.execute('INSERT INTO room(room_name, hospital_id) VALUES (%s, %s)', ('children', 1))
    con.commit()

    cur.execute('INSERT INTO bed(bed_name, room_id) VALUES (%s, %s)', ('peaman', 1))
    con.commit()

    cur.execute('INSERT INTO doctor(doctor_name) VALUES (%s)', ('davodi',))
    con.commit()

    cur.execute('INSERT INTO hd(doctor_id, hospital_id) VALUES (%s, %s)', (1, 1))
    con.commit()

    cur.execute('INSERT INTO patient(patient_name, bed_id, cost, exit_date, start_date) VALUES (%s, %s, %s, %s, %s)', ('sarina', 1, 50, 22, 21))
    con.commit()

    cur.execute('INSERT INTO visit(date_time, comment, doctor_id, ptient_id) VALUES (%s, %s, %s, %s)', (12, 'doctor is comming', 1, 1))
    con.commit()

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()

