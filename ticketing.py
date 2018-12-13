from datetime import datetime
global date
date = datetime.now().strftime("%d/%m/%y")

#----------------------MAIN MENU---------------------------

def main_menu():
    print("*"*30)
    print("*   FERRY TICKETING SYSTEM   *")
    print("*         MAIN MENU          *")
    print("*"*30)
    print(" P - Purchase Ticket ")
    print(" V - View Seating Arrangement ")
    print(" Q - Quit the system\n\n")
    customer = str(input("Enter Here:- ").upper())
    if customer == "P":
        sub_menu()
    elif customer == "V":
        arrangement()
    elif customer == "Q":
        quit()
    else:
        print("-----ERROR-----")
        return sub_menu()

#----------------------SUB MENU---------------------------
def sub_menu():
    destination()
    ch1 = int(input("Choose Destination:- "))
    if ch1 == 1:
        print("-"*30)
        print("B – to purchase ticket for Business class")
        print("E – to purchase ticket for Economy class")
        print("M – to return to Main Menu")
        ch2 = str(input("Enter Here:- ").upper())
        if ch2 == "B":
            business2lang()
        elif ch2 == "E":
            economy2lang()
        elif ch2 == "M":
            main_menu()
        else:
            print("-----ERROR-----")
            return sub_menu()
    elif ch1 == 2:
        print("-"*30)
        print("B – to purchase ticket for Business class")
        print("E – to purchase ticket for Economy class")
        print("M – to return to Main Menu")
        ch2 = str(input("Enter Here:- ").upper())
        if ch2 == "B":
            business2penang()
        elif ch2 == "E":
            economy2penang()
        elif ch2 == "M":
            main_menu()
        else:
            print("-----ERROR-----")
            return sub_menu()
    else:
        print("-----ERROR-----")
        return sub_menu()


#----------------------BUSINESS CLASS 2 LANGKAWI---------------------------
def business2lang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*30)
    des_time2lang()
    chse = int(input("Choose:- "))
    if chse == 1:
        print("-"*30)
        ferryID_101_b()
        if 0 in ferry_101_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_101_b[9] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "101 | TIME: 10:00AM"
                user()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        elif 0 not in ferry_101_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- "))
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        else:
            print("-----ERROR-----")
            return business2lang()
    elif chse == 2:
        print("-"*30)
        ferryID_102_b()
        if 0 in ferry_102_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_102_b[7] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Business"
                trip_seat = "B08"
                trip_ferry = "102 | TIME: 01:00PM"
                user()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        elif 0 not in ferry_102_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        else:
            print("-----ERROR-----")
            return business2lang()
    elif chse == 3:
        print("-"*30)
        ferryID_103_b()
        if 0 in ferry_103_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_103_b[9] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Business"
                trip_seat = "B10"
                trip_ferry = "103 | TIME: 04:00PM"
                user()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        elif 0 not in ferry_103_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        else:
            print("-----ERROR-----")
            return business2lang()
    elif chse == 4:
        print("-"*30)
        ferryID_104_b()
        if 0 in ferry_104_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_104_b[1] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "104 | TIME: 07:00PM"
                user()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        elif 0 not in ferry_104_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                business2lang()
            else:
                print("-----ERROR-----")
                return business2lang()
        else:
            print("-----ERROR-----")
            return main_menu()
    elif chse == 5:
        main_menu()
    else:
        print("-----ERROR-----")
        return business2lang()

#----------------------ECONOMY CLASS 2 LANGKAWI--------------------------
def economy2lang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*30)
    des_time2lang()
    chse = int(input("Choose:- "))
    if chse == 1:
        print("-"*30)
        ferryID_101_e()
        if 0 in ferry_101_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_101_e[31] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E32"
                trip_ferry = "101 | TIME: 10:00AM"
                user()
            elif chse_1 == "NO":
                economy2lang()
            else:
                print("-----ERROR-----")
                return economy2lang()
        elif 0 not in ferry_101_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                sub_menu()
            else:
                print("-----ERROR-----")
                return economy2lang()
        else:
            print("-----ERROR-----")
            return economy2lang()
    elif chse == 2:
        print("-"*30)
        ferryID_102_e()
        if 0 in ferry_102_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_102_e[32] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E33"
                trip_ferry = "102 | TIME: 01:00PM"
                user()
            elif chse_1 == "NO":
                economy2lang()
            else:
                print("-----ERROR-----")
                return economy2lang()
        elif 0 not in ferry_102_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                sub_menu()
            else:
                print("-----ERROR-----")
                return economy2lang()
        else:
            print("-----ERROR-----")
            return economy2lang()
    elif chse == 3:
        print("-"*30)
        ferryID_103_e()
        if 0 in ferry_103_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                trip = "PENANG---->LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E40"
                trip_ferry = "103 | TIME: 04:00PM"
                user()
            elif chse_1 == "NO":
                economy2lang()
            else:
                print("-----ERROR-----")
                return economy2lang()
        elif 0 not in ferry_103_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                sub_menu()
            else:
                print("-----ERROR-----")
                return economy2lang()
        else:
            print("-----ERROR-----")
            return economy2lang()
    elif chse == 4:
        print("-"*30)
        ferryID_104_e()
        if 0 in ferry_104_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_104_e[38] = 1
                trip = "PENANG---->LANGKAWI"
                trip_class = "Economy"
                trip_seat = "E39"
                trip_ferry = "104 | TIME: 07:00PM"
                user()
            elif chse_1 == "NO":
                economy2lang()
            else:
                print("-----ERROR-----")
                return economy2lang()
        elif 0 not in ferry_104_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                economy2lang()
            elif chse_1 == "NO":
                sub_menu()
            else:
                print("-----ERROR-----")
                return economy2lang()
        else:
            print("-----ERROR-----")
            return economy2lang()
    elif chse == 5:
        main_menu()
    else:
        print("-----ERROR-----")
        return business2lang()

