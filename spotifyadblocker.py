import requests
import os
import subprocess
import time

# Things you have to change

path = ''  # Locate the path of spotify.exe on your computer, It should look like : 'C:/Users/yourname/AppData/Roaming/Spotify/Spotify.exe'
SPOTIFY_ACCESS_TOKEN = ''  # Head over to the following link https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= log in and press create token after creating copy and paste it here.

# ----------------------------------------

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
	response = requests.get(
		SPOTIFY_GET_CURRENT_TRACK_URL,
		headers ={
			"Authorization"  : f'Bearer {access_token}'
		}
		)

	resp_json = response.json()

	play_type = resp_json['currently_playing_type']

	if play_type == 'ad':
		IS_AD = True
	else:
		IS_AD = False


	return IS_AD
	


def close_spotify():
	os.system(f'taskkill /F /IM Spotify.exe')

def reopen_spotify():
	subprocess.Popen(path)


def main():
	IS_AD = current_track = get_current_track(
			SPOTIFY_ACCESS_TOKEN
			)

	if IS_AD:
		print("Found an ad, restarting Spotify")

		close_spotify()

		reopen_spotify()

		time.sleep(0.1)

if __name__ == '__main__':

	while True:


		
		try:
			main()
		except:
			print('oops there was an error, head over to this link to get some help https://p2685.csb.app/')