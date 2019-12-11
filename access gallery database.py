import sqlite3

# create a database connection
conn = sqlite3.connect('art_gallery.db', isolation_level=None) 
cur = conn.cursor()

# print all artists
def select_all_artists(conn):
    cur.execute("SELECT * FROM Artist")
    rows = cur.fetchall()
 
    print("---------- Artists ----------")
    for row in rows:
        print(row)
# ---------- select_all_artists ----------
        
# print all art work
def select_all_art_work(conn):
    cur.execute("SELECT * FROM Art_work")
    rows = cur.fetchall()
 
    print("---------- Art_work ----------")
    for row in rows:
        print(row)
# ---------- select_all_art_work ----------
        
# print all customers
def select_all_customer(conn):
    cur.execute("SELECT * FROM Customer")
    rows = cur.fetchall()
 
    print("---------- Customer ----------")
    for row in rows:
        print(row)
# ---------- select_all_customer ----------
       
# print all art shows
def select_all_art_shows(conn):
    cur.execute("SELECT * FROM Art_shows")
    rows = cur.fetchall()
 
    print("---------- Art_shows ----------")
    for row in rows:
        print(row)
# ---------- select_all_art_shows ----------
        
""" --------------------------------------------------
    [print_records_in_database]
        * print records from the database
        * uses select_all_artists,
               select_all_art_work,
               select_all_customer,
               select_all_art_shows
        * triggered by switch 1    
-------------------------------------------------- """        
def print_records_in_database():
    with conn:
        print("\nPrinting records from the art gallery database:")
        select_all_artists(conn)
        select_all_art_work(conn)
        select_all_customer(conn)
        select_all_art_shows(conn)
# ---------- print_records_in_database ----------

# check if a variable is empty or not
def is_empty(check):
    if check:
        return False
    else:
        return True
# ---------- is_empty ----------

# fetch all for sql data retrieval and printing
def fetch_all():
    data = cur.fetchall()
    if not is_empty(data):
        print(data)
# ---------- fetch_all ----------

""" --------------------------------------------------
    [access_record_by_attribute]
        * access any record based on attribute values
        * uses fetch_all
        * triggered by switch 2   
-------------------------------------------------- """     
def access_record_by_attribute_value(value):
    print("\nData with '" + value + "':")
    
    # search through artist
    print("\n---------- Artist ----------")
    cur.execute("SELECT * FROM Artist WHERE Name LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Artist WHERE Phone LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Artist WHERE Address LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Artist WHERE Birth_place LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Artist WHERE Age LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Artist WHERE Style_of_art LIKE '%" + value + "%'")
    fetch_all()
    
    # search through art work
    print("\n---------- Art work ----------")
    cur.execute("SELECT * FROM Art_work WHERE Artist LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_work WHERE Title LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_work WHERE Type_of_art LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_work WHERE Date_of_creation LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_work WHERE Price LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_work WHERE Location LIKE '%" + value + "%'")
    fetch_all()
    
    # search through customer
    print("\n---------- Customer ----------")
    cur.execute("SELECT * FROM Customer WHERE Customer_number LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Customer WHERE Phone LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Customer WHERE Art_preferences LIKE '%" + value + "%'")
    fetch_all()
    
    # search through art shows
    print("\n---------- Art shows ----------")
    cur.execute("SELECT * FROM Art_shows WHERE Date_and_time LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_shows WHERE Location LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_shows WHERE Contact_phone LIKE '%" + value + "%'")
    fetch_all()
    cur.execute("SELECT * FROM Art_shows WHERE Artist LIKE '%" + value + "%'")
    fetch_all()
# ---------- access_record_by_attribute ----------

""" --------------------------------------------------
    [sort_by_art_style]
        * a report according to art style
        * uses fetch_all
        * triggered by switch 3 
-------------------------------------------------- """   
def sort_by_art_style():    
    print("\nArt preference report")

    # get data from artists
    cur.execute("SELECT * FROM Artist")
    all_artists = cur.fetchall()
    
    # get data from art work
    cur.execute("SELECT * FROM Art_work")
    all_art_work = cur.fetchall()
    
    # get data from customers
    cur.execute("SELECT * FROM Customer")
    all_customers = cur.fetchall()
    
    # for each art style from artists
    for art_style in range(len(all_artists)):
        print("\n---------- " + ''.join(all_artists[art_style][5]) + " ----------")
        # artists
        print("Artists: ")
        count1 = 0
        for artists in range(len(all_artists)):
            if ''.join(all_artists[art_style][5]) == ''.join(all_artists[artists][5]):
                count1 += 1
                print("     " + str(count1) + ". " + ''.join(all_artists[artists][0]))
        
        # for each art style from art work
        count2 = 0
        for art_work in range(len(all_art_work)):
            # art work
            print("Art work: ")
            for art_work in range(len(all_artists)):
                if ''.join(all_artists[art_style][5]) == ''.join(all_artists[art_work][5]):
                    count2 += 1
                    print("     " + str(count2) + ". " + ''.join(all_art_work[art_work][1]) + " by " + ''.join(all_art_work[art_work][0]))
            break
        
        # for each art style from customer
        count3 = 0
        for customers in range(len(all_customers)):
            # art work
            print("Customers: ")
            for customers in range(len(all_artists)):
                if ''.join(all_artists[art_style][5]) == ''.join(all_customers[customers][2]):
                    count3 += 1
                    print("     " + str(count3) + ". " + str(all_customers[customers][0]))                 
            break
# ---------- sort_by_art_style ----------
    
""" --------------------------------------------------
    [sort_by_same_art_preference]
        * a report showing customers whose art preference is the same as an art show
        * provides customer name and phone
        * triggered by switch 4
-------------------------------------------------- """   
def sort_by_same_art_preference():
    print("\nArt preference report")

    # get data from art shows
    cur.execute("SELECT * FROM Art_shows")
    all_art_shows = cur.fetchall()
    
    # get data from art work
    cur.execute("SELECT * FROM Art_work")
    all_art_work = cur.fetchall()
    
    # get data from customers
    cur.execute("SELECT * FROM Customer")
    all_customers = cur.fetchall()

    # for each art show
    for art_show in range(len(all_art_shows)):
        # print different art shows
        print("\nCustomers who would be interested in attending " + ''.join(all_art_shows[art_show][1]) +  " (" + ''.join(all_art_shows[art_show][0]) +"): ")

        # find artshow location in art work
        for location in range(len(all_art_work)):
            # pick out an art work location that is the same as the art show
            if ''.join(all_art_shows[art_show][1]) == ''.join(all_art_work[location][5]):
                # find customer
                for customer in range(len(all_customers)):
                    # pick out art preferences similar to art style
                    if ''.join(all_customers[customer][2]) == ''.join(all_art_work[location][2]):
                        print("Customer number: " + str(all_customers[customer][0]) + ", Phone: " + str(all_customers[customer][1]))
    
# ---------- sort_by_same_art_preference ----------

def main():
    print("1: Print records from the database\n 2: Access any record based on attribute values\n 3: Sort a report according to art style\n 4: Produce a report showing customers with the same art preference of any given art show")
    option = input('Please enter a number from 1-4: \n')
    
    if option == '1':
        print_records_in_database()
    elif option == '2':
        attribute_value = input('Enter a value to search for records: \n')
        access_record_by_attribute_value(attribute_value)
    elif option == '3': 
        sort_by_art_style()
    elif option == '4':
        sort_by_same_art_preference()
    else:
        print('Invalid input')
    
if __name__ == '__main__':
    main()

# close the database
conn.close()