#----------------------BUSINESS CLASS 2 PENANG---------------------------

def business2penang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*30)
    des_time2penang()
    chse = int(input("Choose:- "))
    if chse == 1:
        print("-"*30)
        ferryID_201_b()
        if 0 in ferry_201_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_201_b[1] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Business"
                trip_seat = "B02"
                trip_ferry = "201 | TIME: 11:00AM"
                user()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        elif 0 not in ferry_201_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        else:
            print("-----ERROR-----")
            return business2penang()
    elif chse == 2:
        print("-"*30)
        ferryID_202_b()
        if 0 in ferry_202_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_202_b[6] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Business"
                trip_seat = "B07"
                trip_ferry = "202 | TIME: 02:00PM"
                user()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        elif 0 not in ferry_202_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        else:
            print("-----ERROR-----")
            return business2penang()
    elif chse == 3:
        print("-"*30)
        ferryID_203_b()
        if 0 in ferry_203_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_203_b[4] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Business"
                trip_seat = "B05"
                trip_ferry = "203 | TIME: 05:00PM"
                user()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        elif 0 not in ferry_203_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        else:
            print("-----ERROR-----")
            return business2penang()
    elif chse == 4:
        print("-"*30)
        ferryID_204_b()
        if 0 in ferry_204_b:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_204_b[5] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Business"
                trip_seat = "B06"
                trip_ferry = "204 | TIME: 08:00PM"
                user()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        elif 0 not in ferry_204_b:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("You can choose economy YES/NO:- ").upper())
            if chse_1 == "YES":
                economy()
            elif chse_1 == "NO":
                business2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        else:
            print("-----ERROR-----")
            return main_menu()
    elif chse == 5:
        main_menu()
    else:
        print("-----ERROR-----")
        return business2penang()

#----------------------ECONOMY CLASS 2 PENANG--------------------------
def economy2penang():
    global trip
    global trip_seat
    global trip_class
    global trip_ferry
    print("-"*30)
    des_time2penang()
    chse = int(input("Choose:- "))
    if chse == 1:
        print("-"*30)
        ferryID_201_e()
        if 0 in ferry_201_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_201_e[11] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Economy"
                trip_seat = "E12"
                trip_ferry = "201 | TIME: 11:00AM"
                user()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        elif 0 not in ferry_201_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- "))
            if chse_1 == "yes":
                des_time2penang()
            elif chse_1 == "no":
                economy2penang()
            else:
                print("-----ERROR-----")
                return economy2penang()
        else:
            print("-----ERROR-----")
            return economy2penang()
    elif chse == 2:
        print("-"*30)
        ferryID_202_e()
        if 0 in ferry_202_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_202_e[37] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Economy"
                trip_seat = "E38"
                trip_ferry = "202 | TIME: 02:00PM"
                user()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return economy2penang()
        elif 0 not in ferry_202_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                des_time2penang()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return economy2penang()
        else:
            print("-----ERROR-----")
            return economy2penang()
    elif chse == 3:
        print("-"*30)
        ferryID_203_e()
        if 0 in ferry_203_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_203_e[32] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Economy"
                trip_seat = "E33"
                trip_ferry = "203 | TIME: 05:00PM"
                user()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return business2penang()
        elif 0 not in ferry_203_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                des_time2penang()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return economy2penang()
        else:
            print("-----ERROR-----")
            return economy2penang()
    elif chse == 4:
        print("-"*30)
        ferryID_204_e()
        if 0 in ferry_204_e:
            chse_1 = str(input("Buy Ticket? YES/NO:- ").upper())
            if chse_1 == "YES":
                ferry_204_e[39] = 1
                trip = "LANGKAWI---->PENANG"
                trip_class = "Economy"
                trip_seat = "E40"
                trip_ferry = "204 | TIME: 08:00PM"
                user()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return economy2penang()
        elif 0 not in ferry_204_e:
            print("Sorry la there is no space available Next trip after 3 hour")
            chse_1 = str(input("Change Time? YES/NO:- ").upper())
            if chse_1 == "YES":
                des_time2penang()
            elif chse_1 == "NO":
                economy2penang()
            else:
                print("-----ERROR-----")
                return economy2penang()
        else:
            print("-----ERROR-----")
            return economy2penang()
    elif chse == 5:
        main_menu()
    else:
        print("-----ERROR-----")
        return economy2penang()

def user():
    print("-"*30)
    global f_name
    global l_name
    f_name = str(input("Enter Your First Name:- ").title())
    l_name = str(input("Enter Your Last Name:- ").title())
    purchase()

def purchase():
    print("\n"*20)
    print("*"*17, "Thank You", "*"*17)
    print("* Destination: ", trip)
    print("*"*45)
    print("* FERRY ID: ", trip_ferry, date)
    print("* Class:    ", trip_class)
    print("* Name :    ", f_name, l_name)
    print("*"*45)
    print("\n--[1] Back to Main Menu--[2] Quite--")
    ticket()
    ch2 = int(input("Enter:- "))
    if ch2 == 1:
        main_menu()
    elif ch2 == 2:
        quit()
    else:
        quit()

