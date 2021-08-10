import pydirectinput
import keyboard

if __name__ == '__main__':
    try:
        while True:
            if keyboard.is_pressed("="):
                print("[AutoCobblestoneScript] Enabled!")
                while True:
                    if not keyboard.is_pressed("-"):
                        pydirectinput.keyDown("w")
                        pydirectinput.mouseDown(button="left")
                    else:
                        print("[AutoCobblestoneScript] Disabled!")
                        pydirectinput.keyUp("w")
                        pydirectinput.mouseUp(button="left")
                        break
    except KeyboardInterrupt:
        input("[AutoCobblestoneScript] Press enter to continue...")