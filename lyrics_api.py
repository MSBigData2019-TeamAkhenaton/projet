import requests
from random import randint


def lyrics(song, artist):
	keys = [
		'bffd099744c5812617813de69b93e2b0',
		'16fce98709ab0cfda3d679a5a80d00aa',
		'f65d821196427016661d6b80ce5bb2c9',
		'911c39f720d7825fb2de2a98fe8905c1',
		'591e236d68f408f61e6c7019bba857ac'
	]
	ind = randint(0, 4)
	key = keys[ind]
	#key = '26cc996c835cca5e9941d0c6a77ad8d1'
	get_track = "https://api.musixmatch.com/ws/1.1/track.search?apikey={}&q_track={}&q_artist={}&f_has_lyrics=1&s_track_rating=desc".format(key, song, artist)

	res = requests.get(get_track)
	res_data = res.json()
	song_info = {}
	try:
		track = res_data['message']['body']['track_list'][0]['track']

		song_info['id'] = track['track_id']
		song_info['has_lyrics'] = track['has_lyrics']
		song_info['album'] = track['album_name']
		song_info['song_name'] = track['track_name']
		song_info['artist'] = track['artist_name']
		song_info['genre'] = track['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']

		get_lyrics = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey={}&track_id={}".format(key, song_info['id'])
		res = requests.get(get_lyrics)
		res_data = res.json()

		lyric = res_data['message']['body']['lyrics']

		song_info['language'] = lyric['lyrics_language_description']
		song_info['instrumental'] = lyric['instrumental']
		song_info['lyrics'] = lyric['lyrics_body'].replace("\n...\n\n******* This Lyrics is NOT for Commercial use *******", "")

	except:
		song_info['id'] = ""
		song_info['has_lyrics'] = ""
		song_info['album'] = ""
		song_info['song_name'] = ""
		song_info['artist'] = ""
		song_info['genre'] = ""
		song_info['language'] = ""
		song_info['instrumental'] = ""
		song_info['lyrics'] = ""

	return song_info