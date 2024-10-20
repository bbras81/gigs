import flet as ft
from clients.clients_data import Clients


def clients_add(page: ft.Page):
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
                ft.ElevatedButton(
                    "Add",
                    on_click=lambda _: page.go("/view_client"),
                    width=100,
                    height=40,
                ),
            ],
        )
    )

    return export
