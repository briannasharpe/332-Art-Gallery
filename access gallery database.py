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
    print("---------- Artist ----------")
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
        * sort a report according to art style
        * uses fetch_all
        * triggered by switch 3 
-------------------------------------------------- """   
def sort_by_art_style(art_style):
    print("\nArt style report: " + art_style)
    
    print("\nArtists with " + art_style + ": ")
    cur.execute("SELECT Name FROM Artist WHERE Style_of_art LIKE '%" + art_style + "%'")
    fetch_all()
    
    print("\nArt work with " + art_style + ": ")
    cur.execute("SELECT Title FROM Art_work WHERE Type_of_art LIKE '%" + art_style + "%'")
    fetch_all()
    
    print("\nCustomers who prefer " + art_style + ": ")
    cur.execute("SELECT Customer_number FROM Customer WHERE Art_preferences LIKE '%" + art_style + "%'")
    fetch_all()
# ---------- sort_by_art_style ----------
    
""" --------------------------------------------------
    [sort_by_same_art_preference]
        * sort a report according to art style
        * uses fetch_all
        * triggered by switch 3 
-------------------------------------------------- """   
def sort_by_same_art_preference():
    print("\nArt preference report")

    # get data from art shows
    cur.execute("SELECT Location FROM Art_shows")
    num_of_art_shows = cur.fetchall()
    
    # get data from customers
    cur.execute("SELECT * FROM Customer")
    num_of_customers = cur.fetchall()

    # for each art show, list customers with the same art preferences
    for art_show in range(len(num_of_art_shows)):
        # print different art shows
        print("\nCustomers who would be interested in attending " + ''.join(num_of_art_shows[art_show]) + ": ")
        
        # gather the art style of the art shows
        cur.execute("SELECT Type_of_art FROM Art_work WHERE Location LIKE '%" + ''.join(num_of_art_shows[art_show]) + "%'")
        art_style = cur.fetchall()
        print("art style:", art_style)
        print("no. of art shows:", art_show)
        
        https://animalcrossing.fandom.com/wiki/Forgery
        
        print(''.join(art_style[art_show]))
        # for every art style, list the customers with similar art preferences
       # for customers in range(len(num_of_customers)):
            #print("no.of customers:", customers)
        cur.execute("SELECT Customer_number, Phone FROM Customer WHERE Art_preferences LIKE '%" + ''.join(art_style[art_show]) + "%'")
        interested_customers = cur.fetchall()
        print("interested customers:", interested_customers)
   # cur.execute("SELECT Art_preferences FROM Customer")
#    fetch_all()
    '''
    cur.execute("SELECT * FROM Artist WHERE Style_of_art LIKE '%" + art_style + "%'")
    data = cur.fetchall()
    
    
    cur.execute("SELECT Location FROM Art_shows WHERE Artist LIKE '%" + artist + "%'")
    fetch_all()'''
# ---------- sort_by_same_art_preference ----------
    
'''
def switch(option):
    switch = {
        1: "Print records from the database",
        2: "Access any record based on attribute values",
        3: "Sort a report according to art style",
        4: "Produce a report showing customers with the same art preference of any given art show"
    }
    print switch.get(option, "Invalid input")
'''
def main():
    #print_records_in_database()
    #access_record_by_attribute_value("Pointillism")
    #sort_by_art_style("Pointillism")
    sort_by_same_art_preference()
    
if __name__ == '__main__':
    main()

# close the database
conn.close()