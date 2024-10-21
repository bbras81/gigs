import flet as ft
from clients.clients_data import Clients


def clients_view(page: ft.Page):
    clients = Clients()
    clients.company_name.read_only = True
    clients.company_name.value = "Bruno Brás"
    clients.company_name.border = ft.InputBorder.NONE

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
        )
    )

    list_view = ft.ListView(
        
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                list_view,
            ],
        ),
        expand=True,
        bgcolor=ft.colors.TEAL_100,
        margin=ft.margin.all(0),
    )
    return container
