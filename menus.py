from scripts.helpers import screenHeight, screenWidth, bgColor
import pygame_menu

menuTheme = pygame_menu.Theme(
    background_color=bgColor,
    widget_padding=20,
    widget_font=pygame_menu.font.FONT_MUNRO,
    widget_font_size=70,
    widget_background_inflate_to_selection=True,
    title_close_button=False,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
    title_font=pygame_menu.font.FONT_8BIT,
    title_font_size=100,
    title_font_shadow=True,
    title_font_shadow_color=(255, 104, 0),
    title_font_shadow_offset=10,
    title_offset=(screenWidth / 2 - 290, screenHeight / 2 - 230))

pausedTheme = pygame_menu.Theme(
    background_color=(0, 0, 0, 0),
    selection_color=(255, 0, 104, 0),
    widget_padding=20,
    widget_font=pygame_menu.font.FONT_MUNRO,
    widget_font_size=70,
    widget_offset=(100, 150),
    widget_alignment=pygame_menu.locals.ALIGN_LEFT,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE,
    title_font=pygame_menu.font.FONT_8BIT,
    title_font_size=95,
    title_background_color=(255, 0, 104),
    title_offset=(30, 110))

menu = pygame_menu.Menu('Pypong', screenWidth, screenHeight,
                        theme=menuTheme, mouse_motion_selection=True)
pausedMenu = pygame_menu.Menu('Pausa', screenWidth, screenHeight,
                        theme=pausedTheme, mouse_motion_selection=True)
