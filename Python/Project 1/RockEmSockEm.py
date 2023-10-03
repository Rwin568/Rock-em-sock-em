import random
import tkinter as tk


class RockEmSockEm:

  def __init__(self, origin):
    self.origin = origin
    self.origin.title("Rock 'Em Sock 'Em")
    self.player_health = 100
    self.enemy_health = 100

    font = "Comic Sans MS", 30, "bold"

    self.label = tk.Label(origin,
                          text="Player Health: " + str(self.player_health) +
                          "     Enemy Health: " + str(self.enemy_health),
                          font=(font))
    self.label.pack()

    self.label2 = tk.Label(origin, text="Player's turn!", font=(font))
    self.label2.pack()

    self.punch_button = tk.Button(origin,
                                  text="Punch",
                                  command=self.player_punch,
                                  font=('Courier New', 30))
    self.punch_button.pack()

    self.block_button = tk.Button(origin,
                                  text="Block",
                                  font=('Courier New', 30))
    self.block_button.pack()

    self.player_turn = True

  def turn_switch(self):
    self.player_turn = not self.player_turn

    if self.player_turn:
        self.label2.config(text="Player's turn!", fg="black")
        self.punch_button.config(state=tk.NORMAL)
        self.block_button.config(state=tk.NORMAL)
    else:
        self.label2.config(text="Enemy's turn!", fg="black")
        self.origin.after(1000, self.enemy_punch)
        

  def player_punch(self):
    if random.random() < 0.3:
        self.label2.config(text="You missed!", fg="red")
        self.origin.after(1000, self.turn_switch)
        self.punch_button.config(state=tk.DISABLED)
        self.block_button.config(state=tk.DISABLED)
    else:
        damage = random.randint(5, 20)
        self.enemy_health -= damage
        self.label.config(text="Player Health: " + str(self.player_health) +
                          "     Enemy Health: " + str(self.enemy_health))
        self.label2.config(text="You hit!", fg="green")
        if self.enemy_health <= 0:
            self.label.config(text="Enemy has been defeated!")
            self.label2.config(text="You win!", fg="gold")
        else:
            self.punch_button.config(state=tk.DISABLED)
            self.block_button.config(state=tk.DISABLED)
            self.origin.after(1000, self.turn_switch)

  def player_block(self):
    damage = random.randint(1,10)
    self.player_health -= damage

  def enemy_punch(self):

    #action = random.choice(["punch","block"])
    #if action == "punch":
    if random.random() < 0.3:
      self.label2.config(text="The enemy missed!", fg="red")
      self.origin.after(1000, self.turn_switch)
    else:
      damage = random.randint(5, 20)
      self.player_health -= damage
      self.label.config(text="Player Health: " + str(self.player_health) +
                        "     Enemy Health: " + str(self.enemy_health))
      self.label2.config(text="Enemy hit!", fg="green")
      if self.player_health <= 0:
        self.label.config(text="Player has been defeated!")
        self.label2.config(text="You lose.", fg="red")
      else:
        self.origin.after(1000, self.turn_switch)


win = tk.Tk()
game = RockEmSockEm(win)
win.mainloop()
