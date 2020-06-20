import csv

with open ('student_name.csv','r') as students:
    csv_students = csv.reader(students)
    next(csv_students)
    students = [ ]
    for line in csv_students:
    	students.append(line)
    
    with open ('attendance.csv','r') as attendance:
        csv_attendance = csv.reader(attendance) 
        next(csv_attendance)
        attendance = [ ]
        for line2 in csv_attendance:
        	attendance.append(line2)
        
        with open ('attendance2.csv','w') as attendance1:
            csv_writer = csv.writer(attendance1)
            
            for line in students:
                if line in attendance:
                    line.append('PRESENT')
                else:
                    line.append('ABSENT')
                csv_writer.writerow(line )