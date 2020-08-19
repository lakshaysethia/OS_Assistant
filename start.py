#import necessary libraries
import os,subprocess
import pyttsx3
import time
#
pyttsx3.speak("Welcome to my world user.")
# pyttsx3.speak("What would you like to do now?")
while True:
    pyttsx3.speak("What would you like to do, Please type ?")
    p=input("User typing...")
# To start notepad
    if (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("notepad" in p) or ("editor" in p) or ("text" in p)):
        pyttsx3.speak("okay. your Notepad is about to start please hold on")
        os.system("start notepad")
        pyttsx3.speak("Notepad opened")
        # time.sleep(10)
# To start chrome
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p) )and (("chrome" in p) or ("browser" in p) or ("googlechrome" in p) or ("google chrome" in p)):   
        pyttsx3.speak("okay. your chrome browser is about to start please hold on")
        os.system("start chrome")
        pyttsx3.speak("Chrome browser opened")
# To start paint
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p) )and (("paint" in p) or ("color" in p)or ("drawing" in p) or ("draw" in p)):   
        pyttsx3.speak("okay. your microsoft paint software is about to start please hold on")
        os.system("start MSPaint")
        pyttsx3.speak("Paint opened")
# To start control panel
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("control" in p) or ("panel" in p) or ("control panel" in p)):   
        pyttsx3.speak("okay. your control panel is about to start please hold on")
        os.system("start control")
        pyttsx3.speak("Control panel opened")
# To start media player
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("player" in p )or ("media" in p) or ("mediaplayer" in p)or ("media player" in p)):   
        pyttsx3.speak("okay. your media player is about to start please hold on")
        os.system("start wmplayer")
        pyttsx3.speak("media player opened")
# To start excel sheet
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("excel" in p) or ("spreadsheet" in p )or ("msexcel" in p) or ("excel sheet" in p)):   
        pyttsx3.speak("okay. your microsoft excel is about to start please hold on")
        os.system("start excel")
        pyttsx3.speak("microsoft excel opened")
# To start wordpad
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p) )and (("wordpad" in p) or ("word pad" in p) or ("write"in p)) :   
        pyttsx3.speak("okay. your wordpad is about to start please hold on")
        os.system("start wordpad")
        pyttsx3.speak("wordpad opened")
# To start microsoft word
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("msword" in p) or ("word" in p) or ("ms word"in p)):   
        pyttsx3.speak("okay. your microsoft word is about to start please hold on")
        os.system("start winword")
        pyttsx3.speak("microsoft word opened")
# To start command window
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("cmd" in p) or ("terminal" in p) or ("command" in p)):   
        pyttsx3.speak("okay. your command window is about to start please hold on")
        os.system("start cmd")
        pyttsx3.speak("command window opened")
# To open windows settings
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("setting" in p) or ("settings" in p) or ("windows settings" in p)):   
        pyttsx3.speak("okay. your windows settings is about to start please hold on")
        os.system("start ms-settings:")
        pyttsx3.speak("windows settings opened")
# To open voice recorder
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("voice recorder" in p) or ("recorder" in p) or ("voice" in p) or("recording" in p)):   
        pyttsx3.speak("okay. your Voice recorder is about to start please hold on")
        os.system("start explorer.exe shell:appsFolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App")
        pyttsx3.speak("voice recorder opened")
# To open Adobe reader
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("pdf" in p) or ("adobe reader" in p) or ("reader" in p) or("pdf file reader" in p)):   
        pyttsx3.speak("okay. your Adobe reader is about to start please hold on")
        os.system("start acrord32")
        pyttsx3.speak("Adobe reader opened")
# To open Alarm and clock
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("alarm" in p) or ("clock" in p) or ("timer" in p) or("stopwatch" in p) or ("watch" in p)):   
        pyttsx3.speak("okay. your alarm and clock is about to start please hold on")
        os.system("start explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App")
        pyttsx3.speak("Alarm and clock opened")
# To open task manager
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("task" in p) or ("manager" in p) or ("task manager" in p) or("taskmanager" in p)):   
        pyttsx3.speak("okay. your task manager is about to start please hold on")
        os.system("start taskmgr")
        pyttsx3.speak("Task manager opened")
# To start outlook
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("outlook" in p) or ("out" in p) or ("look" in p)):   
        pyttsx3.speak("okay. your microsoft outlook is about to start please hold on")
        os.system("start outlook")
        pyttsx3.speak("microsoft outlook opened")  
# To start Microsoft power shell 
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("powershell" in p) or ("shell" in p )or ("shell window" in p)):   
        pyttsx3.speak("okay. your power shell window is about to start please hold on")
        os.system("start powershell")
        pyttsx3.speak("Microsoft power shell opened")
