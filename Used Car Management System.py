# Rachael Neo, 222743F, DBFT-06
# Import the necessary module
from colorama import init, Fore, Style

# Initialize colorama (required for Windows)
init()

class Car:

    def __init__(self, car_engineno, car_brand, car_type, mileage, regyear):
        self.__car_engineno = car_engineno
        self.__car_brand = car_brand
        self.__car_type = car_type
        self.__mileage = mileage
        self.__regyear = regyear

    def set_car_engineno(self, car_engineno):
        self.__car_engineno = car_engineno

    def set_car_brand(self, car_brand):
        self.__car_brand = car_brand

    def set_car_type(self, car_type):
        self.__car_type = car_type

    def set_mileage(self, mileage):
        if mileage.isnumeric():
            self.__mileage = mileage
        else:
            print('Mileage should be in numbers.')

    def set_regyear(self, regyear):
        if regyear.isnumeric():
            self.__regyear = regyear
        else:
            print('Register year should be in numbers.')


    def get_car_engineno(self):
        return self.__car_engineno

    def get_car_brand(self):
        return self.__car_brand

    def get_car_type(self):
        return self.__car_type

    def get_mileage(self):
        return self.__mileage

    def get_regyear(self):
        return self.__regyear


cars = []
command = 0


# Implementation of the Queue ADT using a Python list.
class Queue:
    # Creates an empty queue.
    def __init__(self):
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty(self):
        return len(self._qList) == 0

    # Returns the number of items in the queue.
    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue.
    def enqueue(self, item):
        self._qList.append(item)

    # Removes and returns the first item in the queue.
    def dequeue(self):
        # Assertion
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop(0) # take note of the diff between queue and stack remove items


# Empty dictionary
hardcode_customers = {}


# Appending the 3 customers details into hardcode_customers dictionary
def test_code_customerrequests():
    print(Style.BRIGHT + "Hardcoded Customers' Details:" + Style.RESET_ALL)
    # Updates the dictionary with the specified key-value pairs (3 customers)
    hardcode_customers.update(
        {
        "S888": {
            "Name": "Rachael",
            "Email": "rn@gmail.com",
            "Tier": "C",
            "Points": 9783,
        },
        "S222": {
            "Name": "Mike Johnson",
            "Email": "Mike@gmail.com",
            "Tier": "B",
            "Points": 486,
        },
        "S966": {
            "Name": "Tom Holland",
            "Email": "Tom@gmail.com",
            "Tier": "D",
            "Points": 1001,
        }
        }
    )

    print(hardcode_customers)
    print(" ")
    print(Fore.GREEN + "=== Hardcoded Customers' Details successfully added ===" + Style.RESET_ALL)

class CustomerRequest:

    def __init__(self, customer_ID, customer_request):
        self.customer_ID = customer_ID
        self.customer_request = customer_request

    def __str__(self):
        return "Customer ID: {}\nName: {}\nEmail: {}\nTier: {}\nPoints: {}\n----------------------------------------\nRequest: {}\n----------------------------------------\n".format(
            self.customer_ID, hardcode_customers[self.customer_ID]["Name"], hardcode_customers[self.customer_ID]["Email"],
            hardcode_customers[self.customer_ID]["Tier"], hardcode_customers[self.customer_ID]["Points"],
            self.customer_request
        )


def test_code_cars():
    print(Style.BRIGHT + "Hardcoded Cars' Records:" + Style.RESET_ALL)

    hardcode_cars = [
        Car("112251654254", "KIA", "SUV", 71000, 2021),
        Car("569325487515", "BMV", "Sedan", 20000, 2021),
        Car("515421693758", "TOYOTA", "Vellfire", 45000, 2022),
        Car("111111111111", "BMV", "Sedan", 20000, 2021),
        Car("221111111111", "BMV", "Sedan", 20000, 2022)
    ]                                                                       # Append the object into list (hardcode_cars)
                                                                            # Creating an object (Car Object)
    for car in hardcode_cars:
        cars.append(car)
        print(f"Car EngineNo= {car.get_car_engineno()}, Car Brand= {car.get_car_brand()}, Car Type= {car.get_car_type()}, Mileage= {car.get_mileage()}, Registered year= {car.get_regyear()}")
    print(" ")
    print(Fore.GREEN + "=== Hardcoded Cars' Records successfully added ===" + Style.RESET_ALL)

