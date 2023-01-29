# CrowdPlated 
​
The purpose of this website is to give a platform for people to fund local, small-business restaurants. 
It allows people to support their favourite restaurant that may be on the verge of bankruptcy or help bring to life a new restaurant. 
The target audience for the project owners would be chefs/people in the restaurant industry and the target audience for the pledgers would be everyday people.
​
## Features
​
### User Accounts
​
- [X] Username
- [X] Email Address
- [X] Password
​
### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Goal
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
  - [X] Restaurant address (optional)
  - [X] Cuisine
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy 
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update - Can only do this if project is still live (end date field to be added)
  - [ ] Destroy - Can only do this if project is still live (end date field to be added)
- User
  - [X] Create
  - [X] Retrieve - includes list of pledges that the user has submitted
  - [X] Update
  - [ ] Destroy
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Limit who can create
  - [X] Limit who can retrieve (Project Detail is limited but anyone can see the project list)
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [ ] Limit who can create - anyone can create, they just need to be signed in
  - [X] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- User
  - [X] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
​
### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [X] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
## Additional features
​
- [X] Anonymous pledges
​
Anonymous pledges have been implemented - when pledges are viewed in Project Detail, anonymous pledges will not show the supporter's username so that they can't be identified.

​
### External libraries used
​
- [ ] django-filter
​
​
## Part A Submission
​
- [X] A link to the deployed project: https://crowdplated.fly.dev/projects/
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [X] Your refined API specification and Database Schema: https://docs.google.com/document/d/1i4mhFyGQLr8Q7MqKApGsHZ2hsoJpOFREvvb8B4e0YqA/edit?usp=sharing
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/create-account/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "chef",
	"email": "sarah@sarah.com",
	"password": "1234"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "chef",
	"password": "1234"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token fa2adb783526cf009d52e7271f3e5d30eb6048c2' \
  --header 'Content-Type: application/json' \
  --data '{
	"id": 4,
	"title": "Burrito",
	"description": "Asian fusion burritos",
	"goal": 150.0,
	"image": "https://via.placeholder.com/300.jpg",
	"is_open": true,
	"date_created": "2023-01-21T01:38:35.112514Z",
	"owner": 1,
	"address": "Inner West",
	"cuisine": "Mexican, Asian"
}'
```