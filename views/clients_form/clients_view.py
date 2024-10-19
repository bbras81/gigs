import flet as ft
from clients.clients_data import Clients


def clients_view(page: ft.Page):
    clients = Clients()
    export = ft.Container(
        content=ft.Column(
            controls=[
                clients.company_name_tf,
                clients.address_tf,
                clients.zip_code_tf,
                clients.city_tf,
                clients.tax_number_tf,
                clients.email_tf,
                clients.phone_number_tf,
                clients.receipt_required_tf,
            ],
        )
    )

    return export
