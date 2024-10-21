import flet as ft
from clients.clients_data import Clients


def client_card(page: ft.Page):
    clients = Clients()
    export = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    clients.company_name,
                    clients.address,
                    clients.zip_code,
                    clients.city,
                    clients.tax_number,
                    clients.email,
                    clients.phone_number,
                    clients.receipt_required,
                ],
            ),
            padding=ft.padding.all(20),
            expand=True,
            visible=False,
        )
    )

    return export
