import sqlite3
import tkinter as tk
from tkinter import messagebox

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_name TEXT,
        min_audience INTEGER,
        max_audience INTEGER,
        manager_username TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sponsors (
        sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sponsor_name TEXT,
        budget INTEGER,
        sponsor_username TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS event_manager_username_and_password (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS event_sponsor_username_and_password (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()


# Initialize the database when the program starts
init_db()

# Tkinter window setup
window = tk.Tk()
window.title('Event Hub')
window.geometry('600x600')
window.config(bg='light gray')

# Set the window icon


welcome_to_event_hub_message = tk.Label(window, text='Welcome to Event Hub', font=('Arial', 25), bg='light gray')
welcome_to_event_hub_message.grid(row=0, column=0, columnspan=10)

who_are_you_message = tk.Label(window, text='Choose who are you\n', font=('Arial', 10), bg='light gray')
who_are_you_message.grid(row=1, column=0, columnspan=10)

login_button = None
signup_button = None
username_entryfield = None
password_entryfield = None

# Current user tracking
current_username_event_manager = None
current_username_event_sponsor = None


# Function to show the main page
def show_main_page():
    for widget in window.winfo_children():
        widget.destroy()

    welcome_to_event_hub_message = tk.Label(window, text='Welcome to Event Hub', font=('Arial', 25), bg='light gray')
    welcome_to_event_hub_message.grid(row=0, column=0, columnspan=10)

    who_are_you_message = tk.Label(window, text='Choose who are you\n', font=('Arial', 10), bg='light gray')
    who_are_you_message.grid(row=1, column=0, columnspan=10)

    eventmanager_button = tk.Button(window, text='Event Manager', command=you_are_event_manager_button_function)
    eventmanager_button.grid(row=2, column=0, columnspan=4)

    eventsponsor_button = tk.Button(window, text='Event Sponsor', command=you_are_event_sponsor_button_function)
    eventsponsor_button.grid(row=2, column=6, columnspan=4)


# Event Manager Platform Functions
def inside_the_platform_via_event_manager():
    for widget in window.winfo_children():
        widget.destroy()

    def create_post_for_event_managers_button_function_in_the_platform():
        for widget in window.winfo_children():
            widget.destroy()
        event_name_label = tk.Label(window, text='Event Name & Location: ')
        event_name_label.grid(row=0, column=0)
        event_name_entryfield = tk.Entry()
        event_name_entryfield.grid(row=0, column=1)

        event_audience_label = tk.Label(window, text='Event Audience (min and max): ')
        event_audience_label.grid(row=1, column=0)
        event_min_audience_entryfield = tk.Entry()
        event_min_audience_entryfield.grid(row=1, column=1)
        event_max_audience_entryfield = tk.Entry()
        event_max_audience_entryfield.grid(row=1, column=2)

        def save_event_to_db():
            event_name = event_name_entryfield.get()
            event_min_audience = event_min_audience_entryfield.get()
            event_max_audience = event_max_audience_entryfield.get()

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO events (event_name, min_audience, max_audience, manager_username) VALUES (?, ?, ?, ?)",
                (event_name, event_min_audience, event_max_audience, current_username_event_manager))
            conn.commit()
            conn.close()

            tk.messagebox.showinfo("Success", "Event created successfully!")

        submit_button = tk.Button(window, text='Submit', command=save_event_to_db)
        submit_button.grid(row=2, column=1)

        return_button = tk.Button(window, text='Return', command=inside_the_platform_via_event_manager)
        return_button.grid(row=2, column=0)

    def watch_sponsor_post():
        for widget in window.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT sponsor_name, budget, sponsor_username FROM sponsors")
        sponsor_posts = cursor.fetchall()
        conn.close()

        for index, post in enumerate(sponsor_posts):
            sponsor_name, budget, sponsor_username = post
            post_label = tk.Label(window, text=f"Sponsor: {sponsor_name}, Budget: {budget}, Username: {sponsor_username}")
            post_label.grid(row=index, column=0)

        return_button = tk.Button(window, text='Return', command=inside_the_platform_via_event_manager)
        return_button.grid(row=len(sponsor_posts), column=0)

    create_post_event_manager_inside_platform = tk.Button(window, text='Create Post',
                                                          command=create_post_for_event_managers_button_function_in_the_platform)
    create_post_event_manager_inside_platform.grid(row=1, column=0)

    watch_sponsor_post_button_in_the_platform_for_event_manager = tk.Button(window, text='Watch Sponsor Post', command=watch_sponsor_post)
    watch_sponsor_post_button_in_the_platform_for_event_manager.grid(row=2, column=0)

    return_button = tk.Button(window, text='Return', command=show_main_page)
    return_button.grid(row=3, column=0)


# Event Sponsor Platform Functions
def inside_the_platform_via_event_sponsor():
    for widget in window.winfo_children():
        widget.destroy()

    def create_post_event_sponsor_button_function_in_the_platform():
        for widget in window.winfo_children():
            widget.destroy()
        sponsor_name_label = tk.Label(window, text='Sponsor Name: ')
        sponsor_name_label.grid(row=0, column=0)
        sponsor_name_entryfield = tk.Entry()
        sponsor_name_entryfield.grid(row=0, column=1)

        sponsor_budget_label = tk.Label(window, text='Budget: ')
        sponsor_budget_label.grid(row=1, column=0)
        sponsor_budget_entryfield = tk.Entry()
        sponsor_budget_entryfield.grid(row=1, column=1)

        def save_sponsor_to_db():
            sponsor_name = sponsor_name_entryfield.get()
            sponsor_budget = sponsor_budget_entryfield.get()

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sponsors (sponsor_name, budget, sponsor_username) VALUES (?, ?, ?)",
                           (sponsor_name, sponsor_budget, current_username_event_sponsor))
            conn.commit()
            conn.close()

            tk.messagebox.showinfo("Success", "Sponsor post created successfully!")

        submit_button = tk.Button(window, text='Submit', command=save_sponsor_to_db)
        submit_button.grid(row=2, column=1)

        return_button = tk.Button(window, text='Return', command=inside_the_platform_via_event_sponsor)
        return_button.grid(row=2, column=0)

    def watch_event_manager_post():
        for widget in window.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT event_name, min_audience, max_audience, manager_username FROM events")
        event_manager_posts = cursor.fetchall()
        conn.close()

        for index, post in enumerate(event_manager_posts):
            event_name, min_audience, max_audience, manager_username = post
            post_label = tk.Label(window, text=f"Event: {event_name}, Min Audience: {min_audience}, Max Audience: {max_audience}, Username: {manager_username}")
            post_label.grid(row=index, column=0)

        return_button = tk.Button(window, text='Return', command=inside_the_platform_via_event_sponsor)
        return_button.grid(row=len(event_manager_posts), column=0)

    create_post_event_sponsor_inside_platform = tk.Button(window, text='Create Post',
                                                          command=create_post_event_sponsor_button_function_in_the_platform)
    create_post_event_sponsor_inside_platform.grid(row=0, column=0)

    watch_event_manager_post_button_in_the_platform_for_event_sponsor = tk.Button(window, text='Watch Event Manager Post', command=watch_event_manager_post)
    watch_event_manager_post_button_in_the_platform_for_event_sponsor.grid(row=1, column=0)

    return_button = tk.Button(window, text='Return', command=show_main_page)
    return_button.grid(row=2, column=0)


# Event Manager Authentication Functions
def you_are_event_manager_button_function():
    global login_button, signup_button
    for widget in window.winfo_children():
        widget.destroy()

    header_of_eventmanager_label = tk.Label(window, text='You are now preceding as Event Manager\n', font=('Arial', 15),
                                            bg='light gray')
    header_of_eventmanager_label.grid(row=0, column=0, columnspan=10)

    def event_manager_login_button_function():
        global login_button, signup_button, username_entryfield, password_entryfield
        for widget in window.winfo_children():
            widget.destroy()

        header_of_eventmanager_label = tk.Label(window, text='You are now preceding as Event Manager\n',
                                                font=('Arial', 15), bg='light gray')
        header_of_eventmanager_label.grid(row=0, column=0, columnspan=10)

        username_label = tk.Label(window, text='User Name:')
        username_label.grid(row=1, column=0, sticky=tk.W)
        username_entryfield = tk.Entry()
        username_entryfield.grid(row=1, column=1)

        password_label = tk.Label(window, text='Password:')
        password_label.grid(row=2, column=0, sticky=tk.W)
        password_entryfield = tk.Entry()
        password_entryfield.grid(row=2, column=1)

        def event_manager_login_button_final_function():
            global username_entryfield, password_entryfield
            global current_username_event_manager

            username = username_entryfield.get()
            password = password_entryfield.get()

            current_username_event_manager = username

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username, password FROM event_manager_username_and_password WHERE username=?",
                           (username,))
            result = cursor.fetchone()
            conn.commit()
            conn.close()

            if result is None:
                no_username_found_label = tk.Label(window, text='No user found')
                no_username_found_label.grid(row=4, column=1)
            else:
                stored_username, stored_password = result
                if username == stored_username and password == stored_password:
                    inside_the_platform_via_event_manager()
                else:
                    incorrect_password_label = tk.Label(window, text='Incorrect password')
                    incorrect_password_label.grid(row=4, column=1)

        final_login_button = tk.Button(window, text='Login', command=event_manager_login_button_final_function)
        final_login_button.grid(row=3, column=1)

        return_button = tk.Button(window, text='Return', command=you_are_event_manager_button_function)
        return_button.grid(row=3, column=0)

    def event_manager_signup_button_function():
        global login_button, signup_button, username_entryfield, password_entryfield
        for widget in window.winfo_children():
            widget.destroy()

        header_of_eventmanager_label = tk.Label(window, text='You are now preceding as Event Manager\n',
                                                font=('Arial', 15), bg='light gray')
        header_of_eventmanager_label.grid(row=0, column=0, columnspan=10)

        username_label = tk.Label(window, text='User Name:')
        username_label.grid(row=1, column=0, sticky=tk.W)
        username_entryfield = tk.Entry()
        username_entryfield.grid(row=1, column=1)

        password_label = tk.Label(window, text='Password:')
        password_label.grid(row=2, column=0, sticky=tk.W)
        password_entryfield = tk.Entry()
        password_entryfield.grid(row=2, column=1)

        def event_manager_signup_button_final_function():
            global username_entryfield, password_entryfield
            username = username_entryfield.get()
            password = password_entryfield.get()

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO event_manager_username_and_password (username, password) VALUES (?, ?)",
                           (username, password))
            conn.commit()
            conn.close()

            tk.messagebox.showinfo("Success", "Signup successful!")
            event_manager_login_button_function()

        final_signup_button = tk.Button(window, text='Signup', command=event_manager_signup_button_final_function)
        final_signup_button.grid(row=3, column=1)

        return_button = tk.Button(window, text='Return', command=you_are_event_manager_button_function)
        return_button.grid(row=3, column=0)

    login_button = tk.Button(window, text='Login', command=event_manager_login_button_function)
    login_button.grid(row=2, column=0, columnspan=4)

    signup_button = tk.Button(window, text='Signup', command=event_manager_signup_button_function)
    signup_button.grid(row=2, column=6, columnspan=4)


