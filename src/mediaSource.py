import pytube
import io



yt = pytube.YouTube('https://www.youtube.com/watch?v=QlMCyVd23RU')
print(yt.streams)