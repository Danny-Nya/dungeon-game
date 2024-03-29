import typing
from typing import List

from enums.Action import Action
from view import Utils

import pygame
from assets.button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
img = pygame.image.load("assets/Hero.png").convert_alpha()

def get_font(size):  # Returns Press-Start-2P in the desired size
	return pygame.font.Font("assets/font.ttf", size)

if typing.TYPE_CHECKING:
	from logic.fighter.Player import Player
	from controller.Game import Game


class CombatView:

	def __init__(self, game: 'Game', player: 'Player', monsterName: str):
		self.player = player
		self.monsterName = monsterName
		self.game = game

	def fight(self) -> None:
		print(self.monsterName, " has appeared!\n")

		while not self.game.currentMonsterIsDead():
			while True:
					SCREEN.blit(BG, (0, 0))
					SCREEN.blit(img, (10, 10))
					MENU_MOUSE_POS = pygame.mouse.get_pos()

					MENU_TEXT = get_font(10).render('{} is attacking!'.format(self.monsterName), True, "#b68f40")
					MENU_RECT = MENU_TEXT.get_rect(center=(250, 600))

					SCREEN.blit(MENU_TEXT, MENU_RECT)
					pygame.display.update()
			print('{} is attacking!'.format(self.monsterName))
			print(self.game.currentMonsterAttackPlayer())
			input("Press any key to continue...")
			Utils.clear()
			self.playerTurn()
			input("Press any key to continue...")
			Utils.clear()

	def playerTurn(self) -> None:
		print(self.player)
		self.displayMenu()

	def displayMenu(self) -> None:
		action = self.enterValidAction()
		print('\n')

		if action == Action.ATTACK:
			print(self.game.playerAttackCurrentMonster())
		elif action == Action.HEAL:
			print(self.player.name + ' self heals.')
			self.player.selfHeal()
		elif action == Action.QUIT:
			print(self.player.name + ' abandons game. See you soon!')
			exit()

	def enterValidAction(self) -> Action:
		while True:
			actionList: List[Action] = [action for action in Action]
			for action in actionList:
				print(action, "): ", action.description())
			try:
				userAction = Action.strToAction(input(" -> Enter an action: "))
			except ValueError:
				print("Not a valid action")
			else:
				return userAction
