import flet as ft
from clients.clients_data import Clients
import db


class Gigs:
    def __init__(self):
        self.gig_date = ft.TextField(
            label="Gig date",
            autofocus=True,
        )
        self.gig_hour = ft.Dropdown(label="Gig start", max_menu_height=300)
        self.gig_cachet = ft.TextField(label="Cachet", suffix_text="€")
        self.gig_local = ft.Dropdown(hint_text="Please select a store")

        self.gig_local.options = self.get_house_dropdown()
        self.gig_hour.options = self.hours_dropdown()

    @staticmethod
    def get_house_dropdown():
        client_data = Clients().get_store_all()
        options = []
        for client in client_data:
            options.append(ft.dropdown.Option(client[1]))
        return options

    @staticmethod
    def hours_dropdown():
        hours = []
        for i in range(0, 24):
            if i >= 0 and i < 10:
                hours.append(ft.dropdown.Option(str(f"0{i}:00h")))
            else:
                hours.append(ft.dropdown.Option(str(f"{i}:00h")))
        return hours
