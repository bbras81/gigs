import flet as ft
import db
from clients.clients_data import Clients


class Gigs:
    def __init__(self):
        self.gig_date = ft.TextField("Gig date", autofocus=True)
        self.gig_local = ft.Dropdown("Please select a store")
        self.gig_hour = ft.TextField("Gig start")
        self.gig_cachet = ft.TextField("Cahet")

        self.gig_local.options = self.get_house_dropdown()

    db.db_execute(
        """CREATE TABLE IF NOT EXISTS gigs (
                gig_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                gig_date DATE,
                gig_start TEXT,
                gig_cachet FLOAT,
                gig_recipt INTEGER,
                id_client INTEGER,
                FOREIGN KEY (id_client) REFERENCES clients(id_client)
        )"""
    )
    @staticmethod
    def get_house_dropdown():
        client_data = Clients().get_store_all()
        options = []
        for client in client_data:
            options.append(ft.dropdown.Option(client[1], client[0]))
        return options
