import flet as ft
import db


class Clients:
    def __init__(
        self,
        company_name: str = "",
        address: str = "",
        zip_code: str = "",
        city: str = "",
        tax_number: int = 0,
        email: str = "",
        phone_number: int = 0,
        receipt_required: bool = False,
    ):
        self.company_name = company_name
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.tax_number = tax_number
        self.email = email
        self.phone_number = phone_number
        self.receipt_required = receipt_required

        self.company_name_tf = ft.TextField(
            label="Company Name",
            autofocus=True,
        )

        self.address_tf = ft.TextField(
            label="Address",
        )

        self.zip_code_tf = ft.TextField(
            label="Zip Code",
        )

        self.city_tf = ft.TextField(
            label="City",
        )

        self.tax_number_tf = ft.TextField(
            label="Tax Number",
        )

        self.email_tf = ft.TextField(
            label="Email",
        )

        self.phone_number_tf = ft.TextField(
            label="Phone Number",
        )

        self.receipt_required_tf = ft.Checkbox(
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