def ticket():
    file = open("Ticket.txt", "w")
    print("*"*17, "Thank You", "*"*17, file = open("Ticket.txt", "a"))
    print("* Destination: ", trip, file = open("Ticket.txt", "a"))
    print("*"*45, file = open("Ticket.txt", "a"))
    print("* FERRY ID: ", trip_ferry, date, file = open("Ticket.txt", "a"))
    print("* Class:    ", trip_class, file = open("Ticket.txt", "a"))
    print("* Name :    ", f_name, l_name, file = open("Ticket.txt", "a"))
    print("*"*45, file = open("Ticket.txt", "a"))
    file.close()

def fer_ID():
    print("*"*29)
    print("*     PENANG ---> LANGKAWI    ")
    print("-"*29)
    print("Ferry ID: 101 -------- 10:00AM")
    print("Ferry ID: 102 -------- 01:00PM")
    print("Ferry ID: 103 -------- 04:00PM")
    print("Ferry ID: 104 -------- 07:00PM")
    print("*"*29)
    print("*     LANGKAWI ---> PENANG    ")
    print("-"*29)
    print("Ferry ID: 201 -------- 11:00PM")
    print("Ferry ID: 202 -------- 02:00PM")
    print("Ferry ID: 203 -------- 05:00PM")
    print("Ferry ID: 204 -------- 08:00PM")
    print("*"*29)
    type = input("TYPE ANY BUTTON TO BACK MAIN MENU:- ")
    if type == "":
        main_menu()
    else:
        main_menu()

def destination():
    print("-"*30)
    print("*"*30)
    print("*     CHOOSE DESTINATION     *")
    print("*"*30)
    print("[1] Penang -----> Langkawi")
    print("[2] Langkawi -----> Penang")
    print("[3] Back\n")

def des_time2lang():
    print("\nChoose Time:")
    print("\n[1]-10:00AM\n[2]-01:00PM\n[3]-04:OOPM\n[4]-07:00PM\n[5]-Back to Main Menu")

def des_time2penang():
    print("\nChoose Time:")
    print("\n[1]-11:00AM\n[2]-02:00PM\n[3]-05:OOPM\n[4]-08:00PM\n[5]-Back to Main Menu")

def arrangement():
    destination()
    way_1 = int(input("\nCheck Your Destination:- "))
    if way_1 == 1:
        des_time2lang()
        ch1 = int(input("\nChoose Time:- "))
        if ch1 == 1:
            ferryID_101()
            main_menu()
        elif ch1 == 2:
            ferryID_102()
            main_menu()
        elif ch1 == 3:
            ferryID_103()
            main_menu()
        elif ch1 == 4:
            ferryID_104()
            main_menu()
        elif ch1 == 5:
            main_menu()
        else:
            print("Invalid Value")
            return destination()
    elif way_1 == 2:
        des_time2penang()
        ch1 = int(input("\nChoose Time: "))
        if ch1 == 1:
            ferryID_201()
            main_menu()
        elif ch1 == 2:
            ferryID_202()
            main_menu()
        elif ch1 == 3:
            ferryID_203()
            main_menu()
        elif ch1 == 4:
            ferryID_204()
            main_menu()
        elif ch1 == 5:
            main_menu()
        else:
            print("Invalid Value")
            return destination()
    else:
        print("Invalid Value")
        return arrangement()

#----------------------FERRY ID FOR LANGKAWI----------------------------
#FerryID 1:
ferry_101_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
ferry_101_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_101_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 101                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[0], "     *     ",ferry_101_b[1], "     *     ",ferry_101_b[2], "     *     ",ferry_101_b[3], "     *     ",ferry_101_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[5], "     *     ",ferry_101_b[6], "     *     ",ferry_101_b[7], "     *     ",ferry_101_b[8], "     *     ",ferry_101_b[9], "     *")
    print("***********************************************************************")
def ferryID_101_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 101                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[0], "     *     ",ferry_101_e[1], "     *     ",ferry_101_e[2], "     *     ",ferry_101_e[3], "     *     ",ferry_101_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[5], "     *     ",ferry_101_e[6], "     *     ",ferry_101_e[7], "     *     ",ferry_101_e[8], "     *     ",ferry_101_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[10], "     *     ",ferry_101_e[11], "     *     ",ferry_101_e[12], "     *     ",ferry_101_e[13], "     *     ",ferry_101_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[15], "     *     ",ferry_101_e[16], "     *     ",ferry_101_e[17], "     *     ",ferry_101_e[18], "     *     ",ferry_101_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[20], "     *     ",ferry_101_e[21], "     *     ",ferry_101_e[22], "     *     ",ferry_101_e[23], "     *     ",ferry_101_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[25], "     *     ",ferry_101_e[26], "     *     ",ferry_101_e[27], "     *     ",ferry_101_e[28], "     *     ",ferry_101_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[30], "     *     ",ferry_101_e[31], "     *     ",ferry_101_e[32], "     *     ",ferry_101_e[33], "     *     ",ferry_101_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[35], "     *     ",ferry_101_e[36], "     *     ",ferry_101_e[37], "     *     ",ferry_101_e[38], "     *     ",ferry_101_e[39], "     *")
    print("***********************************************************************")

