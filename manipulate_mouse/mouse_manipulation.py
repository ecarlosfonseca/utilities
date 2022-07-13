from pyautogui import moveTo, click, moveRel, size
from time import sleep
from datetime import datetime as dt


def lets_procrastinate(time_in_minutes: int) -> None:
	"""Keeps the mouse moving for the specified time

	Args:
		time_in_minutes (Int): _description_
	"""
	total = time_in_minutes * 60
	while total > 0:
		print(dt.now())
		moveTo(0, 0, 2)
		moveRel(500, 500, 2)
		click(button='left')
		sleep(26)
		total -= 30

print(size())
lets_procrastinate(1)