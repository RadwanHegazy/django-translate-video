import whisper, json
from googletrans import Translator


class TranslateVideo () :
    
    def __init__(self,video_src) :
        self.starts = []
        self.ends = []
        self.texts = []

        self.translate(video_src)

    def translate (self,video) :
                
        w_mode = whisper.load_model('base.en')
        tran = w_mode.transcribe(video)['segments']


        trans = Translator()
        
        for i in tran :
            self.starts.append(i['start'])
            self.ends.append(i['end'])

            ar = trans.translate(dest='ar',text=i['text']).text
            self.texts.append(ar)