def ferryID_101():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 101                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[0], "     *     ",ferry_101_b[1], "     *     ",ferry_101_b[2], "     *     ",ferry_101_b[3], "     *     ",ferry_101_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_b[5], "     *     ",ferry_101_b[6], "     *     ",ferry_101_b[7], "     *     ",ferry_101_b[8], "     *     ",ferry_101_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[0], "     *     ",ferry_101_e[1], "     *     ",ferry_101_e[2], "     *     ",ferry_101_e[3], "     *     ",ferry_101_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[5], "     *     ",ferry_101_e[6], "     *     ",ferry_101_e[7], "     *     ",ferry_101_e[8], "     *     ",ferry_101_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[10], "     *     ",ferry_101_e[11], "     *     ",ferry_101_e[12], "     *     ",ferry_101_e[13], "     *     ",ferry_101_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[15], "     *     ",ferry_101_e[16], "     *     ",ferry_101_e[17], "     *     ",ferry_101_e[18], "     *     ",ferry_101_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[20], "     *     ",ferry_101_e[21], "     *     ",ferry_101_e[22], "     *     ",ferry_101_e[23], "     *     ",ferry_101_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[25], "     *     ",ferry_101_e[26], "     *     ",ferry_101_e[27], "     *     ",ferry_101_e[28], "     *     ",ferry_101_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[30], "     *     ",ferry_101_e[31], "     *     ",ferry_101_e[32], "     *     ",ferry_101_e[33], "     *     ",ferry_101_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_101_e[35], "     *     ",ferry_101_e[36], "     *     ",ferry_101_e[37], "     *     ",ferry_101_e[38], "     *     ",ferry_101_e[39], "     *")
    print("***********************************************************************")

#FerryID 2:
ferry_102_b = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
ferry_102_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_102_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 102                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[0], "     *     ",ferry_102_b[1], "     *     ",ferry_102_b[2], "     *     ",ferry_102_b[3], "     *     ",ferry_102_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[5], "     *     ",ferry_102_b[6], "     *     ",ferry_102_b[7], "     *     ",ferry_102_b[8], "     *     ",ferry_102_b[9], "     *")
    print("***********************************************************************")
def ferryID_102_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 102                        Time: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[0], "     *     ",ferry_102_e[1], "     *     ",ferry_102_e[2], "     *     ",ferry_102_e[3], "     *     ",ferry_102_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[5], "     *     ",ferry_102_e[6], "     *     ",ferry_102_e[7], "     *     ",ferry_102_e[8], "     *     ",ferry_102_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[10], "     *     ",ferry_102_e[11], "     *     ",ferry_102_e[12], "     *     ",ferry_102_e[13], "     *     ",ferry_102_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[15], "     *     ",ferry_102_e[16], "     *     ",ferry_102_e[17], "     *     ",ferry_102_e[18], "     *     ",ferry_102_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[20], "     *     ",ferry_102_e[21], "     *     ",ferry_102_e[22], "     *     ",ferry_102_e[23], "     *     ",ferry_102_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[25], "     *     ",ferry_102_e[26], "     *     ",ferry_102_e[27], "     *     ",ferry_102_e[28], "     *     ",ferry_102_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[30], "     *     ",ferry_102_e[31], "     *     ",ferry_102_e[32], "     *     ",ferry_102_e[33], "     *     ",ferry_102_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[35], "     *     ",ferry_102_e[36], "     *     ",ferry_102_e[37], "     *     ",ferry_102_e[38], "     *     ",ferry_102_e[39], "     *")
    print("***********************************************************************")

def ferryID_102():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 102                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[0], "     *     ",ferry_102_b[1], "     *     ",ferry_102_b[2], "     *     ",ferry_102_b[3], "     *     ",ferry_102_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_b[5], "     *     ",ferry_102_b[6], "     *     ",ferry_102_b[7], "     *     ",ferry_102_b[8], "     *     ",ferry_102_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[0], "     *     ",ferry_102_e[1], "     *     ",ferry_102_e[2], "     *     ",ferry_102_e[3], "     *     ",ferry_102_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[5], "     *     ",ferry_102_e[6], "     *     ",ferry_102_e[7], "     *     ",ferry_102_e[8], "     *     ",ferry_102_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[10], "     *     ",ferry_102_e[11], "     *     ",ferry_102_e[12], "     *     ",ferry_102_e[13], "     *     ",ferry_102_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[15], "     *     ",ferry_102_e[16], "     *     ",ferry_102_e[17], "     *     ",ferry_102_e[18], "     *     ",ferry_102_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[20], "     *     ",ferry_102_e[21], "     *     ",ferry_102_e[22], "     *     ",ferry_102_e[23], "     *     ",ferry_102_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[25], "     *     ",ferry_102_e[26], "     *     ",ferry_102_e[27], "     *     ",ferry_102_e[28], "     *     ",ferry_102_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[30], "     *     ",ferry_102_e[31], "     *     ",ferry_102_e[32], "     *     ",ferry_102_e[33], "     *     ",ferry_102_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_102_e[35], "     *     ",ferry_102_e[36], "     *     ",ferry_102_e[37], "     *     ",ferry_102_e[38], "     *     ",ferry_102_e[39], "     *")
    print("***********************************************************************")

