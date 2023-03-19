from pytube import YouTube


yt = YouTube('https://youtu.be/9bZkp7q19f0')

streams = yt.streams.all()
print(streams[0])
videos = list(enumerate(streams))



title = streams[0].title
link = streams[0].resolution
for i in videos:
    print(i)

myinput = int(input("Enter Stream Number"))


streams[myinput].download()
print("Successfully Download")