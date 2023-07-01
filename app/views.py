from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoModel

import os
def index (request) :
    if request.method == "POST" :
        video = request.FILES['video']
        title = video.name
        video.name = 'v.mp4'

        main_url = request.META['HTTP_REFERER']
        direction = os.getcwd()

        create_video_uuid = VideoModel.save_video(
            main_url = main_url,
            title = title,
            video = video,
            direction = direction
            )
        
        return redirect('watch',create_video_uuid)

    return render(request,'index.html')


def WatchVideo (request,video_uuid) :
    
    video = get_object_or_404(VideoModel, user_uuid = video_uuid )
   
    context = {
        'video' : video,
    }

    return render(request,'video.html',context)