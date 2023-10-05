import random
import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

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

    script_dir = os.path.dirname(os.path.abspath(__file__))
    self.image_default = Image.open(os.path.join(script_dir, "images/idle.png"))
    self.image_pla_att = Image.open(os.path.join(script_dir, "images/platt.png"))
    self.image_pla_blo = Image.open(os.path.join(script_dir, "images/plblo.png"))
    self.image_pla_mis = Image.open(os.path.join(script_dir, "images/plmiss.png"))
    self.image_pla_ko = Image.open(os.path.join(script_dir, "images/plko.png"))
    self.image_ene_att = Image.open(os.path.join(script_dir, "images/enatt.png"))
    self.image_ene_blo = Image.open(os.path.join(script_dir, "images/enblo.png"))
    self.image_ene_mis = Image.open(os.path.join(script_dir, "images/enmiss.png"))
    self.image_ene_ko = Image.open(os.path.join(script_dir, "images/enko.png"))

    self.resize_images()

    self.image_default = ImageTk.PhotoImage(self.image_default)
    self.image_pla_att = ImageTk.PhotoImage(self.image_pla_att)
    self.image_pla_blo = ImageTk.PhotoImage(self.image_pla_blo)
    self.image_pla_mis = ImageTk.PhotoImage(self.image_pla_mis)
    self.image_pla_ko = ImageTk.PhotoImage(self.image_pla_ko)
    self.image_ene_att = ImageTk.PhotoImage(self.image_ene_att)
    self.image_ene_blo = ImageTk.PhotoImage(self.image_ene_blo)
    self.image_ene_mis = ImageTk.PhotoImage(self.image_ene_mis)
    self.image_ene_ko = ImageTk.PhotoImage(self.image_ene_ko)

    font = "Comic Sans MS", 30, "bold"

    self.health = tk.Label(origin,
                           text="Player Health: " + str(self.player_health) +
                           "     Enemy Health: " + str(self.enemy_health),
                           font=(font))
    self.health.pack()

    self.image_label = tk.Label(origin, image=self.image_default)
    self.image_label.pack()

    self.turnmsg = tk.Label(origin, text="Player's turn!", font=(font))
    self.turnmsg.pack()

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

    self.retry_button = tk.Button(origin,
                                  text="Retry",
                                  command=self.retry_game,
                                  font=('Courier New', 30))
    self.retry_button.pack()
    self.retry_button.forget()

  def resize_images(self):
    width = 576
    height = 324

    self.image_default = self.image_default.resize((width, height) )
    self.image_pla_att = self.image_pla_att.resize((width, height) )
    self.image_pla_blo = self.image_pla_blo.resize((width, height) )
    self.image_pla_mis = self.image_pla_mis.resize((width, height) )
    self.image_pla_ko = self.image_pla_ko.resize((width, height) )
    self.image_ene_att = self.image_ene_att.resize((width, height) )
    self.image_ene_blo = self.image_ene_blo.resize((width, height) )
    self.image_ene_mis = self.image_ene_mis.resize((width, height) )
    self.image_ene_ko = self.image_ene_ko.resize((width, height) )

  def show_retry_button(self):
    self.punch_button.forget()
    self.block_button.forget()
    self.retry_button.pack()

  def retry_game(self):
    self.player_health = 100
    self.enemy_health = 100
    self.player_turn = True
    self.player_action = None
    self.enemy_blocked = False
    self.p_last_action = None
    self.e_last_action = None
    self.image_label.configure(image=self.image_default)

    self.health.config(text="Player Health: " + str(self.player_health) +
                       "     Enemy Health: " + str(self.enemy_health))
    self.turnmsg.config(text="Player's turn!", fg="black")
    self.punch_button.pack()
    self.block_button.pack()
    self.retry_button.forget()

  def turn_switch(self):
    self.player_turn = not self.player_turn

    if self.player_turn:
      self.turnmsg.config(text="Player's turn!", fg="black")
      self.punch_button.config(state=tk.NORMAL)
      self.block_button.config(state=tk.NORMAL)

    else:
      self.turnmsg.config(text="Enemy's turn!", fg="black")
      self.origin.after(1000, self.enemy_action)

  def player_punch(self):
    if random.random() < 0.3:
      self.turnmsg.config(text="You missed!", fg="red")
      self.image_label.configure(image=self.image_pla_mis)
      self.p_last_action = "punch"
    else:
      self.player_action = "punch"
      self.p_last_action = "punch"
      if self.enemy_blocked:
        if random.random() < 0.5:  # chance to block some damage
          damage = random.randint(1, 10)
          self.enemy_health -= damage
          self.turnmsg.config(text="Enemy has blocked some damage!",
                              fg="green")
        else:
          self.turnmsg.config(text="Enemy has blocked all damage!", fg="green")
        self.image_label.configure(image=self.image_ene_blo)
        self.enemy_blocked = False
      else:
        damage = random.randint(5, 20)
        self.enemy_health -= damage
        self.health.config(text="Player Health: " + str(self.player_health) +
                           "     Enemy Health: " + str(self.enemy_health))
        self.turnmsg.config(text="You hit!", fg="green")
        self.image_label.configure(image=self.image_pla_att)
        if self.enemy_health <= 0:
          self.health.config(text="Enemy has been defeated!")
          self.image_label.configure(image=self.image_ene_ko)
          self.turnmsg.config(text="You win!", fg="gold")
          self.show_retry_button()
          return

    self.punch_button.config(state=tk.DISABLED)
    self.block_button.config(state=tk.DISABLED)
    self.origin.after(1000, self.turn_switch)

  def player_block(self):
    if self.p_last_action == "block":
      self.turnmsg.config(text="You can't block two turns in a row!", fg="red")
      self.punch_button.config(state=tk.NORMAL)
      self.block_button.config(state=tk.DISABLED)
      return
    elif random.random() < 0.7:
      self.player_action = 'block'
      self.p_last_action = 'block'
      self.turnmsg.config(text="You successfully blocked!", fg="green")
    else:
      self.player_action = None
      self.turnmsg.config(text="You tried to block, but failed!", fg="red")

    self.punch_button.config(state=tk.DISABLED)
    self.block_button.config(state=tk.DISABLED)
    self.origin.after(1000, self.turn_switch)

  def enemy_action(self):
    if random.random() < 0.7:  #block or punch
      if random.random() < 0.3:  # chance to miss punch
        self.turnmsg.config(text="The enemy missed!", fg="red")
        self.image_label.configure(image=self.image_ene_mis)
        self.e_last_action = "punch"
      else:
        if self.player_action == "block":
          if random.random() < 0.5:  # chance to block some damage
            damage = random.randint(1, 10)
            self.player_health -= damage
            self.turnmsg.config(text="You blocked some damage!", fg="green")
            self.health.config(text="Player Health: " +
                               str(self.player_health) +
                               "     Enemy Health: " + str(self.enemy_health))
          else:
            self.turnmsg.config(text="You blocked all damage!", fg="green")
          self.player_action = None
          self.image_label.configure(image=self.image_pla_blo)
        else:
          damage = random.randint(5, 20)
          self.player_health -= damage
          self.health.config(text="Player Health: " + str(self.player_health) +
                             "     Enemy Health: " + str(self.enemy_health))
          self.turnmsg.config(text="Enemy hit!", fg="green")
          self.image_label.configure(image=self.image_ene_att)
          if self.player_health <= 0:
            self.health.config(text="Player has been defeated!")
            self.image_label.configure(image=self.image_pla_ko)
            self.turnmsg.config(text="You lose.", fg="red")
            self.show_retry_button()
            return
        self.e_last_action = 'punch'
    else:
      if self.e_last_action == "block":
        if random.random() < 0.3:  # chance to miss punch
          self.turnmsg.config(text="The enemy missed!", fg="red")
          self.image_label.configure(image=self.image_ene_mis)
          self.e_last_action = "punch"
        else:
          if self.player_action == "block":
            if random.random() < 0.5:  # chance to block some damage
              damage = random.randint(1, 10)
              self.player_health -= damage
              self.turnmsg.config(text="You blocked some damage!", fg="green")
            else:
              self.turnmsg.config(text="You blocked all damage!", fg="green")
            self.player_action = None
            self.image_label.configure(image=self.image_pla_blo)
          else:
            damage = random.randint(5, 20)
            self.player_health -= damage
            self.health.config(text="Player Health: " +
                               str(self.player_health) +
                               "     Enemy Health: " + str(self.enemy_health))
            self.image_label.configure(image=self.image_ene_att)
            self.turnmsg.config(text="Enemy hit!", fg="green")
            if self.player_health <= 0:
              self.health.config(text="Player has been defeated!")
              self.image_label.configure(image=self.image_pla_ko)
              self.turnmsg.config(text="You lose.", fg="red")
              self.show_retry_button()
              return
        self.e_last_action = 'punch'
      else:
        if random.random() < 0.7:
            self.enemy_blocked = True
            self.turnmsg.config(text="Enemy has successfully blocked!",
                              fg="green")
        else:
          self.turnmsg.config(text="Enemy tried to block, but failed!",
                              fg="red")
        self.e_last_action = 'block'

    self.origin.after(1000, self.turn_switch)


win = tk.Tk()
game = RockEmSockEm(win)
win.mainloop()