#FerryID 3:
ferry_103_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ferry_103_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def ferryID_103_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 103                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[0], "     *     ",ferry_103_b[1], "     *     ",ferry_103_b[2], "     *     ",ferry_103_b[3], "     *     ",ferry_103_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[5], "     *     ",ferry_103_b[6], "     *     ",ferry_103_b[7], "     *     ",ferry_103_b[8], "     *     ",ferry_103_b[9], "     *")
    print("***********************************************************************")
def ferryID_103_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 103                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[0], "     *     ",ferry_103_e[1], "     *     ",ferry_103_e[2], "     *     ",ferry_103_e[3], "     *     ",ferry_103_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[5], "     *     ",ferry_103_e[6], "     *     ",ferry_103_e[7], "     *     ",ferry_103_e[8], "     *     ",ferry_103_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[10], "     *     ",ferry_103_e[11], "     *     ",ferry_103_e[12], "     *     ",ferry_103_e[13], "     *     ",ferry_103_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[15], "     *     ",ferry_103_e[16], "     *     ",ferry_103_e[17], "     *     ",ferry_103_e[18], "     *     ",ferry_103_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[20], "     *     ",ferry_103_e[21], "     *     ",ferry_103_e[22], "     *     ",ferry_103_e[23], "     *     ",ferry_103_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[25], "     *     ",ferry_103_e[26], "     *     ",ferry_103_e[27], "     *     ",ferry_103_e[28], "     *     ",ferry_103_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[30], "     *     ",ferry_103_e[31], "     *     ",ferry_103_e[32], "     *     ",ferry_103_e[33], "     *     ",ferry_103_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[35], "     *     ",ferry_103_e[36], "     *     ",ferry_103_e[37], "     *     ",ferry_103_e[38], "     *     ",ferry_103_e[39], "     *")
    print("***********************************************************************")

def ferryID_103():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 103                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[0], "     *     ",ferry_103_b[1], "     *     ",ferry_103_b[2], "     *     ",ferry_103_b[3], "     *     ",ferry_103_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_b[5], "     *     ",ferry_103_b[6], "     *     ",ferry_103_b[7], "     *     ",ferry_103_b[8], "     *     ",ferry_103_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[0], "     *     ",ferry_103_e[1], "     *     ",ferry_103_e[2], "     *     ",ferry_103_e[3], "     *     ",ferry_103_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[5], "     *     ",ferry_103_e[6], "     *     ",ferry_103_e[7], "     *     ",ferry_103_e[8], "     *     ",ferry_103_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[10], "     *     ",ferry_103_e[11], "     *     ",ferry_103_e[12], "     *     ",ferry_103_e[13], "     *     ",ferry_103_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[15], "     *     ",ferry_103_e[16], "     *     ",ferry_103_e[17], "     *     ",ferry_103_e[18], "     *     ",ferry_103_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[20], "     *     ",ferry_103_e[21], "     *     ",ferry_103_e[22], "     *     ",ferry_103_e[23], "     *     ",ferry_103_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[25], "     *     ",ferry_103_e[26], "     *     ",ferry_103_e[27], "     *     ",ferry_103_e[28], "     *     ",ferry_103_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[30], "     *     ",ferry_103_e[31], "     *     ",ferry_103_e[32], "     *     ",ferry_103_e[33], "     *     ",ferry_103_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_103_e[35], "     *     ",ferry_103_e[36], "     *     ",ferry_103_e[37], "     *     ",ferry_103_e[38], "     *     ",ferry_103_e[39], "     *")
    print("***********************************************************************")

#FerryID 4:
ferry_104_b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ferry_104_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_104_b():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 104                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[0], "     *     ",ferry_104_b[1], "     *     ",ferry_104_b[2], "     *     ",ferry_104_b[3], "     *     ",ferry_104_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[5], "     *     ",ferry_104_b[6], "     *     ",ferry_104_b[7], "     *     ",ferry_104_b[8], "     *     ",ferry_104_b[9], "     *")
    print("***********************************************************************")
def ferryID_104_e():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 104                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[0], "     *     ",ferry_104_e[1], "     *     ",ferry_104_e[2], "     *     ",ferry_104_e[3], "     *     ",ferry_104_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[5], "     *     ",ferry_104_e[6], "     *     ",ferry_104_e[7], "     *     ",ferry_104_e[8], "     *     ",ferry_104_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[10], "     *     ",ferry_104_e[11], "     *     ",ferry_104_e[12], "     *     ",ferry_104_e[13], "     *     ",ferry_104_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[15], "     *     ",ferry_104_e[16], "     *     ",ferry_104_e[17], "     *     ",ferry_104_e[18], "     *     ",ferry_104_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[20], "     *     ",ferry_104_e[21], "     *     ",ferry_104_e[22], "     *     ",ferry_104_e[23], "     *     ",ferry_104_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[25], "     *     ",ferry_104_e[26], "     *     ",ferry_104_e[27], "     *     ",ferry_104_e[28], "     *     ",ferry_104_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[30], "     *     ",ferry_104_e[31], "     *     ",ferry_104_e[32], "     *     ",ferry_104_e[33], "     *     ",ferry_104_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[35], "     *     ",ferry_104_e[36], "     *     ",ferry_104_e[37], "     *     ",ferry_104_e[38], "     *     ",ferry_104_e[39], "     *")
    print("***********************************************************************")

