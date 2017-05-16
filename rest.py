import drest

# Create a generic client api object
api = drest.API('http://localhost:8000/api/v1/')

# Make calls openly via any HTTP Method, and any path
# GET http://localhost:8000/api/v1/users/1/
response = api.make_request('GET', '/users/1/')

# Or attach a resource
api.add_resource('users')

# Get available resources
api.resources
>>> ['users', 'projects', 'etc']

# Get all objects of a resource
# GET http://localhost:8000/api/v1/users/
response = api.users.get()

# Get a single resource with primary key '1'
# GET http://localhost:8000/api/v1/users/1/
response = api.users.get(1)

# Create a resource data dictionary
user_data = dict(
    username='john.doe',
    password='oober-secure-password',
    first_name='John',
    last_name='Doe',
    )

# POST http://localhost:8000/api/v1/users/
response = api.users.post(user_data)

# Update a resource with primary key '1'
response = api.users.get(1)
updated_data = response.data.copy()
updated_data['first_name'] = 'John'
updated_data['last_name'] = 'Doe'

# PUT http://localhost:8000/api/v1/users/1/
response = api.users.put(1, updated_data)

# Patch a resource with primary key '1'
# PATCH http://localhost:8000/api/v1/users/1/
response = api.users.patch(1, dict(first_name='Johnny'))

# Delete a resource with primary key '1'
# DELETE http://localhost:8000/api/v1/users/1/
response = api.users.delete(1)

# Get the status of the request
response.status

# Or the data returned by the request
response.data

# Or the headers returned by the request
response.headers
