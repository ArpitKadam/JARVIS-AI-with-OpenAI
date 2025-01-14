import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
speaker.Voice = voices.Item(1)

while 1:
    print("Enter")
    s = input()
    speaker.Speak(s)
