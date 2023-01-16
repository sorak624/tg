import requests
import time
import re
import random


class poke:
    def __init__(self):
        self.json = {
            "一般": 1,
            "火": 1,
            "水": 1,
            "電": 1,
            "草": 1,
            "冰": 1,
            "格鬥": 1,
            "毒": 1,
            "地面": 1,
            "飛行": 1,
            "超能力": 1,
            "蟲": 1,
            "岩石": 1,
            "幽靈": 1,
            "龍": 1,
            "惡": 1,
            "鋼": 1,
            "妖精":1
        }
    def test1(self, def1, def2):
        newJson = self.json

        if def1 == "一般" or def2 == "一般" or def1 == "普" or def2 == "普":
            newJson["格鬥"] = newJson["格鬥"]*2
            newJson["幽靈"] = 0
        if def1 == "火" or def2 == "火":
            newJson["火"] = newJson["火"] / 2
            newJson["水"] = newJson["水"] * 2
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"] / 2
            newJson["地面"] = newJson["地面"] * 2
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"] * 2
            newJson["鋼"] = newJson["鋼"] / 2
            newJson["妖精"] = newJson["妖精"] / 2
        if def1 == "水" or def2 == "水":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"] / 2
            newJson["水"] = newJson["水"] / 2
            newJson["電"] = newJson["電"] * 2
            newJson["草"] = newJson["草"] * 2
            newJson["冰"] = newJson["冰"] / 2
            newJson["格鬥"] = newJson["格鬥"]
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"] / 2
            newJson["妖精"] = newJson["妖精"]
        if def1 == "電" or def2 == "電":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"] / 2
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"]
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"] * 2
            newJson["飛行"] = newJson["飛行"] / 2
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"] / 2
            newJson["妖精"] = newJson["妖精"]
        if def1 == "草" or def2 == "草":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"] * 2
            newJson["水"] = newJson["水"] / 2
            newJson["電"] = newJson["電"] / 2
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"] * 2
            newJson["格鬥"] = newJson["格鬥"]
            newJson["毒"] = newJson["毒"] * 2
            newJson["地面"] = newJson["地面"] / 2
            newJson["飛行"] = newJson["飛行"] * 2
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"] * 2
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"]
        if def1 == "冰" or def2 == "冰":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"] * 2
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"] / 2
            newJson["格鬥"] = newJson["格鬥"] * 2
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"] * 2
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"] * 2
            newJson["妖精"] = newJson["妖精"]
        if def1 == "格鬥" or def2 == "格鬥" or def1 == "格" or def2 == "格":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"]
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"] * 2
            newJson["超能力"] = newJson["超能力"] * 2
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"] / 2
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"] / 2
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"] * 2
        if def1 == "毒" or def2 == "毒":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"] / 2
            newJson["毒"] = newJson["毒"] / 2
            newJson["地面"] = newJson["地面"] * 2
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"] * 2
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"] / 2
        if def1 == "地面" or def2 == "地面" or def1 == "地" or def2 == "地":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"] * 2
            newJson["電"] = 0
            newJson["草"] = newJson["草"] * 2
            newJson["冰"] = newJson["冰"] * 2
            newJson["格鬥"] = newJson["格鬥"]
            newJson["毒"] = newJson["毒"] / 2
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"] / 2
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"]
        if def1 == "飛行" or def2 == "飛行" or def1 == "飛" or def2 == "飛":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"] * 2
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"] * 2
            newJson["格鬥"] = newJson["格鬥"] / 2
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = 0
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"] * 2
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"]
        if def1 == "超能力" or def2 == "超能力" or def1 == "超" or def2 == "超":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"] / 2
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"] / 2
            newJson["蟲"] = newJson["蟲"] * 2
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"] * 2
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"] * 2
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"]
        if def1 == "蟲" or def2 == "蟲":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"] * 2
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"] / 2
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"] / 2
            newJson["飛行"] = newJson["飛行"] * 2
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"] * 2
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"]
        if def1 == "岩石" or def2 == "岩石" or def1 == "岩" or def2 == "岩":
            newJson["一般"] = newJson["一般"] / 2
            newJson["火"] = newJson["火"] / 2
            newJson["水"] = newJson["水"] * 2
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"] * 2
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"] * 2
            newJson["毒"] = newJson["毒"] / 2
            newJson["地面"] = newJson["地面"] * 2
            newJson["飛行"] = newJson["飛行"] / 2
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"] * 2
            newJson["妖精"] = newJson["妖精"]
        if def1 == "幽靈" or def2 == "幽靈" or def1 == "鬼" or def2 == "鬼":
            newJson["一般"] = 0
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = 0
            newJson["毒"] = newJson["毒"] / 2
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"] * 2
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"] * 2
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"]
        if def1 == "龍" or def2 == "龍":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"] / 2
            newJson["水"] = newJson["水"] / 2
            newJson["電"] = newJson["電"] / 2
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"] * 2
            newJson["格鬥"] = newJson["格鬥"]
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"]
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"] * 2
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"] * 2
        if def1 == "惡" or def2 == "惡":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"] * 2
            newJson["毒"] = newJson["毒"]
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = 0
            newJson["蟲"] = newJson["蟲"] * 2
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"] / 2
            newJson["龍"] = newJson["龍"]
            newJson["惡"] = newJson["惡"] / 2
            newJson["鋼"] = newJson["鋼"]
            newJson["妖精"] = newJson["妖精"] * 2
        if def1 == "鋼" or def2 == "鋼":
            newJson["一般"] = newJson["一般"] / 2
            newJson["火"] = newJson["火"] * 2
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"] / 2
            newJson["冰"] = newJson["冰"] / 2
            newJson["格鬥"] = newJson["格鬥"] * 2
            newJson["毒"] = 0
            newJson["地面"] = newJson["地面"] * 2
            newJson["飛行"] = newJson["飛行"] / 2
            newJson["超能力"] = newJson["超能力"] / 2
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"] / 2
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = newJson["龍"] / 2
            newJson["惡"] = newJson["惡"]
            newJson["鋼"] = newJson["鋼"] / 2
            newJson["妖精"] = newJson["妖精"] / 2
        if def1 == "妖精" or def2 == "妖精" or def1 == "妖" or def2 == "妖":
            newJson["一般"] = newJson["一般"]
            newJson["火"] = newJson["火"]
            newJson["水"] = newJson["水"]
            newJson["電"] = newJson["電"]
            newJson["草"] = newJson["草"]
            newJson["冰"] = newJson["冰"]
            newJson["格鬥"] = newJson["格鬥"] / 2
            newJson["毒"] = newJson["毒"] * 2
            newJson["地面"] = newJson["地面"]
            newJson["飛行"] = newJson["飛行"]
            newJson["超能力"] = newJson["超能力"]
            newJson["蟲"] = newJson["蟲"] / 2
            newJson["岩石"] = newJson["岩石"]
            newJson["幽靈"] = newJson["幽靈"]
            newJson["龍"] = 0
            newJson["惡"] = newJson["惡"] / 2
            newJson["鋼"] = newJson["鋼"] * 2
            newJson["妖精"] = newJson["妖精"]

        return newJson

    def result(self, def1, def2=None):
        newJson = poke().test1(def1, def2)
        lst = {}
        lst2 = {}
        lst3 = {}
        lst4 = {}
        lst5 = {}
        for k, v in newJson.items():
            if v != 1:
                if k == "一般":
                    k = "普"
                if k == "格鬥":
                    k = "格"
                if k == "超能力":
                    k = "超"
                if k == "岩石":
                    k = "岩"
                if k == "飛行":
                    k = "飛"
                if k == "地面":
                    k = "地"
                if k == "幽靈":
                    k = "鬼"
                if k == "妖精":
                    k = "妖"
                if v == 0:
                    lst[k] = v
                elif v == 0.25:
                    lst2[k] = v
                elif v == 0.5:
                    lst3[k] = v
                elif v == 2:
                    lst4[k] = v
                elif v == 4:
                    lst5[k] = v

        text1 = '\n'.join(f'{key}: {value}' for key, value in lst.items())
        text2 = '\n'.join(f'{key}: {value}' for key, value in lst2.items())
        text3 = '\n'.join(f'{key}: {value}' for key, value in lst3.items())
        text4 = '\n'.join(f'{key}: {value}' for key, value in lst4.items())
        text5 = '\n'.join(f'{key}: {value}' for key, value in lst5.items())

        text = f'無效:\n{text1}\n\n唔怕(1/4):\n{text2}\n\n唔怕(1/2):\n{text3}\n\n怕(2倍):\n{text4}\n\n怕(4倍):\n{text5}'
        print(text)
        return text

# Poke = poke()
# Poke.result(def1="火")