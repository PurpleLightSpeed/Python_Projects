import requests

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
data = response.json()

image_url = data["message"]
image_response = requests.get(image_url)

# Save the image to your directory
with open("random_dog.jpg", "wb") as f:
    f.write(image_response.content)

print("Image saved as random_dog.jpg")

