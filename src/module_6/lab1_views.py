# Refer to this module's readme
import numpy as np
import csv
from PIL import Image



def main():
    with open("analysis.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=["id" ,"english_title" ,"japanese_title" ,"brightness"])

        # couldn't get this to work
        #writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"),2)
            writer.writerow(row)

            #brightness = calculate_brightness(f"{row['id']}.jpeg")
            #print(round(brightness, 2))
            '''
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),

                }
            )
            '''



def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
        return brightness

main()