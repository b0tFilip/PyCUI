import curses
from curses import wrapper
from curses.textpad import rectangle , Textbox

class Menu:
    def __init__(self,Lop,Lof,name,Stdscr):
        self.LOP = Lop
        self.LOF = Lof
        self.name = name
        self.stdscr = Stdscr
        curses.start_color()
        curses.init_pair(1, 55, curses.COLOR_BLACK)
        curses.init_pair(2, 160,curses.COLOR_BLACK)
        curses.init_pair(3, 27, 15)
        curses.init_pair(4, 109, 0)

    def chageLOP(self, newLOP):
        self.LOP = newLOP

    def chageLOF(self, newLOF):
      self.LOF = newLOF

    def chageName(self, newname):
        self.name = newname

    def Start(self):
        stdscr = self.stdscr
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1) 
        self.main(stdscr)
        curses.endwin()
    def main(self,stdscr):
        
        if len(self.LOP) != len(self.LOF):
            raise Exception("List of Options and List of Functions isn't the same lenght")
        Index = 0
        char = 0
        while True:
            h, w= stdscr.getmaxyx()
            box1X = 1
            box1Y = h - (len(self.LOP)+3)
            box2X = w-2
            box2Y = h-2


            rectangle(stdscr, box1Y, box1X, box2Y, box2X)
            text = "-=[ "+ self.name + " ]=-"
            textX = w//2-len(text)//2 
            stdscr.addstr(box1Y,textX, text, curses.color_pair(1))
            quit_text = " Press Q to EXIT "
            stdscr.addstr(h-2,w-len(quit_text)-2,quit_text, curses.color_pair(2))
            '''
            stdscr.addstr(1, 1, str(Index))
            stdscr.addstr(2,1,str(char))
            '''
                
            x = 0
            for Option in self.LOP:
                if Index == x:
                    stdscr.addstr(box1Y+1+x, 2, "                             ")
                    stdscr.addstr(box1Y+1+x, 2, ">" + Option,curses.color_pair(3))
                else:
                    stdscr.addstr(box1Y+1+x, 2, "                             ")
                    stdscr.addstr(box1Y+1+x, 2,Option,curses.color_pair(4))
                x = x +1

            char = stdscr.getch()
            if char == 113 or char == 81:
                break
            elif char == 259:
                if Index > 0:
                        Index = Index - 1
            elif char == 258:
                if Index <= len(self.LOP)-2:
                    Index = Index + 1
            elif char == 10:
                self.LOF[Index](stdscr)
            stdscr.refresh()
            curses.setsyx(box1Y, box1X)
        
class Choice:
    def __init__(self, Question, Ans1, Ans2, AnsFunc1, AnsFunc2, name ,Stdscr):
        self.Question = Question
        self.Ans1 = Ans1 
        self.Ans2 = Ans2
        self.AnsFunc1 = AnsFunc1
        self.AnsFunc2 = AnsFunc2
        self.name = name
        self.stdscr = Stdscr
        curses.start_color()
        curses.init_pair(1, 131, curses.COLOR_BLACK)
        curses.init_pair(2, 160,curses.COLOR_BLACK)
        curses.init_pair(3, 27, 15)
        curses.init_pair(4, 109, 0)


    def Start(self):
        stdscr = self.stdscr
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1) 
        self.main(stdscr)
        curses.endwin()

    def main(stdscr):
        h , w = stdscr.getmaxyx()
        print("Hello World!")




def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
