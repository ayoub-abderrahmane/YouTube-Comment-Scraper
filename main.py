from googleapiclient.discovery import build

def get_video_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Récupérer les commentaires de la vidéo spécifiée
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    comments = []

    # Parcourir les commentaires récupérés
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments


video_id = 'T0DmHRdtqY0' # Entrez l'ID que l'on peut retrouver à la fin du lien de la vidéo YouTube
api_key = 'AIzaSyC13US4vwVVPl3vXg3F3WXKBmL9-jgtu5E' # Entrez la clé d'API

comments = get_video_comments(video_id, api_key)

for comment in comments:
    print(comment)