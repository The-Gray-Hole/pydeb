import os
import shutil

import yaml
from .debian import render_build
from .conf import config


def main():
    conf = config()
    if conf.action == "build":
        with open(conf.pydeb_file, "r") as f:
            kwargs = yaml.load(f, Loader=yaml.FullLoader)
        pack_name = os.getcwd().split("/")[-1]
        kwargs["pydeb"]["package-name"] = pack_name
        deb_files_dir = "debian-files"
        kwargs["debian-files"] = deb_files_dir
        render_build(kwargs)
        os.system("chmod +x ./builder.sh")
        os.system("./builder.sh")
        os.system("rm *.deb")
        os.system("debuild -b -us -uc")
        os.system(f"mv ../{pack_name}*.deb ./")
        os.system(f"rm ../{pack_name}*.build ../{pack_name}*.buildinfo ../{pack_name}*.changes ./builder.sh")
        shutil.rmtree("debian")
        shutil.rmtree(deb_files_dir)
