import flet as ft
from clients.clients_data import Clients


def clients_view(page: ft.Page):
    clients = Clients()
    clients.company_name_tf.read_only = True
    clients.company_name_tf.value = "Bruno Brás"
    clients.company_name_tf.border = ft.InputBorder.NONE

    export = ft.Card(
        content=ft.Container(
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
            ),
            padding=ft.padding.all(20),
            expand=True,
        )
    )
    return export
