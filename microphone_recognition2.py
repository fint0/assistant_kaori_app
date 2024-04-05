import speech_recognition as sr

class MicrophoneRecognition2:
  def __init__(self):
     pass
  def run_recognition_mic(self):
     
    """ マイクを使って音声認識をする関数 """
 
    # Recognizerをインスタンス化
    r = sr.Recognizer()
 
    # print文が表示されたらマイクに話しかける
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)
    try:
        # Google Speech Recognitionを実行→テキスト化
        text = r.recognize_google(audio, language="ja")
    except sr.UnknownValueError:
        text = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        text = "Could not request results from Google Speech Recognition service; {0}".format(e)
 
    return text
  
