"""
Exercise 13.3m Bank Account Shell UI

Instantiates and runs a Shell-based Bank Account Management Application
"""

if __name__ == "__main__":
    from Data import AccountSystem
    from UI.ShellUI import BankAccountApplication

    ui = BankAccountApplication.BankAccountApplication
    account_system = AccountSystem.AccountSystem

    app = ui(filename="accounts.pkl", storage_class=account_system)
    app.main_menu()
