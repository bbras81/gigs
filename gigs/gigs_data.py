import flet as ft
from clients.clients_data import Clients
import db


class Gigs:
    def __init__(self):
        self.gig_date = ft.TextField(label="Gig date", autofocus=True)
        self.gig_hour = ft.TextField(label="Gig start")
        self.gig_cachet = ft.TextField(label="Cachet", suffix_text="€")
        self.gig_local = ft.Dropdown(hint_text="Please select a store")

        self.gig_local.options = self.get_house_dropdown()

    @staticmethod
    def get_house_dropdown():
        client_data = Clients().get_store_all()
        options = []
        for client in client_data:
            options.append(ft.dropdown.Option(client[1]))
        return options