def display_cars():
    if cars == []:
        print(Fore.BLUE + "=== There are no records. ===" + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + "All Cars' Records:" + Style.RESET_ALL)
        for car in cars:
            print(f"Car EngineNo= {car.get_car_engineno()}, Car Brand= {car.get_car_brand()}, Car Type= {car.get_car_type()}, Mileage= {car.get_mileage()}, Registered year= {car.get_regyear()}")


def is_duplicate_engine_number(car_engineno):
    for car in cars:
        if car_engineno == car.get_car_engineno():
            return True
    return False


def add_record():
    print(Style.BRIGHT + "Adding new Car Record:" + Style.RESET_ALL)
    while True:
        car_engineno = input("Enter engine number: ")
        if not car_engineno.isnumeric() or len(car_engineno) != 12:
            print(Fore.RED + "Not a valid input. Please enter a 12-digit numeric value." + Style.RESET_ALL)
        elif is_duplicate_engine_number(car_engineno):
            print(Fore.YELLOW + "Car engine number already exists. Please enter a different engine number." + Style.RESET_ALL)
        else:
            break

    car_brand = input("Enter brand: ")
    while not car_brand.isalpha():
        print(Fore.RED + "Not a valid input. Please enter alphabetic characters." + Style.RESET_ALL)
        car_brand = input("Enter brand: ")

    car_type = input("Enter type: ")
    while not car_type.isalpha():
        print(Fore.RED + "Not a valid input. Please enter alphabetic characters." + Style.RESET_ALL)
        car_type = input("Enter type: ")

    # Capitalize the first letter of car_type
    car_type = car_type.capitalize()

    while True:
        mileage = input("Enter mileage: ")
        if not mileage.isnumeric():
            print(Fore.RED + "Not a valid input. Please enter numeric characters." + Style.RESET_ALL)
        elif len(mileage) < 5:
            print(Fore.YELLOW + "Mileage cannot be less than 5 digit." + Style.RESET_ALL)
            mileage = int(mileage)
        else:
            break

    while True:
            regyear = input("Enter registered year: ")
            if not regyear.isnumeric():
                print(Fore.RED + "Not a valid input. Please enter numeric characters." + Style.RESET_ALL)
            elif int(regyear) < 2013 or int(regyear) > 2023:
                print(Fore.YELLOW + "Registered year must be within 2013 and 2023." + Style.RESET_ALL)
            else:
                break

    car = Car(car_engineno, car_brand.upper(), car_type, mileage, regyear)
    cars.append(car)
    print(" ")
    print(Style.BRIGHT + "Newly Added Car Record:" + Style.RESET_ALL)
    print(f"Car EngineNo= {car.get_car_engineno()}, Car Brand= {car.get_car_brand()}, Car Type= {car.get_car_type()}, Mileage= {car.get_mileage()}, Registered year= {car.get_regyear()}")
    print(Fore.GREEN + "=== Car successfully added ===" + Style.RESET_ALL)


def update_cars_records(cars):
    while cars == []:
        print(Fore.BLUE + "=== There are no cars record. Please press 00 or 2 to add car record(s) first===" + Style.RESET_ALL)
        break
    else:
        update_car_engine_no = input("Enter the engine number of the car to update: ")

        def SequentialSearch(update_car_engine_no, theSeq):
            for car in theSeq:
                if car.get_car_engineno() == update_car_engine_no:
                    return True
            return False

        if SequentialSearch(update_car_engine_no, cars):
            for car in cars:
                if car.get_car_engineno() == update_car_engine_no:
                    car_brand = input("Enter brand: ")
                    while not car_brand.isalpha():
                        print(Fore.RED + "Not a valid input. Please enter alphabetic characters." + Style.RESET_ALL)
                        car_brand = input("Enter brand: ")

                    car_type = input("Enter type: ")
                    while not car_type.isalpha():
                        print(Fore.RED + "Not a valid input. Please enter alphabetic characters." + Style.RESET_ALL)
                        car_type = input("Enter type: ")

                    while True:
                            mileage = input("Enter mileage: ")
                            if not mileage.isnumeric():
                                print(Fore.RED + "Not a valid input. Please enter numeric characters." + Style.RESET_ALL)
                            elif len(mileage) < 5:
                                print(Fore.YELLOW + "Mileage cannot be less than 5 digit." + Style.RESET_ALL)
                                mileage = int(mileage)
                            else:
                                break

                    while True:
                            regyear = input("Enter registered year: ")
                            if not regyear.isnumeric():
                                print(Fore.RED + "Not a valid input. Please enter numeric characters." + Style.RESET_ALL)
                            elif int(regyear) < 2013 or int(regyear) > 2023:
                                print(Fore.YELLOW + "Registered year must be within 2013 and 2023." + Style.RESET_ALL)
                            else:
                                break

                    car.set_car_brand(car_brand.upper())
                    car.set_car_type(car_type)
                    car.set_mileage(mileage)
                    car.set_regyear(regyear)

                    print(Fore.GREEN + "=== Car record updated successfully ===" + Style.RESET_ALL)
                    break
        else:
            print(Fore.YELLOW + "Car engine number not found. Please enter a valid engine number." + Style.RESET_ALL)


