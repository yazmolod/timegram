from InstagramAPI import InstagramAPI

ig = InstagramAPI('yazmolod', 'SgAsU2014')
file_path = 'static/maxresdefault.jpg'
caption = 'Something happened'

def DoMagic():
	ig.uploadPhoto(file_path, caption=caption)