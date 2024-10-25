import flet as ft
import db


class Gigs:
    def __init__(self) -> None:
        self.gig_date = ft.TextField("Gig date")
        self.gig_local = ft.Dropdown("Please select a store")
        self.gig_hour = ft.TextField("Gig start")
        self.gig_cachet = ft.TextField("Cahet")

    db.db_execute(
        """CREATE TABLE IF NOT EXISTS gigs (
                gig_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                gig_date DATE,
                gig_start TEXT,
                gig_cachet FLOAT,
                gig_recipt INTEGER,
                id_client INTEGER,
                FOREIGN KEY (id_client) REFERENCES clients(id_client)
        )"""
    )
