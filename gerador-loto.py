import flet as ft
import random

def main(page: ft.Page):
    # Configurações da página
    page.bgcolor = "#228B22"
    page.title = "Gerador de Números para Loteria"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para gerar números aleatórios
    def gerar_numeros(e):
        for i in range(len(caixas)):
            caixas[i].content.value = str(random.randint(1, 60))
        page.update()

    # Lista de caixas redondas
    caixas = [
        ft.Container(
            content=ft.Text(value="0", color="black"),
            width=100,
            height=100,
            border_radius=50,
            bgcolor="white",
            alignment=ft.alignment.center
        )
        for _ in range(6)  # Gerar 6 caixas
    ]

    # Botão para gerar números
    botao_gerar = ft.ElevatedButton(
        text="Gerar Números",
        on_click=gerar_numeros,
    )

    # Adicionar elementos à página
    page.add(
        ft.Column(
            [
                ft.Row(caixas, alignment=ft.MainAxisAlignment.CENTER),
                botao_gerar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)