import flet as ft
from clients.clients_data import Clients


def client_card(page: ft.Page, client_id: int) -> ft.Card:
    """
    Creates a card with client information.

    Args:
        page (ft.Page): The page where the card will be shown.
        client_id (int): The id of the client to be shown in the card.

    Returns:
        ft.Card: A card with all the information of the client.
    """

    clients = Clients()
    client = clients.client_info_by_id(client_id)
    client_stores = clients.get_store_by_id(client_id)
    store_list = ft.ListView(controls=[])
    store_list_column = ft.Column(
        controls=[
            ft.TextField(
                label="Stores",
                value=" ",
                read_only=True,
                border=ft.InputBorder.NONE,
                height=15,
            ),
            store_list,
        ],
        visible=False,
    )

    if len(client_stores) > 0:
        for i in range(len(client_stores)):
            store_list.controls.append(
                ft.ListTile(
                    title=ft.Text(f"{client_stores[i][1]}"),
                )
            )
        store_list_column.visible = True

    address = ft.TextField(
        label="Address", value=client[2], read_only=True, border=ft.InputBorder.NONE
    )
    city = ft.TextField(
        label="City", value=client[4], read_only=True, border=ft.InputBorder.NONE
    )
    company_name = ft.TextField(
        label="Company Name",
        value=client[1],
        read_only=True,
        border=ft.InputBorder.NONE,
    )
    email = ft.TextField(
        label="Email", value=client[6], read_only=True, border=ft.InputBorder.NONE
    )
    phone_number = ft.TextField(
        label="Phone Number",
        value=client[7],
        read_only=True,
        border=ft.InputBorder.NONE,
    )
    receipt_required = ft.Checkbox(
        label="Receipt required?", value=bool(client[8]), disabled=True
    )
    tax_number = ft.TextField(
        label="Tax Number",
        value=client[5],
        read_only=True,
        border=ft.InputBorder.NONE,
    )
    zip_code = ft.TextField(
        label="Zip Code", value=client[3], read_only=True, border=ft.InputBorder.NONE
    )

    client_card_view = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    company_name,
                    address,
                    zip_code,
                    city,
                    tax_number,
                    email,
                    phone_number,
                    receipt_required,
                    store_list_column,
                ],
            ),
            padding=ft.padding.all(20),
        )
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                client_card_view,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda _: page.go(f"/client_delete/{client_id}"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            on_click=lambda _: page.go(f"/client_add"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.EDIT,
                            on_click=lambda _: page.go(f"/client_update/{client_id}"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
        ),
        expand=True,
    )
