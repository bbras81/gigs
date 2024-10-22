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
    add_store = ft.TextButton("Add Store", on_click=lambda e: store_fields(e))
    store_tf = ft.Column(
        controls=[
            clients.store_name,
            ft.TextButton("Ok", on_click=lambda _: store_save(page)),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.END,
        spacing=10,
        visible=False,
    )
    store_list = ft.Column(
        controls=[
            ft.TextField(
                label="Stores",
                value=" ",
                read_only=True,
                border=ft.InputBorder.NONE,
                height=15,
            ),
            ft.ListView(
                controls=[
                    ft.ListTile(
                        title=ft.Text(f"casa de fado"),
                    )
                ]
            ),
        ]
    )
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

    def store_fields(e):
        store_tf.visible = not store_tf.visible
        add_store.text = "Close" if store_tf.visible else "Add Store"
        store_tf.update()
        add_store.update()

    def store_save(page): ...

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
                    store_list,
                    store_tf,
                ]
            ),
            padding=ft.padding.all(20),
            expand=True,
        )
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                client_card_view,
                ft.Row(
                    controls=[
                        add_store,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )
    )