def ferryID_104():
    print("***********************************************************************")
    print("*                     PENANG TO LANGKAWI                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 104                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[0], "     *     ",ferry_104_b[1], "     *     ",ferry_104_b[2], "     *     ",ferry_104_b[3], "     *     ",ferry_104_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_b[5], "     *     ",ferry_104_b[6], "     *     ",ferry_104_b[7], "     *     ",ferry_104_b[8], "     *     ",ferry_104_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[0], "     *     ",ferry_104_e[1], "     *     ",ferry_104_e[2], "     *     ",ferry_104_e[3], "     *     ",ferry_104_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[5], "     *     ",ferry_104_e[6], "     *     ",ferry_104_e[7], "     *     ",ferry_104_e[8], "     *     ",ferry_104_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[10], "     *     ",ferry_104_e[11], "     *     ",ferry_104_e[12], "     *     ",ferry_104_e[13], "     *     ",ferry_104_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[15], "     *     ",ferry_104_e[16], "     *     ",ferry_104_e[17], "     *     ",ferry_104_e[18], "     *     ",ferry_104_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[20], "     *     ",ferry_104_e[21], "     *     ",ferry_104_e[22], "     *     ",ferry_104_e[23], "     *     ",ferry_104_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[25], "     *     ",ferry_104_e[26], "     *     ",ferry_104_e[27], "     *     ",ferry_104_e[28], "     *     ",ferry_104_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[30], "     *     ",ferry_104_e[31], "     *     ",ferry_104_e[32], "     *     ",ferry_104_e[33], "     *     ",ferry_104_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_104_e[35], "     *     ",ferry_104_e[36], "     *     ",ferry_104_e[37], "     *     ",ferry_104_e[38], "     *     ",ferry_104_e[39], "     *")
    print("***********************************************************************")

#----------------------FERRY ID FOR PENANG----------------------------
#FerryID 1:
ferry_201_b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ferry_201_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_201_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 201                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[0], "     *     ",ferry_201_b[1], "     *     ",ferry_201_b[2], "     *     ",ferry_201_b[3], "     *     ",ferry_201_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[5], "     *     ",ferry_201_b[6], "     *     ",ferry_201_b[7], "     *     ",ferry_201_b[8], "     *     ",ferry_201_b[9], "     *")
    print("***********************************************************************")
def ferryID_201_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 201                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[0], "     *     ",ferry_201_e[1], "     *     ",ferry_201_e[2], "     *     ",ferry_201_e[3], "     *     ",ferry_201_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[5], "     *     ",ferry_201_e[6], "     *     ",ferry_201_e[7], "     *     ",ferry_201_e[8], "     *     ",ferry_201_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[10], "     *     ",ferry_201_e[11], "     *     ",ferry_201_e[12], "     *     ",ferry_201_e[13], "     *     ",ferry_201_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[15], "     *     ",ferry_201_e[16], "     *     ",ferry_201_e[17], "     *     ",ferry_201_e[18], "     *     ",ferry_201_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[20], "     *     ",ferry_201_e[21], "     *     ",ferry_201_e[22], "     *     ",ferry_201_e[23], "     *     ",ferry_201_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[25], "     *     ",ferry_201_e[26], "     *     ",ferry_201_e[27], "     *     ",ferry_201_e[28], "     *     ",ferry_201_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[30], "     *     ",ferry_201_e[31], "     *     ",ferry_201_e[32], "     *     ",ferry_201_e[33], "     *     ",ferry_201_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[35], "     *     ",ferry_201_e[36], "     *     ",ferry_201_e[37], "     *     ",ferry_201_e[38], "     *     ",ferry_201_e[39], "     *")
    print("***********************************************************************")

def ferryID_201():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 201                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[0], "     *     ",ferry_201_b[1], "     *     ",ferry_201_b[2], "     *     ",ferry_201_b[3], "     *     ",ferry_201_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_b[5], "     *     ",ferry_201_b[6], "     *     ",ferry_201_b[7], "     *     ",ferry_201_b[8], "     *     ",ferry_201_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[0], "     *     ",ferry_201_e[1], "     *     ",ferry_201_e[2], "     *     ",ferry_201_e[3], "     *     ",ferry_201_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[5], "     *     ",ferry_201_e[6], "     *     ",ferry_201_e[7], "     *     ",ferry_201_e[8], "     *     ",ferry_201_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[10], "     *     ",ferry_201_e[11], "     *     ",ferry_201_e[12], "     *     ",ferry_201_e[13], "     *     ",ferry_201_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[15], "     *     ",ferry_201_e[16], "     *     ",ferry_201_e[17], "     *     ",ferry_201_e[18], "     *     ",ferry_201_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[20], "     *     ",ferry_201_e[21], "     *     ",ferry_201_e[22], "     *     ",ferry_201_e[23], "     *     ",ferry_201_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[25], "     *     ",ferry_201_e[26], "     *     ",ferry_201_e[27], "     *     ",ferry_201_e[28], "     *     ",ferry_201_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[30], "     *     ",ferry_201_e[31], "     *     ",ferry_201_e[32], "     *     ",ferry_201_e[33], "     *     ",ferry_201_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_201_e[35], "     *     ",ferry_201_e[36], "     *     ",ferry_201_e[37], "     *     ",ferry_201_e[38], "     *     ",ferry_201_e[39], "     *")
    print("***********************************************************************")

#FerryID 2:
ferry_202_b = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
ferry_202_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_202_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 202                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[0], "     *     ",ferry_202_b[1], "     *     ",ferry_202_b[2], "     *     ",ferry_202_b[3], "     *     ",ferry_202_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[5], "     *     ",ferry_202_b[6], "     *     ",ferry_202_b[7], "     *     ",ferry_202_b[8], "     *     ",ferry_202_b[9], "     *")
    print("***********************************************************************")

