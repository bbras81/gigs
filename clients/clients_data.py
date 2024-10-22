import flet as ft
import db


class Clients:
    def __init__(self):
        self.company_name = ft.TextField(
            label="Company Name",
            autofocus=True,
        )
        self.address = ft.TextField(
            label="Address",
        )

        self.zip_code = ft.TextField(
            label="Zip Code",
        )

        self.city = ft.TextField(
            label="City",
        )

        self.tax_number = ft.TextField(
            label="Tax Number",
        )

        self.email = ft.TextField(
            label="Email",
        )

        self.phone_number = ft.TextField(
            label="Phone Number",
        )

        self.receipt_required = ft.Checkbox(
            label="Receipt required?",
        )
        self.house_name = ft.TextField(
            label="House Name",
        )

        # Cria a tabela de clientes se não existir
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
            )
            """,
            [],
        )
        # Cria a tabela de estabelecimentos comerciais, associada ao cliente
        db.db_execute(
            """CREATE TABLE IF NOT EXISTS commercial_establishments (
                id_establishment INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT UNIQUE NOT NULL,
                id_client INTEGER NOT NULL,
                FOREIGN KEY (id_client) REFERENCES clients (id_client)
            )
            """,
            [],
        )

    def create_client(self, client_data: dict) -> None:
        """Insert a new client into the database."""
        db.db_execute(
            """INSERT INTO clients (
                company_name, address, zip_code, city, tax_number, email, phone_number, receipt_required
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?
            )""",
            params=(
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

    def client_info_all(self):
        client_information = db.db_execute("SELECT * FROM clients", fetch_all=True)
        return client_information

    def client_info_by_id(self, client_id: int):
        client_information = db.db_execute(
            "SELECT * FROM clients WHERE id_client = ?", (client_id,), fetch_one=True
        )
        return client_information