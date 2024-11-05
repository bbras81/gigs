import flet as ft
from clients.clients_data import Clients
import db


class Gigs:
    def __init__(self):

        self.gig_date = ft.TextField(

            label="Gig date",
        )
        self.hour_picker = ft.Container(
            content=(
                ft.CupertinoDatePicker(
                    date_picker_mode=ft.CupertinoDatePickerMode.TIME,
                    use_24h_format=True,
                    minute_interval=15,
                )
            ),
            height=216,
            padding=ft.padding.only(top=6),
            visible=False,
        )

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

    def add_gig():
        pass
