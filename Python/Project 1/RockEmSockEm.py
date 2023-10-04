import random
import tkinter as tk


class RockEmSockEm:

  def __init__(self, origin):
    self.origin = origin
    self.origin.title("Rock 'Em Sock 'Em")
    self.player_health = 100
    self.enemy_health = 100
    self.player_turn = True
    self.player_action = None
    self.enemy_blocked = False
    self.p_last_action = None
    self.e_last_action = None

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
                                  command=self.player_block,
                                  font=('Courier New', 30))
    self.block_button.pack()

  def turn_switch(self):
    self.player_turn = not self.player_turn

    if self.player_turn:
      self.label2.config(text="Player's turn!", fg="black")
      self.punch_button.config(state=tk.NORMAL)
      self.block_button.config(state=tk.NORMAL)

    else:
      self.label2.config(text="Enemy's turn!", fg="black")
      self.origin.after(1000, self.enemy_action)

  def player_punch(self):
    if random.random() < 0.3:
      self.label2.config(text="You missed!", fg="red")
      self.p_last_action == "punch"
    else:
      self.player_action = "punch"
      self.p_last_action = "punch"
      if self.enemy_blocked:
        if random.random() < 0.5:  # chance to block some damage
          damage = random.randint(1, 10)
          self.enemy_health -= damage
          self.label2.config(text="Enemy has blocked some damage!", fg="green")
        else:
          self.label2.config(text="Enemy has blocked all damage!", fg="green")
          self.enemy_blocked = False
      else:
        damage = random.randint(5, 20)
        self.enemy_health -= damage
        self.label.config(text="Player Health: " + str(self.player_health) +
                          "     Enemy Health: " + str(self.enemy_health))
        self.label2.config(text="You hit!", fg="green")
        if self.enemy_health <= 0:
          self.label.config(text="Enemy has been defeated!")
          self.label2.config(text="You win!", fg="gold")

    self.punch_button.config(state=tk.DISABLED)
    self.block_button.config(state=tk.DISABLED)
    self.origin.after(1000, self.turn_switch)

  def player_block(self):
    if self.p_last_action == "block":
      self.label2.config(text="You can't block two turns in a row!", fg="red")
      self.punch_button.config(state=tk.NORMAL)
      self.block_button.config(state=tk.DISABLED)
      return
    elif random.random() < 0.7:
      self.player_action = 'block'
      self.p_last_action = 'block'
      self.label2.config(text="You successfully blocked!", fg="green")
    else:
      self.player_action = None
      self.label2.config(text="You tried to block, but failed!", fg="red")

    self.punch_button.config(state=tk.DISABLED)
    self.block_button.config(state=tk.DISABLED)
    self.origin.after(1000, self.turn_switch)

  def enemy_action(self):
    if self.e_last_action != 'block':
      if random.random() < 0.3:  # chance to miss punch
        self.label2.config(text="The enemy missed!", fg="red")
        self.p_last_action == "punch"
      else:
        if self.player_action == "block":
          if random.random() < 0.5:  # chance to block some damage
            damage = random.randint(1, 10)
            self.player_health -= damage
            self.label2.config(text="You blocked some damage!", fg="green")
          else:
            self.label2.config(text="You blocked all damage!", fg="green")
          self.player_action = None
        else:
          damage = random.randint(5, 20)
          self.player_health -= damage
          self.label.config(text="Player Health: " + str(self.player_health) +
                            "     Enemy Health: " + str(self.enemy_health))
          self.label2.config(text="Enemy hit!", fg="green")
          if self.player_health <= 0:
            self.label.config(text="Player has been defeated!")
            self.label2.config(text="You lose.", fg="red")
      self.e_last_action = 'punch'
    else:
      if random.random() < 0.7:
        self.enemy_blocked = True
        self.label2.config(text="Enemy has successfully blocked!", fg="green")
      else:
        self.label2.config(text="Enemy tried to block, but failed!", fg="red")
      self.e_last_action = 'block'

    self.origin.after(1000, self.turn_switch)


win = tk.Tk()
game = RockEmSockEm(win)
win.mainloop()
