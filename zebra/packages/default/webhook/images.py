import random

def getImageUrl():
	images = [
	"https://img.freepik.com/free-vector/hands-holding-microphones-recorder_24877-57103.jpg?size=338&ext=jpg https://image.freepik.com/free-vector/flat-thinking-concept_23-2148159060.jpg",
	"https://image.freepik.com/free-vector/flat-thinking-concept_23-2148163131.jpg",
	"https://image.freepik.com/free-vector/flat-thinking-concept_23-2148167780.jpg",
	"https://image.freepik.com/free-vector/worried-concept-illustration_114360-3729.jpg",
	"https://image.freepik.com/free-vector/news-concept-landing-page_52683-20699.jpg",
	"https://image.freepik.com/free-vector/news-concept-landing-page_52683-18565.jpg",
	"https://image.freepik.com/free-vector/surprised-hipster-man-pop-art-style_88138-375.jpg",
	"https://image.freepik.com/free-vector/people-using-their-mobile-phones-news_52683-39976.jpg",
	"https://image.freepik.com/free-vector/flat-design-news-concept-illustration_23-2148268773.jpg",
	"https://image.freepik.com/free-vector/news-tv-illustration_24877-57106.jpg",
	"https://image.freepik.com/free-vector/news-concept-landing-page_52683-20167.jpg",
	"https://image.freepik.com/free-vector/people-watching-breaking-news-phone_23-2148636538.jpg",
	"https://image.freepik.com/free-vector/online-news_23-2147509495.jpg",
	"https://image.freepik.com/free-vector/people-watching-breaking-news-phone_23-2148608055.jpg",
	"https://image.freepik.com/free-vector/news-concept-landing-page_52683-18629.jpg",
	"https://image.freepik.com/free-vector/people-watching-breaking-news-phone_23-2148616489.jpg",
	"https://image.freepik.com/free-vector/people-showcasing-different-types-ways-access-news_53876-66059.jpg",
	"https://image.freepik.com/free-vector/people-watching-breaking-news-phone_23-2148631651.jpg",
	"https://image.freepik.com/free-vector/people-watching-breaking-news-phone_23-2148608054.jpg",
	"https://image.freepik.com/free-vector/news-concept-landing-page_52683-20929.jpg",
	"https://image.freepik.com/free-vector/communication-elements-illustration_24877-57109.jpg",
	"https://image.freepik.com/free-vector/mass-media-news-mobile_24877-53175.jpg",
	"https://image.freepik.com/free-vector/illustration-online-news-concept_53876-28574.jpg"
	]
	url = random.choice(images)
	print("random.choice(images)", url)
	return url