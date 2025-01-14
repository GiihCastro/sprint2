import flet as ft

def main(page: ft.Page):
    page.title = 'Safecity'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = True
    page.padding = ft.padding.all(0)

    def logar(e: ft.ControlEvent):
        page.remove(register)
        page.add(login)
    
    def registar(e: ft.ControlEvent):
        page.remove(login)
        page.add(register)

    login = ft.Column(
        controls=[ 
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=353,
                height=767,
                padding=ft.padding.all(10),
                margin=ft.margin.all(20),
                content=ft.Column(
                    controls=[ 
                        ft.Container(
                            margin=ft.margin.only(top=20),
                            content=ft.Text(
                                value='S A F E C I T Y',
                                weight='bold',
                                size=32,
                                color="#0D633D"
                            )
                        ),
                        ft.Image(
                            src="safecity_app/src/assets/safecityimg.png",
                            width=344,
                            height=273,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text='E-mail',
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    )
                                ),
                                ft.TextField(
                                    hint_text='Senha',
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    password=True,
                                    can_reveal_password=True
                                ),
                                 ft.Row(
                                controls=[
                                    ft.Checkbox(
                                        label="Lembrar senha", 
                                        value=False,
                                        active_color="#0D633D",
                                        check_color="#ffffff",
                                        label_style=ft.TextStyle(
                                            color="#5E5E5E"
                                        ),
                                    ),
                                    ft.TextButton(
                                        text='Esqueci a senha',
                                        style=ft.ButtonStyle(
                                        color= "#5E5E5E",
                                        text_style=ft.TextStyle(
                                        weight="light",
                                        decoration=ft.TextDecoration.UNDERLINE, 
                                        ),
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text='L O G I N',
                                        color=ft.colors.WHITE,
                                        bgcolor="#0D633D",
                                        width=158,
                                        height=55,
                                        on_click=logar
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER 
                            ),
                            ft.Row(
                                controls=[
                                    ft.TextButton(
                                        text='Não possui uma conta?',
                                        on_click=registar,
                                        style=ft.ButtonStyle(
                                            color=ft.colors.with_opacity(0.6, ft.colors.BLACK),
                                            text_style=ft.TextStyle(
                                                decoration=ft.TextDecoration.UNDERLINE, 
                                            ),
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER 
                            ),
                        ],
                        spacing=15
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    register = ft.Column(
        controls=[ 
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=353,
                height=767,
                padding=ft.padding.all(10),
                margin=ft.margin.all(20),
                content=ft.Column(
                    controls=[ 
                        ft.Container(
                            margin=ft.margin.only(top=20),
                            content=ft.Text(
                                value='S A F E C I T Y',
                                weight='bold',
                                size=32,
                                color="#0D633D"
                            )
                        ),
                        ft.Image(
                            src="safecity_app/src/assets/safecityimg.png",
                            width=344,
                            height=273,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text='E-mail',
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    )
                                ),
                                ft.TextField(
                                    hint_text='Senha',
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    password=True,
                                    can_reveal_password=True
                                ),
                                ft.TextField(
                                    hint_text='Confirmar Senha',
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=-0.30,
                                    border=ft.InputBorder.UNDERLINE,
                                    border_width=2,
                                    border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                    hint_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
                                    ),
                                    text_style=ft.TextStyle(
                                        size=14,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
                                    ),
                                    password=True,
                                    can_reveal_password=True
                                ),
                                ft.ElevatedButton(
                                    text='Registrar',
                                    color=ft.colors.WHITE,
                                    bgcolor="#0D633D",
                                    width=158,
                                    height=55,
                                ),
                                ft.TextButton(
                                    text='Já tenho conta',
                                    on_click=logar,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.with_opacity(0.6, ft.colors.BLACK)
                                    )
                                )
                            ],
                            spacing=15
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)