def ferryID_202_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 202                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[0], "     *     ",ferry_202_e[1], "     *     ",ferry_202_e[2], "     *     ",ferry_202_e[3], "     *     ",ferry_202_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[5], "     *     ",ferry_202_e[6], "     *     ",ferry_202_e[7], "     *     ",ferry_202_e[8], "     *     ",ferry_202_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[10], "     *     ",ferry_202_e[11], "     *     ",ferry_202_e[12], "     *     ",ferry_202_e[13], "     *     ",ferry_202_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[15], "     *     ",ferry_202_e[16], "     *     ",ferry_202_e[17], "     *     ",ferry_202_e[18], "     *     ",ferry_202_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[20], "     *     ",ferry_202_e[21], "     *     ",ferry_202_e[22], "     *     ",ferry_202_e[23], "     *     ",ferry_202_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[25], "     *     ",ferry_202_e[26], "     *     ",ferry_202_e[27], "     *     ",ferry_202_e[28], "     *     ",ferry_202_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[30], "     *     ",ferry_202_e[31], "     *     ",ferry_202_e[32], "     *     ",ferry_202_e[33], "     *     ",ferry_202_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[35], "     *     ",ferry_202_e[36], "     *     ",ferry_202_e[37], "     *     ",ferry_202_e[38], "     *     ",ferry_202_e[39], "     *")
    print("***********************************************************************")

def ferryID_202():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 202                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[0], "     *     ",ferry_202_b[1], "     *     ",ferry_202_b[2], "     *     ",ferry_202_b[3], "     *     ",ferry_202_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_b[5], "     *     ",ferry_202_b[6], "     *     ",ferry_202_b[7], "     *     ",ferry_202_b[8], "     *     ",ferry_202_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[0], "     *     ",ferry_202_e[1], "     *     ",ferry_202_e[2], "     *     ",ferry_202_e[3], "     *     ",ferry_202_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[5], "     *     ",ferry_202_e[6], "     *     ",ferry_202_e[7], "     *     ",ferry_202_e[8], "     *     ",ferry_202_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[10], "     *     ",ferry_202_e[11], "     *     ",ferry_202_e[12], "     *     ",ferry_202_e[13], "     *     ",ferry_202_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[15], "     *     ",ferry_202_e[16], "     *     ",ferry_202_e[17], "     *     ",ferry_202_e[18], "     *     ",ferry_202_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[20], "     *     ",ferry_202_e[21], "     *     ",ferry_202_e[22], "     *     ",ferry_202_e[23], "     *     ",ferry_202_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[25], "     *     ",ferry_202_e[26], "     *     ",ferry_202_e[27], "     *     ",ferry_202_e[28], "     *     ",ferry_202_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[30], "     *     ",ferry_202_e[31], "     *     ",ferry_202_e[32], "     *     ",ferry_202_e[33], "     *     ",ferry_202_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_202_e[35], "     *     ",ferry_202_e[36], "     *     ",ferry_202_e[37], "     *     ",ferry_202_e[38], "     *     ",ferry_202_e[39], "     *")
    print("***********************************************************************")

#FerryID 3:
ferry_203_b = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
ferry_203_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_203_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 203                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[0], "     *     ",ferry_203_b[1], "     *     ",ferry_203_b[2], "     *     ",ferry_203_b[3], "     *     ",ferry_203_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[5], "     *     ",ferry_203_b[6], "     *     ",ferry_203_b[7], "     *     ",ferry_203_b[8], "     *     ",ferry_203_b[9], "     *")
    print("***********************************************************************")

def ferryID_203_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 203                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[0], "     *     ",ferry_203_e[1], "     *     ",ferry_203_e[2], "     *     ",ferry_203_e[3], "     *     ",ferry_203_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[5], "     *     ",ferry_203_e[6], "     *     ",ferry_203_e[7], "     *     ",ferry_203_e[8], "     *     ",ferry_203_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[10], "     *     ",ferry_203_e[11], "     *     ",ferry_203_e[12], "     *     ",ferry_203_e[13], "     *     ",ferry_203_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[15], "     *     ",ferry_203_e[16], "     *     ",ferry_203_e[17], "     *     ",ferry_203_e[18], "     *     ",ferry_203_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[20], "     *     ",ferry_203_e[21], "     *     ",ferry_203_e[22], "     *     ",ferry_203_e[23], "     *     ",ferry_203_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[25], "     *     ",ferry_203_e[26], "     *     ",ferry_203_e[27], "     *     ",ferry_203_e[28], "     *     ",ferry_203_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[30], "     *     ",ferry_203_e[31], "     *     ",ferry_203_e[32], "     *     ",ferry_203_e[33], "     *     ",ferry_203_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[35], "     *     ",ferry_203_e[36], "     *     ",ferry_203_e[37], "     *     ",ferry_203_e[38], "     *     ",ferry_203_e[39], "     *")
    print("***********************************************************************")

