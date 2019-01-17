from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
import json
import asyncio
import os
import re

class GraphsBuilderConsumer(AsyncConsumer):
	
	async def websocket_connect(self, event):

		print('connection successfull', event)
		await self.send({
			'type': 'websocket.accept'
		})

	async def websocket_receive(self, event):

		fileName = event.get('text')
		fileNameJson = json.loads(fileName)
        
		f = open('files/' + fileNameJson['fileName'], 'r')
		lines = f.readlines()
		title = lines[0]
		lines = lines[1:]
		measurements = []
		for i in lines:
			if re.search(r'[0-9]+', i):
				measurements += i.split()
		f.close()

		print(event)

		# await self.send({
		# 	'type': 'websocket.send',
  #           'message': json.dumps(measurements)
  #       })

		await self.send({
			"type": "websocket.send",
			"text": json.dumps(measurements),
		})