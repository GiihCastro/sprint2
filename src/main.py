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

    def menu(e: ft.ControlEvent):
        page.remove(login)
        page.add(menu)

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
                            src="safecityimg.png",
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
                                        text='Login',
                                        color=ft.colors.WHITE,
                                        bgcolor="#0D633D",
                                        width=158,
                                        height=55,
                                        on_click=menu
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
                            margin=ft.margin.only(top=30, bottom=30),  
                            content=ft.Text(
                                value='C A D A S T R O',
                                weight='bold',
                                size=32,
                                color="#0D633D"
                            )
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text='Nome completo',
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
                                    hint_text='E-mail',
                                    prefix_icon=ft.icons.EMAIL,
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
                                ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text='Criar Conta',
                                        color=ft.colors.WHITE,
                                        bgcolor="#0D633D",
                                        width=158,
                                        height=55,
                                ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.TextButton(
                                    text='―――――――― Entrar com ――――――――',
                                    on_click=logar,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.with_opacity(0.6, ft.colors.BLACK)
                                    )
                                ),
                                ft.Row(
                                    controls = [
                                        ft.Image(
                                            src="googleicon.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Image(
                                            src="facebookicon.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                controls=[
                                    ft.TextButton(
                                        text='Já tem uma conta? Entrar',
                                        on_click=logar,
                                        style=ft.ButtonStyle(
                                            color=ft.colors.with_opacity(0.6, ft.colors.BLACK)
                                        )
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=30  
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    menu = ft.Column(
    controls=[ 
        ft.Container(
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            width=353,
            height=767,
            margin=ft.margin.all(20),
            content=ft.Column(
                controls=[ 
                    ft.Container(
                        bgcolor="#0D633D", 
                        width=page.width,   
                        height=115,         
                        border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),  
                        padding=ft.padding.all(20),
                        gradient=ft.LinearGradient(
                            colors=["#0D633D", "#074A2C"],
                        ),
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src="avatar.png",
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            margin=ft.margin.only(top=10),  
                                            content=ft.Text(
                                                value="Olá, Fulano",
                                                size=24,
                                                color=ft.colors.WHITE,
                                            )
                                        ),
                                        ft.Text(
                                            value="fulanouser@gmail.com",
                                            size=14,
                                            color=ft.colors.WHITE,
                                        ),
                                    ],
                                    spacing=0
                                ),
                                ft.Icon(
                                    ft.icons.SETTINGS,  
                                    size=30,
                                    color=ft.colors.WHITE,
                                ), 
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.START
                        ),
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text='Buscar',
                                    prefix_icon=ft.icons.SEARCH,
                                    suffix_icon=ft.icons.MIC_NONE,
                                    text_vertical_align=-0.30,
                                    border_color="#0D633D",
                                    border_radius=10,
                                ),
                            ],
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),

                        padding=ft.padding.all(20),
                    ),
                    ft.Image(
                        src="mapa.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),

                    ft.Column(
                        controls=[
                            ft.Row(
                                ft.Icon(
                                    ft.icons.PLACE_OUTLINED,  
                                    size=18,
                                    color=ft.colors.WHITE,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            margin=ft.margin.only(top=10),  
                                            content=ft.Text(
                                                value="Casa",
                                                size=14,
                                                color=ft.colors.WHITE,
                                            )
                                        ),
                                        ft.Text(
                                            value="Rua Flutuantes 232, Joalba",
                                            size=12,
                                            color=ft.colors.WHITE,
                                        ),
                                    ],
                                    spacing=0
                                ),
                            ),
                        ],
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        ),
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(menu)

if __name__ == '__main__':
    ft.app(target=main)
