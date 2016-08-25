import pythoncom, pyHook
import ctypes
import sys


def OnMouseEvent(event):
    # called when mouse events are received
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Position:', event.Position)
    print('Wheel:', event.Wheel)
    print('Injected:', event.Injected)
    print('---')
    return True

def OnKeyboardEvent(event):
    print("Message Name: ", event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')
    if chr(event.Ascii) == 'q':
        ctypes.windll.user32.PostQuitMessage(0)
    return True


print("")
print('Python version:')                                            
print((sys.version))
print("")

hm = pyHook.HookManager()       # create a hook manager

hm.MouseAll = OnMouseEvent      # watch for all mouse events
hm.HookMouse()                  # set the hook

hm.KeyDown = OnKeyboardEvent    # watch for "OnKeyboardEvent"
hm.HookKeyboard()               # set the hook

pythoncom.PumpMessages()


# if you reached this point you have terminated the program correctly!
# flush and close any open files etc.

hm.UnhookMouse()
hm.UnhookKeyboard()

print("")
print("The end of Mouse and KBD test!")
print("")