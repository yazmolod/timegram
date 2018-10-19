from InstagramAPI import InstagramAPI

ig = InstagramAPI('yazmolod', 'SgAsU2014')
file_path = 'tmp.jpg'

def DoMagic(caption):
	ig.uploadPhoto(file_path, caption=caption)