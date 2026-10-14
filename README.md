# tophat-slide-downloader
The website my professor uses to present slideshows, `app.tophat.com`, doesn't support direct image download, so saving the images from the slideshow was a huge hassle. Instead of manually saving each HTTP response as an image, I wrote this python script to somewhat automate that process. 

1) Open your browser developer tools to the network tab, preferably with the `Disable Cache` option checked. 
2) Right click on any request and select `Save all as HAR` to save the entire network stream to a HAR archive that this script can parse. 
3) launch a terminal, change to the `binary/dist/` directory and launch the `main` binary (compiled with pyinstaller). 

Alternatively, you can create your own virtual environment and install the contents of the `requirements.txt` file to run the script from source
```shell
python -m venv venv
source .venv/bin/activate

pip install -r requirements.txt
python3 main.py
```

### DISCLAIMER!!!
This script is **not** a broad-use image downloader. It is formatted specifically for the slideshows presented on the `app.tophat.com` domain, and almost certainly will not work as intended outside of those circumstances.