# Event Sponsor Authentication Functions
def you_are_event_sponsor_button_function():
    global login_button, signup_button
    for widget in window.winfo_children():
        widget.destroy()

    header_of_eventsponsor_label = tk.Label(window, text='You are now preceding as Event Sponsor\n', font=('Arial', 15),
                                            bg='light gray')
    header_of_eventsponsor_label.grid(row=0, column=0, columnspan=10)

    def event_sponsor_login_button_function():
        global login_button, signup_button, username_entryfield, password_entryfield
        for widget in window.winfo_children():
            widget.destroy()

        header_of_eventsponsor_label = tk.Label(window, text='You are now preceding as Event Sponsor\n',
                                                font=('Arial', 15), bg='light gray')
        header_of_eventsponsor_label.grid(row=0, column=0, columnspan=10)

        username_label = tk.Label(window, text='User Name:')
        username_label.grid(row=1, column=0, sticky=tk.W)
        username_entryfield = tk.Entry()
        username_entryfield.grid(row=1, column=1)

        password_label = tk.Label(window, text='Password:')
        password_label.grid(row=2, column=0, sticky=tk.W)
        password_entryfield = tk.Entry()
        password_entryfield.grid(row=2, column=1)

        def event_sponsor_login_button_final_function():
            global username_entryfield, password_entryfield
            global current_username_event_sponsor

            username = username_entryfield.get()
            password = password_entryfield.get()

            current_username_event_sponsor = username

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username, password FROM event_sponsor_username_and_password WHERE username=?",
                           (username,))
            result = cursor.fetchone()
            conn.commit()
            conn.close()

            if result is None:
                no_username_found_label = tk.Label(window, text='No user found')
                no_username_found_label.grid(row=4, column=1)
            else:
                stored_username, stored_password = result
                if username == stored_username and password == stored_password:
                    inside_the_platform_via_event_sponsor()
                else:
                    incorrect_password_label = tk.Label(window, text='Incorrect password')
                    incorrect_password_label.grid(row=4, column=1)

        final_login_button = tk.Button(window, text='Login', command=event_sponsor_login_button_final_function)
        final_login_button.grid(row=3, column=1)

        return_button = tk.Button(window, text='Return', command=you_are_event_sponsor_button_function)
        return_button.grid(row=3, column=0)

    def event_sponsor_signup_button_function():
        global login_button, signup_button, username_entryfield, password_entryfield
        for widget in window.winfo_children():
            widget.destroy()

        header_of_eventsponsor_label = tk.Label(window, text='You are now preceding as Event Sponsor\n',
                                                font=('Arial', 15), bg='light gray')
        header_of_eventsponsor_label.grid(row=0, column=0, columnspan=10)

        username_label = tk.Label(window, text='User Name:')
        username_label.grid(row=1, column=0, sticky=tk.W)
        username_entryfield = tk.Entry()
        username_entryfield.grid(row=1, column=1)

        password_label = tk.Label(window, text='Password:')
        password_label.grid(row=2, column=0, sticky=tk.W)
        password_entryfield = tk.Entry()
        password_entryfield.grid(row=2, column=1)

        def event_sponsor_signup_button_final_function():
            global username_entryfield, password_entryfield
            username = username_entryfield.get()
            password = password_entryfield.get()

            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO event_sponsor_username_and_password (username, password) VALUES (?, ?)",
                           (username, password))
            conn.commit()
            conn.close()

            tk.messagebox.showinfo("Success", "Signup successful!")
            event_sponsor_login_button_function()

        final_signup_button = tk.Button(window, text='Signup', command=event_sponsor_signup_button_final_function)
        final_signup_button.grid(row=3, column=1)

        return_button = tk.Button(window, text='Return', command=you_are_event_sponsor_button_function)
        return_button.grid(row=3, column=0)

    login_button = tk.Button(window, text='Login', command=event_sponsor_login_button_function)
    login_button.grid(row=2, column=0, columnspan=4)

    signup_button = tk.Button(window, text='Signup', command=event_sponsor_signup_button_function)
    signup_button.grid(row=2, column=6, columnspan=4)


# Initialize the main page when the program starts
show_main_page()

# Run the Tkinter event loop
window.mainloop()
