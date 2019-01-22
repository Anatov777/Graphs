from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
import json
import asyncio
import os
import re

class GraphsBuilderConsumer(AsyncConsumer):
	
	async def websocket_connect(self, event):

		print('connection successfull')
		await self.send({
			'type': 'websocket.accept'
		})

		self.room_group_name = 'graphs'

        # Join room group
		await self.channel_layer.group_add(
		    self.room_group_name,
		    self.channel_name
		)

	async def websocket_receive(self, event):

		fileName = event.get('text')

		if json.loads(fileName)['addFileTrigger'] == '0' and json.loads(fileName)['delFileTrigger'] == '0':
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

			await self.send({
				"type": "websocket.send",
				"text": json.dumps(measurements)
			})

		if json.loads(fileName)['addFileTrigger'] == '1':
			fileNameJson = json.loads(fileName)['fileName']
			dic = {"action": 'addFile', "fileName": fileNameJson}
			await self.channel_layer.group_send(
	            self.room_group_name,
	            {
	                'type': 'add_file',
	                'text': json.dumps(dic)
	            }
	        )

		if json.loads(fileName)['delFileTrigger'] == '1':
			filePath = 'files/' + json.loads(fileName)['fileName']
			fileName = json.loads(fileName)['fileName']
			dic = {"action": 'delFile', "fileName": fileName}
			if os.path.isfile(filePath):
				os.remove(filePath)
			else:
				print("Error: %s file not found" % filePath)
			await self.channel_layer.group_send(
	            self.room_group_name,
	            {
	                'type': 'add_file',
	                'text': json.dumps(dic)
	            }
	        )

	async def websocket_disconnect(self, event):
		await self.send({
			'type': 'websocket.close'
		})

	async def add_file(self, event):
		await self.send({
			'type': 'websocket.send',
			'text': event['text']
		})