from PIL import Image

class ShotCheck:

    def __init__(self, x, y):
        self.img = Image.open("img/nba_court.jpg")
        self.x = x
        self.y = y

        rgb_img = self.img.convert("RGB")
        self.rgb_values = rgb_img.getpixel((self.x, self.y))

    def GetRGB(self):
        return self.rgb_values

    def TwoOrThreePoints(self):
        if (self.rgb_values == (124, 181, 236) or self.rgb_values == (255, 135, 0)):
            return str("Three point shot")
        else:
            return str("Two point shot")
