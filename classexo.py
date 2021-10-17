class ToolBox:
    def __init__(self):
        self.tools = []
    
    def add_tool(self,tools):
        print(" add tool")

    def remove_tool(self,tools):
        print("remove tool")



class Screwdriver:
    def __init__(self,size):
        self.size =size

    def tighten(self,screw):
        print("tight")

    def loosen(self,screw):
        print("loosen")


class Hammer:
    def __init__(self,color="red"):
        self.color=color

    def paint(self,color):
        self.color = color

    def hammer_in(self,nail):
        print("hammer in")

    def remove(self,nail):
        print("remove nail")



chose = ToolBox()

marteau = Hammer(color="bleu")
print(marteau.color)