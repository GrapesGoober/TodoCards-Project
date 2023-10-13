# TodoCards-Project
A university project for building an application

Members:
- Nachat Kaewmeesang 6422770774
- Panisara Srisan 6422781326
- Praewaphun Sukmark 6422790046

# To run this
- Installation:
  - python & flask (`pip install Flask`)
  - node `https://nodejs.org/en` (i think you shoud go for LTS)
  
- Run Python backend
  - `cd TodoCards-BackEnd`
  - `python app.py` (or just hit the play button)
- Run Svelte front end
  - `cd TodoCards-FrontEnd`
  - `npm run dev`
  - you should see a nice localhost popped up. click on it


# Description:

A “to-do” app called “TodoCard”, where each to-do items are encapsulated as “cards” organized under “decks”. The basic ideas are as follows
- app can have multiple decks
- where each decks can have zero or more cards.
- Each card can have one or more subcards
- Each card contains info, such as
  - Name, description, created date, deadline, etc
  - isdone boolean attribute
- Each subcard contains info such as
  - Name, description,  deadline
