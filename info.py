class Info():
      def __init__(self):
            self.allTerms = []
            self.topTerms = {}
            self.allSongs = []
            self.topSongs = {}

      #Search terms
      def get_allT(self):
            return self.allTerms

      def get_topT(self):
            return self.topTerms

      def set_allT(self, tArr):
            self.allTerms = tArr

      def set_topT(self, tDict):
            self.topTerms = tDict

      #Songs
      def get_allS(self):
            pass

      def get_topS(self):
            pass

      def set_allS(self, sArr):
            pass

      def set_topS(self, sDict):
            pass


s = Info()

#Search terms
def updateAllT(country, decade):
      tArr = s.get_allT()
      found = False
      for item in tArr:
            if item["Country"] == country and item["Decade"] == decade:
                  item["Count"] += 1
                  found = True
                  break
      if found == False:
            t = {"Country": country, "Decade": decade, "Count": 1}
            tArr.append(t)
      s.set_allT(tArr)

def updateTopT(country, decade):
      tArr = s.get_allT()
      tDict = s.get_topT()
      t = None

      for item in tArr:
            if item["Country"] == country and item["Decade"] == decade:
                  t = item
                  break
      
      if len(tDict) == 0:
            tDict["1"] = t
      elif len(tDict) == 1:
            if t["Country"] != tDict["1"]["Country"] or t["Decade"] != tDict["1"]["Decade"]:
                  if t["Count"] >= tDict["1"]["Count"]:
                        tDict["2"] = tDict["1"]
                        tDict["1"] = t
                  else:
                        tDict["2"] = t
      elif len(tDict) == 2:
            if (t["Country"] != tDict["1"]["Country"] or t["Decade"] != tDict["1"]["Decade"]) and (t["Country"] != tDict["2"]["Country"] or t["Decade"] != tDict["2"]["Decade"]):
                  if t["Count"] >= tDict["1"]["Count"]:
                        tDict["3"] = tDict["2"]
                        tDict["2"] = tDict["1"]
                        tDict["1"] = t
                  elif t["Count"] >= tDict["2"]["Count"]:
                        tDict["3"] = tDict["2"]
                        tDict["2"] = t
                  else:
                        tDict["3"] = t
            elif t["Country"] == tDict["2"]["Country"] and t["Decade"] == tDict["2"]["Decade"]:
                  if t["Count"] >= tDict["1"]["Count"]:
                        sec = tDict["2"]
                        tDict["2"] = tDict["1"]
                        tDict["1"] = sec 
      elif len(tDict) == 3:
            if t["Country"] == tDict["1"]["Country"] and t["Decade"] == tDict["1"]["Decade"]: #Term is 1st
                  pass
            elif t["Country"] == tDict["2"]["Country"] and t["Decade"] == tDict["2"]["Decade"]: #Term is 2nd
                  if t["Count"] >= tDict["1"]["Count"]:
                        sec = tDict["2"]
                        tDict["2"] = tDict["1"]
                        tDict["1"] = sec
            elif t["Country"] == tDict["3"]["Country"] and t["Decade"] == tDict["3"]["Decade"]:
                  if t["Count"] >= tDict["1"]["Count"]:
                        tDict["3"] = tDict["2"]
                        tDict["2"] = tDict["1"]
                        tDict["1"] = t
                  elif t["Count"] >= tDict["2"]["Count"]:
                        third = tDict["3"]
                        tDict["3"] = tDict["2"]
                        tDict["2"] = third
            else: #If country is not in dict
                  if t["Count"] >= tDict["1"]["Count"]:
                        tDict["3"] = tDict["2"]
                        tDict["2"] = tDict["1"]
                        tDict["1"] = t
                  elif t["Count"] >= tDict["2"]["Count"]:
                        tDict["3"] = tDict["2"]
                        tDict["2"] = t
                  elif t["Count"] >= tDict["3"]["Count"]:
                        tDict["3"] = t

      s.set_topT(tDict)

#Songs
def updateAllS(song, artist):
      pass

def updateTopS(song, artist):
      pass