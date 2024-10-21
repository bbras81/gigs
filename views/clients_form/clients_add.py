import flet as ft
from clients.clients_data import Clients

clients = Clients()


def clients_add(page: ft.Page):
    page.title = "Add Client"
    export = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Add Client"),
                clients.company_name,
                clients.address,
                clients.zip_code,
                clients.city,
                clients.tax_number,
                clients.email,
                clients.phone_number,
                clients.receipt_required,
                ft.ElevatedButton(
                    "Add",
                    on_click=save_client,
                    width=100,
                    height=40,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    return export


def save_client():
    if clients.company_name_tf.value:
        clients.company_name = clients.company_name_tf.value
