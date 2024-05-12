#Create a program to enter student records [Rno., Name, Age] in a binary file. Also write a function to search for a particular Rollno in the file.
import struct

# Function to enter student records into a binary file
def enter_student_records(file_name):
    with open(file_name, 'ab') as file:
        while True:
            roll_no = int(input("Enter Roll Number (0 to stop): "))
            if roll_no == 0:
                break
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            # Pack the data into a binary format
            data = struct.pack('i 20s i', roll_no, name.encode('utf-8'), age)
            file.write(data)

    print("Student records entered successfully.")

# Function to search for a specific Roll Number in the binary file
def search_student_record(file_name, roll_no):
    with open(file_name, 'rb') as file:
        while True:
            data = file.read(struct.calcsize('i 20s i'))
            if not data:
                break
            record = struct.unpack('i 20s i', data)
            if record[0] == roll_no:
                print("Record found - Roll No: {}, Name: {}, Age: {}".format(record[0], record[1].decode('utf-8').strip('\x00'), record[2]))
                # print("Record found - Roll No: {}, Name: {}, Age: {}".format(record[0], record[1], record[2]))
                return
        print("Record not found for Roll No:", roll_no)

# Main program
file_name = 'Prog15_tudent_records.bin'

# Enter student records into the binary file
enter_student_records(file_name)

# Search for a specific Roll Number in the binary file
roll_number_to_search = int(input("Enter Roll Number to search: "))
search_student_record(file_name, roll_number_to_search)