def bubble_sort(theSeq):
    print(Fore.CYAN + "Car Brand in ascending order using Bubble Sort" + Style.RESET_ALL)
    print(" ")

    n = len(theSeq)
    if n == 0:
        print(Fore.BLUE + "=== There are no records. ===" + Style.RESET_ALL)
    else:
        # Perform n-1 bubble operations on the sequence
        for i in range(n - 1, 0, -1):

            # Bubble the largest item to the end
            for j in range(i):
                if theSeq[j].get_car_brand() > theSeq[j + 1].get_car_brand():
                    # Swap the j and j+1 items
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp

        display_cars()
        print(Fore.CYAN + "=== Sorted === " + Style.RESET_ALL)


def insertion_sort(theSeq):
    print(Fore.CYAN + "Mileage in descending order using Insertion Sort" + Style.RESET_ALL)
    print(" ")

    n = len(theSeq)
    if n == 0:
        print(Fore.BLUE + "=== There are no records. ===" + Style.RESET_ALL)
    else:
        for i in range(1, n):
            value = theSeq[i]   # Inside the loop, the current element at index 'i' is stored in the variable 'value'.
            pos = i             # Representing the current position
            while pos > 0 and value.get_mileage() > theSeq[pos - 1].get_mileage():
                theSeq[pos] = theSeq[pos - 1]
                pos -= 1

            theSeq[pos] = value

        display_cars()
        print(Fore.CYAN + "=== Sorted === " + Style.RESET_ALL)


def selection_sort(theSeq):
    print(Fore.CYAN + "Car Type in ascending order using Selection Sort" + Style.RESET_ALL)
    print(" ")

    n = len(theSeq)
    if n == 0:
        print(Fore.BLUE + "=== There are no records. ===" + Style.RESET_ALL)
    else:
        for i in range(n - 1):
            index = i

            for j in range(i + 1, n):
                if theSeq[j].get_car_type().lower() < theSeq[index].get_car_type().lower():
                    index = j

            if index != i:
                temp = theSeq[i]
                theSeq[i] = theSeq[index]
                theSeq[index] = temp

        display_cars()
        print(Fore.CYAN + "=== Sorted === " + Style.RESET_ALL)


def sort():
    def merge_sort(theSeq):
        if len(theSeq) <= 1:
            return theSeq

        # Compute the midpoint
        mid = len(theSeq) // 2
        # Split the list and perform the recursive step
        leftHalf = merge_sort(theSeq[:mid])
        rightHalf = merge_sort(theSeq[mid:])
        # Merge the two sorted sublists
        return mergeSortedLists(leftHalf, rightHalf)

    def mergeSortedLists(listA, listB):
        newList = []
        while listA and listB:
            if (int(listA[0].get_regyear()), listA[0].get_car_engineno()) <= (int(listB[0].get_regyear()), listB[0].get_car_engineno()):
                newList.append(listA.pop(0))
            else:
                newList.append(listB.pop(0))

        # Append remaining elements, if any
        newList.extend(listA)
        newList.extend(listB)
        return newList


    sorted_cars = merge_sort(cars)
    print(Fore.CYAN + "Registration Year and then Car Engine Number in ascending order using Merge Sort" + Style.RESET_ALL)
    print(" ")
    if sorted_cars:
        for car in sorted_cars:
            print(f"Car EngineNo= {car.get_car_engineno()}, Car Brand= {car.get_car_brand()}, Car Type= {car.get_car_type()}, Mileage= {car.get_mileage()}, Registered year= {car.get_regyear()}")
        print(Fore.CYAN + "=== Sorted === " + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "=== There are no records. ===" + Style.RESET_ALL)
    return sorted_cars



def SequentialSearch(theValues, customer_ID):
    for i in theValues:
        # If the customer_ID is in the _th element, return True
        if i == customer_ID:
            return True

    # If not found, return False as ID is not in the database
    return False


