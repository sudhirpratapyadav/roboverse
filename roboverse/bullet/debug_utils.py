import pybullet as p
import numpy as np

def addLine(startPoint, endPoint, color=[255,0,0], lineWidth=1):
	lineID = p.addUserDebugLine(startPoint, endPoint, lineColorRGB=color, lineWidth=lineWidth)
	return lineID

def updateLine( replaceItemUniqueId, startPoint, endPoint, color=[255,0,0], lineWidth=1):
	lineID = p.addUserDebugLine(startPoint, endPoint, lineColorRGB=color, lineWidth=lineWidth, replaceItemUniqueId=replaceItemUniqueId)
	return lineID
