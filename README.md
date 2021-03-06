# MaxBoost

### Website for boosters and gamers to connect

#### Features:
- Most hired boosters and most played games will be featured in homepage
- Users who are online will be displayed for easier networking
- Boosters will be able to choose pricing for services
- All users will have profile pages
- Lookup of users by filters such as by game or by status (online/offline)


#### Project checklists:

Home page:
- sign in feature that saves user signed in as a variable to use when loading pages
- different page look if signed in (show messages and profile buttons instead of sign in and sign up buttons)
- show name of game hyperlinked to a page about the game on top of picture in most played games feature

Sign Up page:
- add more options to hire price (per hour/level)

Play page:
- pull all users who are online and allow filtering by game, username
- row in table should consist of user's profile pic, username, game being played, level in game, average wins, time online
(will need to keep track in user model of all those fields)
- allow sorting by username, game being played, average wins, time online

Profile page:
- add average wins and levels/hour to game stats section
- add user, message user and hire (if booster) button functionalities 
- improve stat table alignment
- add feature to click on profile pic to show zoomed in version
- show settings button instead of add/message/hire buttons if profile belongs to user signed in

Hire page:
- html creation
- pull all users who are boosters to table and allow filtering by game, price range, status (online)
- allow sorting of table by times hired, price, username, game
- row in table should consist of booster's profile pic, username, games offered, times hired, price, status, and a hire button
(will need to keep track in user model of all those fields)
- hire pop up? or other page?

Messages page:
- html creation
- display list of messages where each row includes sender's profile pic, subject, date
- read, reply, delete and new message buttons

Settings page:
- design/creation

General: 
- make sure sign in form and online list load from all pages