def ferryID_203():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 203                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[0], "     *     ",ferry_203_b[1], "     *     ",ferry_203_b[2], "     *     ",ferry_203_b[3], "     *     ",ferry_203_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_b[5], "     *     ",ferry_203_b[6], "     *     ",ferry_203_b[7], "     *     ",ferry_203_b[8], "     *     ",ferry_203_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[0], "     *     ",ferry_203_e[1], "     *     ",ferry_203_e[2], "     *     ",ferry_203_e[3], "     *     ",ferry_203_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[5], "     *     ",ferry_203_e[6], "     *     ",ferry_203_e[7], "     *     ",ferry_203_e[8], "     *     ",ferry_203_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[10], "     *     ",ferry_203_e[11], "     *     ",ferry_203_e[12], "     *     ",ferry_203_e[13], "     *     ",ferry_203_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[15], "     *     ",ferry_203_e[16], "     *     ",ferry_203_e[17], "     *     ",ferry_203_e[18], "     *     ",ferry_203_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[20], "     *     ",ferry_203_e[21], "     *     ",ferry_203_e[22], "     *     ",ferry_203_e[23], "     *     ",ferry_203_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[25], "     *     ",ferry_203_e[26], "     *     ",ferry_203_e[27], "     *     ",ferry_203_e[28], "     *     ",ferry_203_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[30], "     *     ",ferry_203_e[31], "     *     ",ferry_203_e[32], "     *     ",ferry_203_e[33], "     *     ",ferry_203_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_203_e[35], "     *     ",ferry_203_e[36], "     *     ",ferry_203_e[37], "     *     ",ferry_203_e[38], "     *     ",ferry_203_e[39], "     *")
    print("***********************************************************************")

#FerryID 4:
ferry_204_b = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
ferry_204_e =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def ferryID_204_b():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 204                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[0], "     *     ",ferry_204_b[1], "     *     ",ferry_204_b[2], "     *     ",ferry_204_b[3], "     *     ",ferry_204_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[5], "     *     ",ferry_204_b[6], "     *     ",ferry_204_b[7], "     *     ",ferry_204_b[8], "     *     ",ferry_204_b[9], "     *")
    print("***********************************************************************")

def ferryID_204_e():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 204                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[0], "     *     ",ferry_204_e[1], "     *     ",ferry_204_e[2], "     *     ",ferry_204_e[3], "     *     ",ferry_204_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[5], "     *     ",ferry_204_e[6], "     *     ",ferry_204_e[7], "     *     ",ferry_204_e[8], "     *     ",ferry_204_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[10], "     *     ",ferry_204_e[11], "     *     ",ferry_204_e[12], "     *     ",ferry_204_e[13], "     *     ",ferry_204_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[15], "     *     ",ferry_204_e[16], "     *     ",ferry_204_e[17], "     *     ",ferry_204_e[18], "     *     ",ferry_204_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[20], "     *     ",ferry_204_e[21], "     *     ",ferry_204_e[22], "     *     ",ferry_204_e[23], "     *     ",ferry_204_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[25], "     *     ",ferry_204_e[26], "     *     ",ferry_204_e[27], "     *     ",ferry_204_e[28], "     *     ",ferry_204_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[30], "     *     ",ferry_204_e[31], "     *     ",ferry_204_e[32], "     *     ",ferry_204_e[33], "     *     ",ferry_204_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[35], "     *     ",ferry_204_e[36], "     *     ",ferry_204_e[37], "     *     ",ferry_204_e[38], "     *     ",ferry_204_e[39], "     *")
    print("***********************************************************************")

def ferryID_204():
    print("***********************************************************************")
    print("*                     LANGKAWI TO PENANG                              *")
    print("***********************************************************************")
    print("*     Ferry ID: 204                        Date: ", date, "     *")
    print("***********************************************************************")
    print("*     BUSINESS CLASS                                                  *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[0], "     *     ",ferry_204_b[1], "     *     ",ferry_204_b[2], "     *     ",ferry_204_b[3], "     *     ",ferry_204_b[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_b[5], "     *     ",ferry_204_b[6], "     *     ",ferry_204_b[7], "     *     ",ferry_204_b[8], "     *     ",ferry_204_b[9], "     *")
    print("***********************************************************************")
    print("*     ECONOMY CLASS                                                   *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[0], "     *     ",ferry_204_e[1], "     *     ",ferry_204_e[2], "     *     ",ferry_204_e[3], "     *     ",ferry_204_e[4], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[5], "     *     ",ferry_204_e[6], "     *     ",ferry_204_e[7], "     *     ",ferry_204_e[8], "     *     ",ferry_204_e[9], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[10], "     *     ",ferry_204_e[11], "     *     ",ferry_204_e[12], "     *     ",ferry_204_e[13], "     *     ",ferry_204_e[14], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[15], "     *     ",ferry_204_e[16], "     *     ",ferry_204_e[17], "     *     ",ferry_204_e[18], "     *     ",ferry_204_e[19], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[20], "     *     ",ferry_204_e[21], "     *     ",ferry_204_e[22], "     *     ",ferry_204_e[23], "     *     ",ferry_204_e[24], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[25], "     *     ",ferry_204_e[26], "     *     ",ferry_204_e[27], "     *     ",ferry_204_e[28], "     *     ",ferry_204_e[29], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[30], "     *     ",ferry_204_e[31], "     *     ",ferry_204_e[32], "     *     ",ferry_204_e[33], "     *     ",ferry_204_e[34], "     *")
    print("***********************************************************************")
    print("*     ",ferry_204_e[35], "     *     ",ferry_204_e[36], "     *     ",ferry_204_e[37], "     *     ",ferry_204_e[38], "     *     ",ferry_204_e[39], "     *")
    print("***********************************************************************")

main_menu()
