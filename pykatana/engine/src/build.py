#
# بسم الله الرحمن الرحیم
# اللهم صل علی محمد و آل محمد
# ---------------------------
# Created by pykatana
#
# pykatana:
# Copyright (c) 2024 Abolfazl Danayi
# adanayidet@gmail.com
#

from pykatana import EZJinja

def build(engine: EZJinja):
    # Copy the static folder
    engine.copy_static_folder(exclude_extensions=["scss"])

    # Export templates
    engine.export_template("index.html")
