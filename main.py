from yt_dlp import YoutubeDL


if __name__ == "__main__":
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info = ydl.extract_info("https://www.youtube.com/watch?v=5ognujPxaec&ab_channel=EnsembleG.A.P.TOKYO")