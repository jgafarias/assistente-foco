import flet as ft
import threading
import time

def apps_view(page: ft.Page):
    teste = ft.Text("Gerenciador de Apps Bloqueados", style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD))
    return ft.Column(
        [
            teste
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
