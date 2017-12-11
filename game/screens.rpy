# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    
   tag menu
   # Tells Ren'Py what images to display on screen.
   add "ui/main/background.png"
   add "ui/main/logo.png" at from_top2
   add "ui/main/satan.png" at from_right

   # Imagebuttons, 'Auto' tells it to use both idle and hover states. Focus masks is something to do with the alpha properties but IDK off the top of my head.
   imagebutton auto "ui/main/start_%s.png" xpos 0 ypos 480 focus_mask None action Start() at from_left
   imagebutton auto "ui/main/load_%s.png" xpos 0 ypos 540 focus_mask None action ShowMenu('load') at from_left
   imagebutton auto "ui/main/prefs_%s.png" xpos 0 ypos 600 focus_mask None action ShowMenu('preferences') at from_left
   imagebutton auto "ui/main/extras_%s.png" xpos 0 ypos 660 focus_mask None action ShowMenu('preferences') at from_left
   imagebutton auto "ui/main/quit_%s.png" xpos 0 ypos 720 focus_mask None action Quit(confirm=False) at from_left


init -2:
    # Defines transform properties to make images move.
    transform fade_in:
        alpha 0.0
        linear 2.5 alpha 1.0
    transform from_left:
        alpha 0.0 xpos -500
        linear 2.0 alpha 1.0 xpos 10
    transform from_right:
        alpha 0.0 xpos 2420
        linear 2.5 alpha 1.0 xpos 0
    transform from_top:
        alpha 0.0 ypos -1100
        linear 2.5 alpha 1.0 ypos 0
    transform from_bottom:
        alpha 0.0 ypos 2200
        linear 2.5 alpha 1.0 ypos 1080
    transform from_bottom2:
        alpha 0.0 ypos 1080
        easein 2.5 alpha 1.0 ypos 0
    transform from_left2:
        alpha 0.0 xpos -500
        linear 2.5 alpha 1.0 xpos 0
    transform from_right2:
        alpha 0.0 xpos 2420
        linear 2.5 alpha 1.0 xpos 1920
    transform effect1:
        alpha 0.0
        linear 2.5 alpha 1.0
    transform from_top2:
        alpha 0.0 ypos -300
        linear 1.25 alpha 1.0 ypos 0
    transform from_bottom3:
        alpha 0.0 ypos 1300
        linear 2.5 alpha 1.0 ypos 1080


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    imagebutton auto "ui/navigation/return_%s.png" xpos 225 ypos 970 focus_mask None action Return() at effect1
    imagebutton auto "ui/navigation/save_%s.png" xpos 400 ypos 1020 focus_mask None action ShowMenu('save') at effect1
    imagebutton auto "ui/navigation/load_%s.png" xpos 675 ypos 970 focus_mask None action ShowMenu('load') at effect1
    imagebutton auto "ui/navigation/prefs_%s.png" xpos 850 ypos 1020 focus_mask None action ShowMenu('preferences') at effect1
    imagebutton auto "ui/navigation/title_%s.png" xpos 1125 ypos 970 focus_mask None action MainMenu() at effect1
    imagebutton auto "ui/navigation/quit_%s.png" xpos 1300 ypos 1020 focus_mask None action Quit() at effect1


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen save:
    tag menu
    add "ui/navigation/background.png" 
    add "ui/prefs/base.png" at effect1
    use navigation
    use file_picker
    
screen load:
    tag menu
    add "ui/navigation/background.png" 
    add "ui/prefs/base.png" at effect1
    use navigation
    use file_picker
    
screen file_picker:
    imagebutton auto "ui/saveload/quick_%s.png" xpos 200 ypos 823 focus_mask None action FilePage("quick") at effect1
    imagebutton auto "ui/saveload/auto_%s.png" xpos 450 ypos 823 focus_mask None action FilePage("auto") at effect1
    imagebutton auto "ui/saveload/1_%s.png" xpos 975 ypos 823 focus_mask None action FilePage(1) at effect1
    imagebutton auto "ui/saveload/2_%s.png" xpos 1050 ypos 823 focus_mask None action FilePage(2) at effect1
    imagebutton auto "ui/saveload/3_%s.png" xpos 1125 ypos 823 focus_mask None action FilePage(3) at effect1
    imagebutton auto "ui/saveload/4_%s.png" xpos 1200 ypos 823 focus_mask None action FilePage(4) at effect1
    imagebutton auto "ui/saveload/5_%s.png" xpos 1275 ypos 823 focus_mask None action FilePage(5) at effect1
    imagebutton auto "ui/saveload/6_%s.png" xpos 1350 ypos 823 focus_mask None action FilePage(6) at effect1
    imagebutton auto "ui/saveload/7_%s.png" xpos 1425 ypos 823 focus_mask None action FilePage(7) at effect1
    imagebutton auto "ui/saveload/8_%s.png" xpos 1500 ypos 823 focus_mask None action FilePage(8) at effect1
    imagebutton auto "ui/saveload/9_%s.png" xpos 1575 ypos 823 focus_mask None action FilePage(9) at effect1
    
    imagebutton auto "ui/saveload/slot_%s.png" xpos 236 ypos 195 focus_mask True action FileAction(1) at effect1
    add "ui/saveload/empty.png" xpos 255 ypos 214 at effect1
    use load_save_slot(number=1, x=236, y=195) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 236 ypos 406 focus_mask True action FileAction(2) at effect1
    add "ui/saveload/empty.png" xpos 255 ypos 425 at effect1
    use load_save_slot(number=2, x=236, y=406) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 236 ypos 617 focus_mask True action FileAction(3) at effect1
    add "ui/saveload/empty.png" xpos 255 ypos 636 at effect1
    use load_save_slot(number=3, x=236, y=617) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 1023 ypos 195 focus_mask True action FileAction(4) at effect1
    add "ui/saveload/empty.png" xpos 1042 ypos 214 at effect1
    use load_save_slot(number=4, x=1023, y=195) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 1023 ypos 406 focus_mask True action FileAction(5) at effect1
    add "ui/saveload/empty.png" xpos 1042 ypos 425 at effect1
    use load_save_slot(number=5, x=1023, y=406) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 1023 ypos 617 focus_mask True action FileAction(6) at effect1
    add "ui/saveload/empty.png" xpos 1042 ypos 636 at effect1
    use load_save_slot(number=6, x=1023, y=617) 
    
