import easygui


nupud = ["lühikesed","keskmised","pikad"]
vajutati = easygui.buttonbox("Kui pikad juuksed sul on?", choices = nupud)
easygui.msgbox("Sul on "+vajutati+" juuksed!")


