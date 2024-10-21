import flet as ft
from clients.clients_data import Clients


def clients_view(page: ft.Page):
    clients = Clients()
    clients.company_name.read_only = True
    clients.company_name.value = "Bruno Brás"
    clients.company_name.border = ft.InputBorder.NONE

    def load_clients_list():
        list = clients.client_info_all()
        client_list = []
        for i in range(len(list)):
            client_list.append(
                ft.ListTile(
                    title=ft.Text(f"{list[i][1]} (ID: {list[i][0]})"),
                    subtitle=ft.Text(f"Tax Number: {list[i][5]}"),
                    on_click=lambda e, client_id=list[i][0]: page.go(
                        f"/client_card/{client_id}"
                    ),
                ),
            )
        return client_list

    list_view = ft.ListView(
        controls=load_clients_list(),
        spacing=10,
        padding=10,
        divider_thickness=1,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                list_view,
            ]
        ),
        expand=True,
        margin=ft.margin.all(0),
    )
