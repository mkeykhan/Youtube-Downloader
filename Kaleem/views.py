from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from django.utils.datastructures import MultiValueDictKeyError
import os




def home(request):


    data = {}
    global text
    if request.method == "GET":
        try:
            text = request.GET['vurl']
            yt = YouTube(text)
            thumb1 = YouTube(text).thumbnail_url

            global istreams

            istreams = yt.streams.all()
            videos = list(enumerate(istreams))

            videos = []

            for vid in range(len(istreams)):
                
                title1 = istreams[vid].title
                link1 = istreams[vid].url
                res1 = istreams[vid].resolution
                mime_type1 = istreams[vid].mime_type
                filesize1 = istreams[vid].filesize_mb

                video = {
                    'title' : title1,
                    'link' : link1,
                    'res' : res1,
                    'mime_type' : mime_type1,
                    'filesize' : int(filesize1),

                }


                videos.append(video)


                data = {
                    'videos': videos,
                    'thumb' : thumb1,
                    'title' : title1,
                    } 

        except Exception as e:
            pass
            # print(str(e))  



        
    if request.method == "POST":
        try:
            inp = int(request.POST['itag'])
            print(inp)
            # print(istreams[inp].title)
            tag = int(istreams[inp].itag)

            homedir = os.path.expanduser("~")
            dirs = homedir + '/Downloads'
            download = YouTube(text).streams.get_by_itag(tag).download(dirs)

        except Exception as e:
            print(str(e))

    return render(request, 'index.html', data)


def aboutus(request):
    return render(request, 'about-us.html')


def userform(request):


    
    return render(request, 'userform.html')