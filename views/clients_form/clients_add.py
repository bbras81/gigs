import flet as ft
from clients.clients_data import Clients
from errors_handling import modal_alert

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
                    on_click=lambda _: save_client(page),
                    width=100,
                    height=40,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    return export


def save_client(page):
    if not clients.company_name.value:
        modal_alert(page, error_text="Please insert a valid Company Name")
        return
    else:
        # Create client data
        client_data = {
            "company_name": clients.company_name.value.strip(),
            "company_address": clients.address.value.strip(),
            "company_zip": clients.zip_code.value.strip(),
            "city": clients.city.value.strip(),
            "tax_number": clients.tax_number.value.strip(),
            "email": clients.email.value.strip(),
            "phone_number": clients.phone_number.value.strip(),
            "receipt_required": 1 if clients.receipt_required.value else 0,
        }
        clients.create_client(client_data)
        page.go("/")
