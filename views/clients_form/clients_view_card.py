import flet as ft
from clients.clients_data import Clients


def client_card(page: ft.Page, client_id: int):
    """
    Creates a card with client information.

    Args:
    page (ft.Page): The page where the card will be shown.
    client_id (int): The id of the client to be shown in the card.

    Returns:
    ft.Card: A card with all the information of the client.
    """
    clients = Clients()
    clients.company_name.read_only = True
    clients.company_name.border = ft.InputBorder.NONE
    clients.company_name.value = clients.client_info_by_id(client_id)[1]
    clients.address.read_only = True
    clients.address.border = ft.InputBorder.NONE
    clients.address.value = clients.client_info_by_id(client_id)[2]
    clients.zip_code.read_only = True
    clients.zip_code.border = ft.InputBorder.NONE
    clients.zip_code.value = clients.client_info_by_id(client_id)[3]
    clients.city.read_only = True
    clients.city.border = ft.InputBorder.NONE
    clients.city.value = clients.client_info_by_id(client_id)[4]
    clients.tax_number.read_only = True
    clients.tax_number.border = ft.InputBorder.NONE
    clients.tax_number.value = clients.client_info_by_id(client_id)[5]
    clients.email.read_only = True
    clients.email.border = ft.InputBorder.NONE
    clients.email.value = clients.client_info_by_id(client_id)[6]
    clients.phone_number.read_only = True
    clients.phone_number.border = ft.InputBorder.NONE
    clients.phone_number.value = clients.client_info_by_id(client_id)[7]
    clients.receipt_required.disabled = True
    if clients.client_info_by_id(client_id)[8] == 1:
        clients.receipt_required.value = True
    else:
        clients.receipt_required.value = False

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

    return export