screen load_save_slot:
    hbox:
        style_group "watercress"
        textbutton _("Delete") xpos x+520 ypos y+125  action FileDelete(number) at effect1

    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty."), FileSaveName(number))

    text file_text xpos x+295 ypos y+18 style_group "watercress" at effect1

    add FileScreenshot(number) xpos x+19 ypos y+19 at effect1
    
init -2 python:
    config.thumbnail_width = 260
    config.thumbnail_height = 146

init -2:
    style watercress_button:
        is default
        background None
    style watercress_button_text:
        is default
        size 38
        idle_color "#FFE2BC"
        hover_color "#5B3D28"
        insensitive_color "#808080"
        drop_shadow [(2, 2,)]
        drop_shadow_color (0, 0, 0, 100)
    style watercress_text:
         is default
         size 42
         color "#FFE2BC"
         idle_color "#FFE2BC"
         drop_shadow [(2, 2,)]
         drop_shadow_color (0, 0, 0, 100)


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    add "ui/navigation/background.png" 
    add "ui/prefs/base.png" at effect1
    add "ui/prefs/prefs_titles.png" at effect1
    use navigation
    
    imagebutton auto "ui/prefs/fullscreen_%s.png" xpos 183 ypos 274 focus_mask None action Preference('display','fullscreen') at effect1
    imagebutton auto "ui/prefs/windowed_%s.png" xpos 505 ypos 273 focus_mask None action Preference('display', 'window')  at effect1
    
    imagebutton auto "ui/prefs/enabled_%s.png" xpos 183 ypos 432 focus_mask None action Preference('transitions', 'all') at effect1
    imagebutton auto "ui/prefs/disabled_%s.png" xpos 505 ypos 432 focus_mask None action Preference('transitions', 'none') at effect1
    
    imagebutton auto "ui/prefs/skipall_%s.png" xpos 183 ypos 604 focus_mask None action Preference('skip', 'all') at effect1
    imagebutton auto "ui/prefs/skipread_%s.png" xpos 505 ypos 603 focus_mask None action Preference('skip', 'seen') at effect1
    
    imagebutton auto "ui/prefs/stopskip_%s.png" xpos 183 ypos 768 focus_mask None action Preference('after choices', 'stop') at effect1 
    imagebutton auto "ui/prefs/keepskip_%s.png" xpos 505 ypos 768 focus_mask None action Preference('after choices', 'skip') at effect1
    
    frame xpos 1170 ypos 456:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
        at effect1
    frame xpos 1170 ypos 701:
        style_group "pref"
        has vbox
        bar value Preference("voice volume")
        at effect1
    frame xpos 1171 ypos 212:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
        at effect1
    frame xpos 1172 ypos 332:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
        at effect1
    frame xpos 1171 ypos 572:
        style_group "pref"
        has vbox
        bar value Preference("sound volume") 
        at effect1
        

        
init -2 python: 
    style.pref_frame.background = None
    style.pref_slider.left_bar = "ui/prefs/bar_full.png"
    style.pref_slider.right_bar = "ui/prefs/bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.thumb_offset = 0
    style.pref_slider.xmaximum = 580
    style.pref_slider.ymaximum = 51
    style.pref_slider.xminimum = 580

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    add "ui/yn/background.png" 
    add "ui/yn/base_right.png" xanchor 1.0 xpos 1920 at effect1
    imagebutton auto "ui/yn/yes_%s.png" xpos 1794 ypos 574 xanchor 1.0 focus_mask None action yes_action at effect1
    imagebutton auto "ui/yn/no_%s.png" xpos 1794 ypos 635 xanchor 1.0 focus_mask None action no_action at effect1
    
    if message == layout.ARE_YOU_SURE:
        add "ui/yn/message_quit.png" xanchor 1.0 xpos 1920 at effect1
    elif message == layout.DELETE_SAVE:
        add "ui/yn/message_delete.png" xanchor 1.0 xpos 1920 at effect1
    elif message == layout.OVERWRITE_SAVE:
        add "ui/yn/message_overwrite.png" xanchor 1.0 xpos 1920 at effect1
    elif message == layout.LOADING:
        add "ui/yn/message_load.png" xanchor 1.0 xpos 1920 at effect1
    elif message == layout.QUIT:
        add "ui/yn/message_quit.png" xanchor 1.0 xpos 1920 at effect1
    elif message == layout.MAIN_MENU:
        add "ui/yn/message_title.png" xanchor 1.0 xpos 1920 at effect1


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 24
        idle_color "#888888"
        hover_color "#5B3D28"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

