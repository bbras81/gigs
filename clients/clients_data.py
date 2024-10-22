import flet as ft
import db


class Clients:
    def __init__(self):
        self.id_client = 0
        self.company_name = ft.TextField(label="Company Name", autofocus=True)
        self.address = ft.TextField(label="Address")
        self.zip_code = ft.TextField(label="Zip Code")
        self.city = ft.TextField(label="City")
        self.tax_number = ft.TextField(label="Tax Number")
        self.email = ft.TextField(label="Email")
        self.phone_number = ft.TextField(label="Phone Number")
        self.receipt_required = ft.Checkbox(label="Receipt required?")
        self.store_name = ft.TextField(label="Store Name")

        db.db_execute(
            """CREATE TABLE IF NOT EXISTS clients (
                id_client INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                company_name TEXT NOT NULL,
                address TEXT,
                zip_code TEXT,
                city TEXT,
                tax_number INTEGER,
                email TEXT,
                phone_number INTEGER,
                receipt_required INTEGER
            )"""
        )
        db.db_execute(
            """CREATE TABLE IF NOT EXISTS commercial_establishments (
                id_establishment INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT UNIQUE NOT NULL,
                id_client INTEGER NOT NULL,
                FOREIGN KEY (id_client) REFERENCES clients (id_client)
            )"""
        )

    def create_client(self, client_data: dict) -> None:
        """Insert a new client into the database."""
        db.db_execute(
            """INSERT INTO clients (
                company_name, address, zip_code, city, tax_number, email, phone_number, receipt_required
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                client_data["company_name"],
                client_data["company_address"],
                client_data["company_zip"],
                client_data["city"],
                client_data["tax_number"],
                client_data["email"],
                client_data["phone_number"],
                client_data["receipt_required"],
            ),
        )

    def add_store_db(self, client_data: dict) -> None:
        """Insert a new store into the database."""
        db.db_execute(
            """INSERT INTO commercial_establishments (name, id_client)
            VALUES (?, ?)""",
            (client_data["store_name"], client_data["id_client"]),
        )

    def client_info_all(self):
        return db.db_execute("SELECT * FROM clients", fetch_all=True)

    def client_info_by_id(self, client_id: int):
        return db.db_execute(
            "SELECT * FROM clients WHERE id_client = ?", (client_id,), fetch_one=True
        )
    
    def get_store_by_id(self, client_id: int):
        return db.db_execute(
            "SELECT * FROM commercial_establishments WHERE id_client = ?", (client_id,), fetch_all=True
        )

    def update_client(self, client_data: dict) -> None:
        """Update an existing client in the database."""
        db.db_execute(
            """UPDATE clients
            SET company_name = ?, address = ?, zip_code = ?, city = ?, tax_number = ?, email = ?, phone_number = ?, receipt_required = ?
            WHERE id_client = ?""",
            (
                client_data["company_name"],
                client_data["company_address"],
                client_data["company_zip"],
                client_data["city"],
                client_data["tax_number"],
                client_data["email"],
                client_data["phone_number"],
                client_data["receipt_required"],
                client_data["id_client"],
            ),
        )
