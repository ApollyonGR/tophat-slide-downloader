import base64, os, json, shutil
from haralyzer import HarParser
from tkinter import filedialog, messagebox, Tk

# Establishes and hides the root tkinter window
root = Tk()
root.withdraw()

# File picker dialog menu
filePath = filedialog.askopenfilename(
    title="Select a HAR Archive",
    filetypes=[("HAR Archives", "*.har")]
)
cwd = os.getcwd()
outputDir = "extractedImages"

# deletes the current extractedImages directory if it exists 
try:
    shutil.rmtree(outputDir)
except:
    print(f"{outputDir} directory not found, assuming it doesn't exist")

# Makes the directory for the images to be outputted
os.makedirs(outputDir, exist_ok=True )

with open(filePath, "r") as file:
    parser = HarParser(json.loads(file.read()))
    for page in parser.pages:  
        for entry in page.entries: 
            if parser.match_headers(entry, "response", "Content-Type", "image/jpeg" ): 
                imageURL = (f"{entry.response}")
                imageURLSplit = imageURL.split("/", 5) # Splits the URL into 6 pieces seperated by /
                imageName = imageURLSplit[5] # Grabs the final split. In this instance, it will be "slide-**.jpg"
                imagePath = os.path.join(outputDir, imageName) # Concats the outputDir and the imageName

                # Decodes the base64 encoded image
                base64ImageBytes = base64.b64decode(entry.response.text)

                # Writes the decoded bytes directly to a file
                with open(imagePath, "wb") as fh:
                    fh.write(base64ImageBytes)
    
    print(f"Slides saved to {cwd}/{outputDir}")
