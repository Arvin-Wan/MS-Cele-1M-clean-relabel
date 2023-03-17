# MS-Celeb-1M clean

You can download the torrent of raw dataset from this [https://academictorrents.com/details/9e67eb7cc23c9417f39778a8e06cca5e26196a97/tech&hit=1&filelist=1]


## Requirements(ubuntu)
 ``` sh
 # For decompressing .torrent file
sudo apt-get install transmission-cli

# For decompressing .7z file
sudo apt-get install p7zip-full 

 # python package
 pip install tqdm
 ```


 ## Procedure

 1. Decompression

``` sh
unzip MS-Celeb-1M_clean_list.zip

7z x clean_list.7z

# The step will take a long time.
# It toke me a day approximately
transmission-cli MS-Celeb-1M.torrent
```

2. Modification the path in .py file

3. Run
```sh
python process.py
```