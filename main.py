from google import genai
from google.genai import types

import PIL.Image

client = genai.Client(api_key="AIzaSyAmXGSgtKZ86LoQOJjiYP6tpJ7jojfISYY")
# from google import genai
def extract_attendance(image_path):
    image = PIL.Image.open(image_path)
    prompt = "Extract the table with Roll No, Name, Day 1, Day 2, Day 3 from this image.\
          Output in structured JSON format.\
            Mark P where a Sign is found OTHERWISE leave BLANK"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, image])


    print(response.text)

image_path = "sample1_.jpeg"
extracted_data = extract_attendance(image_path)
