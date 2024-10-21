import flet as ft
from clients.clients_data import Clients


def clients_view(page: ft.Page):
    clients = Clients()
    clients.company_name.read_only = True
    clients.company_name.value = "Bruno Brás"
    clients.company_name.border = ft.InputBorder.NONE

    def card_view(client_id):
        list_view.visible = False
        export.visible = True
        page.update()

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
            visible=False,
        )
    )

    def load_clients_list():
        list = clients.client_info_all()
        client_list = []
        for i in range(len(list)):
            client_list.append(
                ft.ListTile(
                    title=ft.Text(f"{list[i][1]} (ID: {list[i][0]})"),
                    subtitle=ft.Text(f"Tax Number: {list[i][5]}"),
                    on_click=lambda _: card_view({list[i][0]}),
                ),
            )
        return client_list

    list_view = ft.ListView(
        controls=load_clients_list(),
        spacing=10,
        padding=10,
        divider_thickness=1,
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                export,
                list_view,
            ]
        ),
        expand=True,
        margin=ft.margin.all(0),
    )

    return container