# To start calculator
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("calc" in p )or ("calculator" in p )or ("calculate" in p)):   
        pyttsx3.speak("okay. your calculator is about to start please hold on")
        os.system("start calc")
        pyttsx3.speak("calculator opened")
# To start skype video call
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("skype" in p )or ("video call" in p)or ("video chat" in p) or ("skype call" in p)):   
        pyttsx3.speak("okay. your skype software is about to start please hold on")
        os.system("start skype")
        pyttsx3.speak("skype opened")
# To start internet explorer
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("internet" in p) or ("explorer" in p)) :   
        pyttsx3.speak("okay. your internet explorer is about to start please hold on")
        os.system("start iexplore")
        pyttsx3.speak("internet explorer opened")
# To start onemote
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("onenote" in p) or ("msnote" in p) or ("note" in p)) :   
        pyttsx3.speak("okay. your microsoft onenote is about to start please hold on")
        os.system("start onenote")
        pyttsx3.speak("microsoft onenote opened")
# To start camera
    elif ("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p) and (("camera" in p) or ("take photo" in p) or ("click" in p)):   
        pyttsx3.speak("okay. your camera is about to start please hold on")
        subprocess.run("start microsoft.windows.camera:",shell=True)
        pyttsx3.speak("camera opened")
# To start file explorer
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("file" in p) or ("files" in p) or ("recent" in p) or ("file explorer"in p)):   
        pyttsx3.speak("okay. your file explorer is about to start please hold on")
        os.system("start explorer")
        pyttsx3.speak("file explorer opened")
# To start slack channel
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("slack" in p) or ("channel" in p) or ("slack channel" in p)):   
        pyttsx3.speak("okay. your slack channel is about to start please hold on")
        os.system("start slack")
        pyttsx3.speak("slack channel opened")
# To start power point presentation
    elif (("run" in p) or ("execute" in p )or ("start" in p )or ("open" in p)) and (("ppt" in p )or ("power" in p )or ("power point" in p) or ("presentation" in p)):   
        pyttsx3.speak("okay. your power point is about to start please hold on")
        os.system("start powerpnt")
        pyttsx3.speak("microsoft power point opened")
# if typed "not" to do that command 
    elif (("don't" in p) or ("not" in p) or ("can't" in p) or ("can not" in p) or ("do not" in p) or ("dont" in p)):
        pyttsx3.speak("ok as you say user i will not do")
## To shutdown the laptop or pc
    elif (("shutdown" in p) or ("turn off" in p) or ("close" in p))and  (("pc" in p) or ("laptop" in p)or ("computer" in p)):   
        pyttsx3.speak("okay. Do you really wish to shutdown your computer ? type yes or no")
        shut=input("User typing...(yes/no)")
        if shut=="no":
            pyttsx3.speak("great ! you have choosen no, so please continue ")
        else:
            pyttsx3.speak("you have choosen yes!")
            pyttsx3.speak("Thanks for using the service hope you enjoyed it")
            pyttsx3.speak("good bye")
            pyttsx3.speak("your computer is shuting down")
            os.system("shutdown /s /t 1")
# To restart laptop or pc
    elif ("restart pc " in p) and (("pc" in p) or ("laptop" in p)or ("computer" in p)) :   
        pyttsx3.speak("okay. Do you really wish to restart your computer ? type yes or no")
        shut=input("User typing...(yes/no)")
        if shut=="no":
            pyttsx3.speak("great ! you have choosen no so please continue ")
        else:
            pyttsx3.speak("you have choosen yes")
            pyttsx3.speak("Thanks for using the service hope you enjoyed it")
            pyttsx3.speak("good bye")
            pyttsx3.speak("your computer is restarting now")
            os.system("shutdown /r /t 1")
# To close this menu bot 
    elif (("close" in p )or ("shutdown"in p) or ("turn off" in p)) and (("yourself" in p) or ("you" in p) or ("your service" in p )) :
        pyttsx3.speak(" ohh your really want to close my service")
        pyttsx3.speak("type yes to close or no to continue")
        t=input("User typing...")
        if t=="yes":
            break
        else:
            pyttsx3.speak("Thanks keep going.")
            pass
# if something typed incorrectly or useless command
    else:
        pyttsx3.speak("please check you spelling of the program or type correctly what you want to do.")
        pyttsx3.speak("so that i can help you")
        pyttsx3.speak("hope you understand")

pyttsx3.speak("Thanks for using the service hope you enjoyed it")
pyttsx3.speak("good bye")



