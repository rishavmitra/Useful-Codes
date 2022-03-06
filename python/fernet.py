from cryptography.fernet import Fernet

# Key is used fir creating the cipher and the token is the encoded password
Key = b'jzi8A7-i7KivXd4-HE1SPdI42tIqVkk6rTwoZzGUCuY='
Token = b'gAAAAABhJmPwImI3OAnB9Ew8cTp5I2vo9We3ZRqK45cO3J1XCRH8HtPXt3Gslf5BaNf_PpNLRahV_gI-rFAumcBmi6DEKYa4Pw=='

# Creating a cipher for decrypt the password
cipher = Fernet(Key)

List = []  # Declaring a list to store the objects


class StudentInfo:

    "Initializing the variables Name, Regis_no"

    @staticmethod
    def register():
        " This function store the object in a list"
        '''
        obj = class object passed from main
    
        List.append() = Appending the new object to the class 
        '''
        obj.Name = input("Enter Name :")
        obj.Regis_no = int(input("Enter the registration Number :"))
        obj.Dept_no = input("Enter the deparment : ")
        obj.sem_no = input("Enter the semester no. :")
        obj.Payment = input("Payment (yes/no): ")
        if len(str(obj.Regis_no)) == 8 and (obj.Payment== 'yes' or obj.Payment== 'Yes'):
            List.append(obj)
        elif len(str(obj.Regis_no)) != 8:
            print("\n\t\tWarning : Registration number should be 8 digits")
        elif obj.Payment== 'no' or obj.Payment== 'No':
            print("\n\t\t Please make payment first")

    @staticmethod
    def del_regis():
        "This function is used to delete and object from the list"
        '''
        rgis = registration number to be deleted
    
        obj.Regis_no == rgis -> finding the registraton number
        '''
        rgis = int(input("Enter the Registration Number to be deleted: "))
        for obj in List:

            # Checking for the registration number to be deleted
            if obj.Regis_no == rgis:
                List.remove(obj)

    @staticmethod
    def view():
        flag = 0
        "This function is used to view the names of registered students"
        '''
        obj -> Used to iterate over the list of objects
        '''
        rgis = int(input("Enter the Registration Number to be viewed: "))
        for obj in List:
            if obj.Regis_no == rgis:
                flag = 1
        if flag == 1:
            print(" ")
            print("Name: ",obj.Name)
            print("Registraion no.:",obj.Regis_no)
            print("Department no.:",obj.Dept_no)
            print("Semester no.:",obj.sem_no)
            print(" ")
        else:
            print("\nNot Found !!")


#print(cipher.decrypt(Token))
while True:
    Password = input("Password: ")

    # Decrypting the password using the cipher created ago
    if Password == cipher.decrypt(Token).decode('utf-8'):
        while True:

            print("\n-----------------------------------------")
            print("Enter the option")
            print("1.Register a student")
            print("2.Delete the student")
            print("3.View the students")
            print("4.Exit")
            print("-----------------------------------------\n")

            ch = int(input())
            obj = StudentInfo()

            if ch == 1:
                # Calling the register function
                obj.register()
            elif ch == 2:
                # Calling the del_regis function
                obj.del_regis()
            elif ch == 3:
                # Calling the view function
                obj.view()
            elif ch == 4:
                # Ending the program
                exit()
    else:
        print("\t\tError : You are not the admin or enter the correct password \n")