# myQueue object outside the function so that it can retain its values between function calls
myQueue = Queue()


def add_customer_request():
    while True:
        customer_ID = input("Enter Customer ID: ")
        while not len(customer_ID) == 4 or SequentialSearch(hardcode_customers, customer_ID) == False:
            print(Fore.RED + "Invalid Customer ID. Please try again!" + Style.RESET_ALL)
            customer_ID = input("Enter Customer ID: ")

        if customer_ID in hardcode_customers:
            customer_request = input("Enter Customer's request: ")
            while len(customer_request) <= 8:
                print(Fore.RED + "Not a valid input." + Style.RESET_ALL)
                customer_request = input("Enter Customer's request: ")
            request = CustomerRequest(customer_ID, customer_request)
            myQueue.enqueue(request)
            # Print the queue length
            print("Queue Length:", len(myQueue))
            print(Fore.GREEN + "=== Customer's request added successfully ===" + Style.RESET_ALL)
            break
        else:
            print("Customer ID not found")


def view_number_of_customer_requests():
    if len(myQueue) == 0:
        # Print the queue length
        print("Number of request(s): ", len(myQueue))
        print(Fore.BLUE + "=== There are no requests. Please press 1 to add request(s)===" + Style.RESET_ALL)
    else:
        # Print the queue length
        print("Number of request(s): ", len(myQueue))


def service_request():
    if len(myQueue) == 0:
        print(Fore.BLUE + "=== There are no requests. ===" + Style.RESET_ALL)
    else:
        print(" ")
        print("Customer Request Details:")
        print("----------------------------------------")
        # Dequeue items from the queue
        print(myQueue.dequeue())
        # Print the queue length
        print("Remaining request(s): ", len(myQueue))



# MENUS
def display_menu():
    print(" ")
    print(Style.BRIGHT + "---- Car Records ----" + Style.RESET_ALL)
    print("Select the program (0-5) to run: ")
    print("00. Test code for cars")
    print("1. Display all the cars record")
    print("2. Add a new car record")
    print("3. Sort cars by Car Brand in ascending order using Bubble sort and display")
    print("4. Sort cars by Mileage in descending order using Insertion Sort and display")
    print("5. Sort cars by Car Type in ascending order using Selection sort and display")
    print("6. Sort cars by Registration Year and then Car Engine Number in ascending order using Merge sort and display")
    print("7. Manage customer request")
    print("8. Populate data (Customers)")
    print("9. Update Cars' Records")
    print("0. Quit the program")
    print(" ")

    command = input("Enter your command (0-8): ")
    return command


def manage_customer_request_menu():
    print(" ")
    print(" ")
    print(Style.BRIGHT + "---- Customer Request Page ----" + Style.RESET_ALL)
    print("1. Manage customer request")
    print("2. View number of request")
    print("3. Service next request in Queue")
    print("0. Return to Main Menu")

    command = input("Enter your command (0-3): ")
    return command


while True:
    val = display_menu()
    if val == "0":
        print(Fore.MAGENTA + Style.BRIGHT + "=== Bye Bye ===" + Style.RESET_ALL)
        break

    elif val == "00":
        test_code_cars()

    elif val == "1":
        display_cars()

    elif val == "2":
        add_record()

    elif val == "3":
        bubble_sort(cars)

    elif val == "4":
        insertion_sort(cars)

    elif val == "5":
        selection_sort(cars)

    elif val == "6":
        cars = sort()

    elif val == "7":

        while True:
            val2 = manage_customer_request_menu()
            if val2 == "0":
                break

            elif val2 == "1":
                # Check if the 3 Customers are ADDED into the dictionary
                # print(hardcode_customers)
                if hardcode_customers == {}:
                    print(Fore.BLUE + "=== There is no Customer. ===" + Style.RESET_ALL)
                    print(Fore.BLUE + "=== Press 8 to add 3 hardcoded customers. ===" + Style.RESET_ALL)
                    break
                else:
                    add_customer_request()

            elif val2 == "2":
                view_number_of_customer_requests()

            elif val2 == "3":
                service_request()

            else:
                print(Fore.RED + "=== Invalid option. ===" + Style.RESET_ALL)

    elif val == "8":
        test_code_customerrequests()

    elif val == "9":
        update_cars_records(cars)

    else:
        print(Fore.RED + "=== Invalid option. ===" + Style.RESET_ALL)
