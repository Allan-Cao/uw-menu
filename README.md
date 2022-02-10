
# UW Menu

Do you want to know what is on the menu at your favourite cafeteria?
Look no further! UW Menu parses the UW Food Services website to get daily updates on what is on the menu at all of the UW Food Service locations!


## Installation



```bash
  git clone https://github.com/Allan-Cao/uw-menu.git
  cd uw-menu
  python -m pip install bs4
```
    
## Development

To work on this project, please use branches named by the feature you are working on.
If you would like to work on a specific aspect alone, please add some idenitifier to your branch name.

Example branching

```bash
  git pull origin
  git checkout origin
  git checkout -b newfeature/acao
```

Please commit with the feature name, colon, then a title for commits.
An example PR creation is shown below

```bash
  git status
  git add menu.py
  git commit
  git push
  git push --set-upstream origin <branch-name>
```
## Roadmap

- Use OOP to create a class for the menu instead of using a list

- Integrate with a discord bot

- Store future menus and search for certain items

- Use NLP to figure out what is being served (to aid in searching)

- Integrate a review system with the discord bot to be able to review foods and lookup menu options by review



## Disclaimer

UW Menu is not affiliated with the University of Waterloo or UW Food Services in any way.

## License

[MIT](https://choosealicense.com/licenses/mit/)

