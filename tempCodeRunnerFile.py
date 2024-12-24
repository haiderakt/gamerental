def show_rentals(self):
        try:
            window = tk.Toplevel(self.root)
            window.title("Rental Records")
            window.geometry("1200x500")

            frame = ttk.Frame(window)
            frame.pack(fill='both', expand=True)

            y_scroll = ttk.Scrollbar(frame, orient='vertical')
            x_scroll = ttk.Scrollbar(frame, orient='horizontal')
            
            tree = ttk.Treeview(frame, yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
            tree['columns'] = ('ID', 'Customer', 'Game', 'Staff', 'Rental Date', 'Return Date', 'Total Cost')

            tree.column('#0', width=0, stretch=tk.NO)
            tree.column('ID', width=70, anchor='center')
            tree.column('Customer', width=200)
            tree.column('Game', width=200)
            tree.column('Staff', width=200)
            tree.column('Rental Date', width=150, anchor='center')
            tree.column('Return Date', width=150, anchor='center')
            tree.column('Total Cost', width=100, anchor='e')

            for col in tree['columns']:
                tree.heading(col, text=col)

            query = """
            SELECT 
                r.id,
                c.name as customer_name,
                g.title as game_title,
                s.name as staff_name,
                DATE_FORMAT(r.rental_date, '%Y-%m-%d') as rental_date,
                IFNULL(DATE_FORMAT(r.return_date, '%Y-%m-%d'), 'Not Returned') as return_date,
                CONCAT('$', FORMAT(r.total_cost, 2)) as total_cost
            FROM rentals r
            LEFT JOIN customers c ON r.customer_id = c.customer_id
            LEFT JOIN games g ON r.game_id = g.game_id
            LEFT JOIN staff s ON r.staff_id = s.id
            ORDER BY r.rental_date DESC
            """

            self.system.cursor.execute(query)
            for row in self.system.cursor.fetchall():
                tree.insert('', 'end', values=row)

            y_scroll.config(command=tree.yview)
            x_scroll.config(command=tree.xview)
            
            y_scroll.pack(side='right', fill='y')
            x_scroll.pack(side='bottom', fill='x')
            tree.pack(fill='both', expand=True)

        except Error as err:
            logger.error(f"Database error in show_rentals: {err}")
            messagebox.showerror("Error", "Failed to load rental data")

    def show_staff(self):
        window = tk.Toplevel(self.root)
        window.title("Staff List")
        window.geometry("800x400")
        
        tree = ttk.Treeview(window)
        tree['columns'] = ('ID', 'Name', 'Position', 'Contact')
        
        for col in tree['columns']:
            tree.column(col, width=150)
            tree.heading(col, text=col)
        
        tree.column('#0', width=0, stretch=tk.NO)
        self.system.cursor.execute("SELECT * FROM staff")
        for row in self.system.cursor.fetchall():
            tree.insert('', 'end', values=row)
            
        tree.pack(expand=True, fill='both')