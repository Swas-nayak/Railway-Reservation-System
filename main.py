import database

def main():
    print("Welcome to the Railway Reservation System")
    print("1. Search Train")
    print("2. Book Ticket")
    
    # Simple test to show database connection
    database.connect_to_db()

if __name__ == "__main__":
    main()