from django.db import models
import uuid
from .transformer import TranslateVideo

class VideoModel (models.Model) :
    
    title = models.CharField(max_length=1000)
    video = models.FileField(upload_to='video')
    user_uuid = models.CharField(max_length=1000)
    
    date = models.DateTimeField(auto_now_add=True)
    
    fb_url = models.URLField()
    wa_url = models.URLField()
    tel_url = models.URLField()

    starts = models.TextField(null=True,blank=True,max_length=1000000)
    ends = models.TextField(null=True,blank=True,max_length=1000000)
    texts = models.TextField(null=True,blank=True,max_length=1000000)

    def __str__(self) :
        return f"{self.title}"
    
    def save_video(**info) :

        user_uuid = uuid.uuid4()
        main_share_url = info['main_url'] + f'video/{user_uuid}/'
        fb_link = f'https://www.facebook.com/sharer/sharer.php?u={main_share_url}'
        wa_link = f'whatsapp://send?text={main_share_url}'
        te_link = f'https://telegram.me/share/url?url={main_share_url}'

        v = VideoModel.objects.create(
            title = info['title'],
            video = info['video'],
            user_uuid = user_uuid,
            fb_url = fb_link,
            wa_url = wa_link,
            tel_url = te_link,
        )
        v.save()

        data = TranslateVideo(video_src = info['direction'] + v.video.url)

        starts = '@'.join(map(str,data.starts))
        ends = '@'.join(map(str,data.ends))
        texts = '@'.join(map(str,data.texts))

        v.starts = starts
        v.ends = ends
        v.texts = texts
        
        v.save()

        return user_uuid