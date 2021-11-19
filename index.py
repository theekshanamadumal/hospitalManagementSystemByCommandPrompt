import hashlib as hash


class HospitalSystem:
    # System Initialization
    def _init_(self):

        self.userConfigureData = []
        self.userConfigureFile = 'userConfiguration.csv'

        self.patientData = []
        self.dataFile = 'dataFile.csv'

        self.userName = ''
        self.privilages = []

        print("loading.....")
        print("                                   ____________________________________________________________________                               ")
        print("                                   ____________________________________________________________________                               \n")
        print("                                                         Hospital Management System                                               ")
        print("                                   ____________________________________________________________________                               ")
        print("                                   ____________________________________________________________________                               ")

        self.logIn()

    # login function
    def logIn(self):
        print("\n")
        print("\n|_________Enter User Credentials_________|\n")
        userName = input("Enter User Name : ")
        userPassword = input("Enter User Password : ")

        while not self.validateUser(userName, userPassword):
            userName = input("Enter User Name : ")
            userPassword = input("Enter User Password : ")
        else:
            self.selectFunctions()

    # usert login validation
    def validateUser(self, userName, userPassword):
        self.loadConfigureFile()

        hashedPassword = hash.md5(userPassword.encode("utf-8")).hexdigest()

        for line in self.userConfigureData:

            configUserName = line[0]
            configUserPassword = line[1]

            if configUserName == userName and configUserPassword == hashedPassword:
                self.userName = configUserName
                self.privilege = line[3]
                print("\n*****************************************\n|         Welcome  " +
                      line[2] + ' '+configUserName+"        |\n*****************************************")
                return True
            else:
                continue
        else:
            print("\n|_________Wrong User Credentials_________|\n")
            return False

    # load config file data
    def loadConfigureFile(self):
        with open(self.userConfigureFile, "r") as file:
            self.userConfigureData = []
            for line in file:
                self.userConfigureData.append(line.strip("\n").split(","))

    # write to config file
    def writeConfigureFile(self, userName, userPassword, role, privilageLevel):

        hashedPassword = hash.md5(userPassword.encode("utf-8")).hexdigest()

        with open(self.userConfigureFile, "a") as file:
            file.write(userName + "," + hashedPassword + "," +
                       role + "," + privilageLevel + "\n")

    # Load data file
    def loadDataFile(self):
        with open(self.dataFile, "r") as file:
            self.patientData = []
            for line in file:
                self.patientData.append(line.strip("\n").split(","))

    # write to data file
    def writeDataFile(self):
        with open(self.dataFile, "a") as file:
            for i in self.patientData:
                file.write(str(i[0])+","+str(i[1])+","+str(i[2])+"," +
                           str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+"\n")

    # select options

    def selectFunctions(self):

        self.loadDataFile()

        while True:
            print("\n")
            print(
                "|To view user details           Enter   1  |  To Add user                   Enter   6  |")
            print(
                "|To view patient  details       Enter   2  |  To Add patient details        Enter   7  |")
            print(
                "|To view sickness details       Enter   3  |  To Add sickness details       Enter   8  |")
            print(
                "|To view drug prescriptions     Enter   4  |  To Add drug prescriptions     Enter   9  |")
            print(
                "|To view lab test prescriptions Enter   5  |  To Add lab test prescriptions Enter   10 |")
            print("\n|To be Back Enter E ")

            choice = input("Enter your choice : ")
            print('\n')

            if choice == '1':
                for line in self.userConfigureData:
                    userName = line[0]
                    if userName == self.userName:
                        print("Name :", userName)
                        print("Hashed Password :", line[1])
                        print("User Type :", line[2])
                        print("Privilage Level :", line[3])

                    else:
                        continue

            elif choice == '2':
                if self.privilege in ['doctor', 'nurse', 'receptionist', 'labTechnician']:
                    patientId = input("Enter Patient ID: ")

                    for line in self.patientData:
                        if patientId == line[0]:
                            print("Patient Name :", line[1])
                            print("Patient Age :", line[2])
                            print("Patient Doctor :", line[6])
                            return True
                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False
                else:
                    print("Unautharized access!")
                    continue

            elif choice == '3':
                if self.privilege in ['doctor', 'nurse', 'labTechnician']:
                    patientId = input("Enter Patient ID: ")

                    for line in self.patientData:
                        if patientId == line[0]:
                            print("Patient Sick details :", line[3])
                            return True
                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False
                else:
                    print("Unautharized access!")
                    continue

            elif choice == '4':
                if self.privilege in ['doctor', 'nurse']:
                    patientId = input("Enter Patient ID: ")

                    for line in self.patientData:
                        if patientId == line[0]:
                            print("Patient Drug prescriptions :", line[4])
                            return True
                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False
                else:
                    print("Unautharized access!")
                    continue

            elif choice == '5':
                if self.privilege in ['doctor', 'labTechnician']:
                    patientId = input("Enter Patient ID: ")

                    for line in self.patientData:
                        if patientId == line[0]:
                            print("Patient lab Test description :", line[5])
                            return True
                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False
                else:
                    print("Unautharized access!")
                    continue

            elif choice == '6':
                if self.privilege == "admin":
                    userName = input("Enter username: ")
                    password = input("Enter password: ")
                    self.addUser(userName, password)
                else:
                    print("Unautharized access!")
                    continue

            elif choice == '7':
                if self.privilege in ["receptionist", "nurse"]:
                    userID = input("Enter patient ID: ")
                    userName = input("Enter patient Name: ")
                    userAge = input("Enter patient Age: ")

                    patient = [userID, userName, userAge, '', '', '', '']
                    self.patientData.append(patient)

                    print('success')
                else:
                    print("Unautharized access!")
                    continue

            elif choice == '8':
                if self.privilege == "doctor":
                    patientId = input("Enter patient ID: ")
                    for line in self.patientData:
                        if patientId == line[0]:
                            sick = input("Enter patient Sick data: ")
                            line[3] = sick
                            line[6] = self.userName

                            print('success')

                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False

                else:
                    print("Unautharized access!")
                    continue

            elif choice == '9':
                if self.privilege == "doctor":
                    patientId = input("Enter patient ID: ")
                    for line in self.patientData:
                        if patientId == line[0]:
                            drug = input("Enter patient drug prescriptions: ")
                            line[4] = drug
                            line[6] = self.userName
                            print('success')
                            return True
                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False

                else:
                    print("Unautharized access!")
                    continue

            elif choice == '10':
                if self.privilege == "labTechnician":
                    patientId = input("Enter patient ID: ")
                    for line in self.patientData:
                        if patientId == line[0]:
                            lab = input(
                                "Enter patient lab test prescriptions: ")
                            line[5] = lab
                            return True
                        else:
                            continue
                    else:
                        print("\n|_________Wrong Patient ID_________|\n")
                        return False

                else:
                    print("Unautharized access!")
                    continue

            elif choice == "E" or "e":  # Back
                self.writeDataFile()
                break

            else:
                print("--------------Wrong input! Enter a correct choice-------------")

    # ad a user to configure file

    def addUser(self, userName, password):
        hashedPassword = hash.md5(password.encode("utf-8")).hexdigest()

        userType = input("Enter user type(patient/staff):")
        if userType == "staff":
            privilege = input(
                "Enter privilage level [admin , doctor , nurse ,labTechnician, receptionist] : ")
        else:
            privilege = "patient"
        self.writeConfigureFile(userName, hashedPassword, userType, privilege)
        print("Successed!")


hospital = HospitalSystem()
hospital._init_()
