from controller.Main_controller import Main_controller
from config.database import Database
from view.Auth_view import Auth_view

def main():
    db = Database()
    db.init_db()
    
    app = Main_controller()
    app.ejecutar()

if __name__ == "__main__":
    main()