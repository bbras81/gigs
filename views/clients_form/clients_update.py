import flet as ft
from clients.clients_data import Clients
from errors_handling import modal_alert

clients = Clients()


def clients_update(page: ft.Page, client_id: int):
    page.title = "Add Client"
    client_info = clients.client_info_by_id(client_id)
    clients.id_client = client_id
    clients.company_name.value = client_info[1]
    clients.address.value = client_info[2]
    clients.zip_code.value = client_info[3]
    clients.city.value = client_info[4]
    clients.tax_number.value = str(client_info[5])
    clients.email.value = client_info[6]
    clients.phone_number.value = str(client_info[7])
    if client_info[8] == 1:
        clients.receipt_required.value = True
    else:
        clients.receipt_required.value = False

    export = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Update Client"),
                clients.company_name,
                clients.address,
                clients.zip_code,
                clients.city,
                clients.tax_number,
                clients.email,
                clients.phone_number,
                ft.Row(
                    [clients.receipt_required],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.ElevatedButton(
                    "Update",
                    on_click=lambda _: save_client(page),
                    width=100,
                    height=40,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.all(15),
        expand=True,
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
            "id_client": clients.id_client,
            "store_name": (
                clients.store_name.value.strip()
                if clients.store_name.value != ""
                else clients.company_name.value.strip()
            ),
        }
        clients.update_client(client_data)
        # clients.add_store_db(client_data)

        page.go("/view_client")
