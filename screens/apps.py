import flet as ft
from config.db_connection import connection

def apps_view(page: ft.Page):
    nome_input = ft.TextField(label="Nome do Programa", width=250)
    caminho_input = ft.TextField(label="Caminho do Programa", width=350, read_only=True)
    file_picker = ft.FilePicker()
    mensagem = ft.Text("", color=ft.Colors.GREEN_400)

    def atualizar_lista():
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM apps_bloqueados")  # ajuste para sua tabela
        novos_apps = cursor.fetchall()
        conn.close()
        page.controls.clear()
        page.add(apps_view(page, novos_apps))
        page.update()

    def pick_file(e):
        file_picker.pick_files(allow_multiple=False)

    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            caminho_input.value = e.files[0].path
            page.update()

    file_picker.on_result = on_file_picked

    titulo = ft.Text(
        "Gerenciador de Apps Bloqueados",
        style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD),
    )

    return ft.Column(
        [
            file_picker,
            titulo,
            ft.Divider(),
            mensagem,
            ft.Divider(),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
