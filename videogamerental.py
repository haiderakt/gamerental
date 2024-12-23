from mysql.connector import connect, Error
from tkinter import messagebox
import logging
import tkinter as tk
from tkinter import ttk

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class GameRentalSystem:
    def __init__(self, root):  # Modified to accept root
        logger.debug("Initializing GameRentalSystem...")
        self.root = root
        try:
            self.db = connect(
                host="localhost",
                user="root",
                database="gamrentaldb",
                password="haiderr",
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.db.cursor()
            logger.debug("Database connection successful")
        except Error as e:
            logger.error(f"Error connecting to database: {e}")
            messagebox.showerror("Connection Error", "Failed to connect to the database.")
            self.root.quit()

    def close(self):
        if self.db.is_connected():
            self.cursor.close()
            self.db.close()
            logger.info("MySQL connection closed.")

    def add_customer(self, name, email, phone):
        try:
            query = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, email, phone))
            self.db.commit()
            logger.info(f"Customer {name} added successfully")
            return True
        except Error as err:
            logger.error(f"Error adding customer: {err}")
            return False

    def add_game(self, title, genre, price_per_day, copies):
        try:
            query = "INSERT INTO games (title, genre, price_per_day, available_copies) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (title, genre, price_per_day, copies))
            self.db.commit()
            return True
        except Error as err:
            logger.error(f"Error adding game: {err}")
            return False

    def add_rental(self, customer_id, game_id, staff_id):
        try:
            query = """INSERT INTO rentals 
                      (customer_id, game_id, staff_id, rental_date) 
                      VALUES (%s, %s, %s, CURDATE())"""
            self.cursor.execute(query, (customer_id, game_id, staff_id))
            self.db.commit()
            return True
        except Error as err:
            logger.error(f"Error adding rental: {err}")
            return False

    def add_staff(self, name, position, email):
        try:
            query = "INSERT INTO staff (name, position, email) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, position, email))
            self.db.commit()
            logger.info(f"Staff member {name} added successfully")
            return True
        except Error as err:
            logger.error(f"Error adding staff member: {err}")
        return False

