import pytube
import io



yt = pytube.YouTube('https://www.youtube.com/watch?v=QlMCyVd23RU')
stream = yt.streams.get_by_itag(251)
stream.download(filename="play.webm", output_path="./src/media")