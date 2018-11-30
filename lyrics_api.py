import requests


def lyrics(song, artist):
	song = "despacito"
	artist = "Luis Fonsi & Daddy Yankee Featuring Justin Bieber"
	key = '26cc996c835cca5e9941d0c6a77ad8d1'
	get_track = "https://api.musixmatch.com/ws/1.1/track.search?apikey=26cc996c835cca5e9941d0c6a77ad8d1&q_track={}&q_artist={}".format(song, artist)

	res = requests.get(get_track)
	res_data = res.json()
	track = res_data['message']['body']['track_list'][0]['track']

	song_info = {}

	song_info['id'] = track['track_id']
	song_info['has_lyrics'] = track['has_lyrics']
	song_info['album'] = track['album_name']
	song_info['song_name'] = track['track_name']
	song_info['artist'] = track['artist_name']
	song_info['genre'] = track['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']

	if song_info['has_lyrics'] == 1:
		get_lyrics = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey=26cc996c835cca5e9941d0c6a77ad8d1&track_id={}".format(song_info['id'])
		res = requests.get(get_lyrics)
		res_data = res.json()

		lyric = res_data['message']['body']['lyrics']

		song_info['language'] = lyric['lyrics_language_description']
		song_info['instrumental'] = lyric['instrumental']
		song_info['lyrics'] = lyric['lyrics_body'].replace("\n...\n\n******* This Lyrics is NOT for Commercial use *******", "")

	return song_info