class ModernGameRentalGUI:
    def __init__(self):
        # Create single root window
        self.root = tk.Tk()
        self.root.title("Game Rental System")
        self.root.geometry("1000x700")
        
        # Initialize system with root
        self.system = GameRentalSystem(self.root)
        
        # Basic colors
        self.colors = {
            'bg': '#f0f0f0',
            'fg': '#333333',
            'button': '#4a90e2'
        }
        
        # Configure basic styles
        self.setup_styles()
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_label = ttk.Label(
            self.main_container, 
            text="Game Rental System",
            font=('Helvetica', 24, 'bold')
        )
        header_label.pack(pady=(0, 20))
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(fill='both', expand=True)
        
        # Initialize tabs
        self.setup_tabs()

    def setup_styles(self):
        # Simplified styling
        style = ttk.Style()
        style.configure('TFrame', background=self.colors['bg'])
        style.configure('TLabel', background=self.colors['bg'])
        style.configure('TButton', padding=5)
        
    def create_modern_frame(self, parent, title):
        frame = ttk.LabelFrame(
            parent,
            text=title,
            style='Modern.TLabelframe',
            padding="20 10 20 10"
        )
        return frame

    def create_modern_button(self, parent, text, command):
        btn = ttk.Button(
            parent,
            text=text,
            command=command,
            style='Action.TButton'
        )
        return btn

    def create_modern_entry(self, parent):
        entry = ttk.Entry(
            parent,
            style='Modern.TEntry'
        )
        return entry

    def setup_tabs(self):
        self.customers_tab = ttk.Frame(self.notebook)
        self.games_tab = ttk.Frame(self.notebook)
        self.rentals_tab = ttk.Frame(self.notebook)
        self.staff_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.customers_tab, text='Customers')
        self.notebook.add(self.games_tab, text='Games')
        self.notebook.add(self.rentals_tab, text='Rentals')
        self.notebook.add(self.staff_tab, text='Staff')

        self.setup_customers_tab()
        self.setup_games_tab()
        self.setup_rentals_tab()
        self.setup_staff_tab()

    def setup_customers_tab(self):
        customers_frame = self.create_modern_frame(self.customers_tab, "Customer Management")
        customers_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Input fields with modern styling
        input_frame = ttk.Frame(customers_frame)
        input_frame.pack(fill='x', pady=10)

        # Name field
        name_frame = ttk.Frame(input_frame)
        name_frame.pack(fill='x', pady=5)
        ttk.Label(name_frame, text="Name").pack(side='left')
        self.customer_name = self.create_modern_entry(name_frame)
        self.customer_name.pack(side='right', expand=True, fill='x', padx=10)

        # Email field
        email_frame = ttk.Frame(input_frame)
        email_frame.pack(fill='x', pady=5)
        ttk.Label(email_frame, text="Email").pack(side='left')
        self.customer_email = self.create_modern_entry(email_frame)
        self.customer_email.pack(side='right', expand=True, fill='x', padx=10)

        # Phone field
        phone_frame = ttk.Frame(input_frame)
        phone_frame.pack(fill='x', pady=5)
        ttk.Label(phone_frame, text="Phone").pack(side='left')
        self.customer_phone = self.create_modern_entry(phone_frame)
        self.customer_phone.pack(side='right', expand=True, fill='x', padx=10)

        # Add button with hover effect
        add_btn = self.create_modern_button(
            customers_frame,
            "Add Customer",
            self.add_customer
        )
        add_btn.pack(pady=10)

    def setup_games_tab(self):
        games_frame = self.create_modern_frame(self.games_tab, "Game Management")
        games_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Input fields with modern styling
        input_frame = ttk.Frame(games_frame)
        input_frame.pack(fill='x', pady=10)

        # Title field
        title_frame = ttk.Frame(input_frame)
        title_frame.pack(fill='x', pady=5)
        ttk.Label(title_frame, text="Title").pack(side='left')
        self.game_title = self.create_modern_entry(title_frame)
        self.game_title.pack(side='right', expand=True, fill='x', padx=10)

        # Genre field
        genre_frame = ttk.Frame(input_frame)
        genre_frame.pack(fill='x', pady=5)
        ttk.Label(genre_frame, text="Genre").pack(side='left')
        self.game_genre = self.create_modern_entry(genre_frame)
        self.game_genre.pack(side='right', expand=True, fill='x', padx=10)

        # Price per day field
        price_frame = ttk.Frame(input_frame)
        price_frame.pack(fill='x', pady=5)
        ttk.Label(price_frame, text="Price per day").pack(side='left')
        self.game_price = self.create_modern_entry(price_frame)
        self.game_price.pack(side='right', expand=True, fill='x', padx=10)

        # Available copies field
        copies_frame = ttk.Frame(input_frame)
        copies_frame.pack(fill='x', pady=5)
        ttk.Label(copies_frame, text="Available copies").pack(side='left')
        self.game_copies = self.create_modern_entry(copies_frame)
        self.game_copies.pack(side='right', expand=True, fill='x', padx=10)

        # Add button with hover effect
        add_btn = self.create_modern_button(
            games_frame,
            "Add Game",
            self.add_game
        )
        add_btn.pack(pady=10)

    def setup_rentals_tab(self):
        rentals_frame = self.create_modern_frame(self.rentals_tab, "Rental Management")
        rentals_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Input fields with modern styling
        input_frame = ttk.Frame(rentals_frame)
        input_frame.pack(fill='x', pady=10)

        # Customer selection
        customer_frame = ttk.Frame(input_frame)
        customer_frame.pack(fill='x', pady=5)
        ttk.Label(customer_frame, text="Customer").pack(side='left')
        self.customer_select = ttk.Combobox(customer_frame)
        self.customer_select.pack(side='right', expand=True, fill='x', padx=10)

        # Game selection
        game_frame = ttk.Frame(input_frame)
        game_frame.pack(fill='x', pady=5)
        ttk.Label(game_frame, text="Game").pack(side='left')
        self.game_select = ttk.Combobox(game_frame)
        self.game_select.pack(side='right', expand=True, fill='x', padx=10)

        # Staff selection
        staff_frame = ttk.Frame(input_frame)
        staff_frame.pack(fill='x', pady=5)
        ttk.Label(staff_frame, text="Staff").pack(side='left')
        self.staff_select = ttk.Combobox(staff_frame)
        self.staff_select.pack(side='right', expand=True, fill='x', padx=10)

        # Add button with hover effect
        add_btn = self.create_modern_button(
            rentals_frame,
            "Create Rental",
            self.add_rental
        )
        add_btn.pack(pady=10)

    def setup_staff_tab(self):
        staff_frame = self.create_modern_frame(self.staff_tab, "Staff Management")
        staff_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Input fields with modern styling
        input_frame = ttk.Frame(staff_frame)
        input_frame.pack(fill='x', pady=10)

        # Name field
        name_frame = ttk.Frame(input_frame)
        name_frame.pack(fill='x', pady=5)
        ttk.Label(name_frame, text="Name").pack(side='left')
        self.staff_name = self.create_modern_entry(name_frame)
        self.staff_name.pack(side='right', expand=True, fill='x', padx=10)

        # Email field
        email_frame = ttk.Frame(input_frame)
        email_frame.pack(fill='x', pady=5)
        ttk.Label(email_frame, text="Email").pack(side='left')
        self.staff_email = self.create_modern_entry(email_frame)
        self.staff_email.pack(side='right', expand=True, fill='x', padx=10)

        # Role field
        role_frame = ttk.Frame(input_frame)
        role_frame.pack(fill='x', pady=5)
        ttk.Label(role_frame, text="Role").pack(side='left')
        self.staff_role = ttk.Combobox(role_frame, values=["Manager", "Staff", "Admin"])
        self.staff_role.pack(side='right', expand=True, fill='x', padx=10)

        # Add button with hover effect
        add_btn = self.create_modern_button(
            staff_frame,
            "Add Staff",
            self.add_staff
        )
        add_btn.pack(pady=10)

    def add_customer(self):
        name = self.customer_name.get()
        email = self.customer_email.get()
        phone = self.customer_phone.get()
        
        if self.system.add_customer(name, email, phone):
            messagebox.showinfo("Success", "Customer added successfully!")
            self.customer_name.delete(0, tk.END)
            self.customer_email.delete(0, tk.END)
            self.customer_phone.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to add customer")

    def add_game(self):
        title = self.game_title.get()
        genre = self.game_genre.get()
        price = self.game_price.get()
        copies = self.game_copies.get()
        
        if self.system.add_game(title, genre, price, copies):
            messagebox.showinfo("Success", "Game added successfully!")
            self.game_title.delete(0, tk.END)
            self.game_genre.delete(0, tk.END)
            self.game_price.delete(0, tk.END)
            self.game_copies.delete(0, tk.END)

    def add_staff(self):
        name = self.staff_name.get()
        email = self.staff_email.get()
        role = self.staff_role.get()
        
        if self.system.add_staff(name, email, role):
            messagebox.showinfo("Success", "Staff added successfully!")
            self.staff_name.delete(0, tk.END)
            self.staff_email.delete(0, tk.END)
            self.staff_role.set('')

    def add_rental(self):
        customer_id = self.customer_select.get()
        game_id = self.game_select.get()
        staff_id = self.staff_select.get()
        
        if self.system.add_rental(customer_id, game_id, staff_id):
            messagebox.showinfo("Success", "Rental created successfully!")
            self.customer_select.set('')
            self.game_select.set('')
            self.staff_select.set('')

def main():
    app = ModernGameRentalGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main()