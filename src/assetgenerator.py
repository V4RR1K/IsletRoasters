"""
Asset Generator generates the assets from the asset folder into a dictionary
Greg Lynskey
03/10/2023
"""
import pygame
import os
class assetgenerator:
    def __init__(self):
        self.asset_dictionary = dict()

    def generate_assets(self, target):
        """
        Usage: generate all assets from target asset folder
        Dictionary will have form
        :param target: name, not path, of target asset folder
        :return: dictionary of all assets from that folder
        """
        gen_asset_path = 'assets/' + target + '/'
        asset_dictionary = dict()
        for file in os.listdir(gen_asset_path):
            asset_path = os.path.join(gen_asset_path, file)
            self.asset_dictionary[file[:len(file) - 4]] = pygame.image.load(asset_path)
        print(self.asset_dictionary)
        return asset_dictionary


if __name__ == "__main__":
    ag = assetgenerator()
    ag.generate_assets("player")