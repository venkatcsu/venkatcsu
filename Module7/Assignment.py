

#run funtion()
def run():
    #create dictionary containing course numbers and the room numbers with key value pair
    #Course Number (key) : Room Number (value)
    Course_RoomNo_dict = { "CSC101":"3004", "CSC102" : "4501" , "CSC103" : "6755", "NET110" : "1244" , "COM241" : "1411" }
    #create dictionary containing course numbers and the names of the instructors for each course
    #Course Number (key) : Instructor (value)
    Course_Instructors_dict = { "CSC101":"Haynes", "CSC102" : "Alvarado" , "CSC103" : "Rich", "NET110" : "Burke" , "COM241" : "Lee"}
    #create dictionary containing course numbers and the meeting times of each course
    #Course Number (key) : Meeting Time (value)
    Course_Meeting_Time_dict = {"CSC101": "8:00 a.m.", "CSC102" : "9:00 a.m." , "CSC103" : "10:00 a.m.", "NET110" : "11:00 a.m." , "COM241" : "1:00 p.m."}
    #Get course number from the user to get the course's room number, instructor, and meeting time.
    while True:
        Course_Number = (input("Enter your course number: ")).upper()
        if Course_Number in Course_RoomNo_dict:
            #print Course's Room Number, instructor and meeting time
            print(f"Course {Course_Number}'s  Room Number is: ", Course_RoomNo_dict[Course_Number], ".Instructor is:",
                  Course_Instructors_dict[Course_Number]," and meeting time is: ",Course_Meeting_Time_dict[Course_Number])
            return Course_Number
        else:
            print("Invalid input. Please enter a valid course.")     
run()
