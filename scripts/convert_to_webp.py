from PIL import Image
from pathlib import Path

paths = Path("C:\Git\SquadMaps\img\maps\\thumbnails\\").glob("**/*.jpg")
for path in paths:
    print(path)
    image = Image.open(path)
    image.save('C:\Git\SquadMaps\img\maps\webp\\'+path.stem+'.webp', format="webp")
