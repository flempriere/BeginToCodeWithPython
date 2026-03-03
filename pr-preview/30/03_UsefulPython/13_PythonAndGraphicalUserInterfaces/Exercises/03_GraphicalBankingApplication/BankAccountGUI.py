"""
Exercise 13.3 Bank Account GUI

Loads and runs a graphical-based Bank Account System. Only
runs if executed as the main program
"""

if __name__ == "__main__":
    from Data import AccountSystem
    from UI.GUI import BankAccountApplication

    # load the UI implementation
    ui = BankAccountApplication.BankAccountApplication

    # load the data management implementation
    account_system = AccountSystem.AccountSystem

    app = ui(filename="accounts.pkl", storage_class=account_system)
    app.main_menu()
