from dataclasses import dataclass

@dataclass
class File:
	name: str
	type: str
	size: int
	content: str
	versions: list

files = {}


def upload(data):
	if 'name' in data and data['name'] in files:
		return {'message': 'File already exists'}, 400
	file = File(**data)
	files[file.name] = file
	return {'message': 'File uploaded successfully'}, 201

def download(data):
	file = files.get(data['name'])
	if file:
		return {'file': file.__dict__}, 200
	return {'message': 'File not found'}, 404

def organize(data):
	file = files.get(data['name'])
	if file:
		file.name = data.get('new_name', file.name)
		return {'message': 'File organized successfully'}, 200
	return {'message': 'File not found'}, 404

def get_version():
	return {file.name: file.versions for file in files.values()}, 200

def update_version(data):
	file = files.get(data['name'])
	if file:
		file.versions.append(data['new_version'])
		return {'message': 'Version updated successfully'}, 200
	return {'message': 'File not found'}, 404
