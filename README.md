# Player Stat Machine Learning Application / Website

In-depth player stat predictor using machine learning to predict stats based on
player data, coaches, weather, etc.

# To-Do

- [ ] Everything
- [x] Testing format
- [ ] Web Scrapper
- [ ] Class set up and initialization
- [ ] Code file structure set up
- [ ] Find machine learning libary (Terraflow)
- [ ] Intialize database to hold stats
- [ ] Classes and hierarchy decided and decided
- [ ] React site / app setup

# **Planning and Notes**

## Stats needed to calculate

- Rushing / Passing Yards
- Rushing / Passing attempts
- Touchdowns
- The defense ranks for passing and rushing (previous game/season yards allowed)
- CB1 vs WR
- Defensive coordinator vs QB overall stats
- Save stats by game not season
- Note team played for to account for changing teams
- Check stats for previous games against specific team

## Stats/variables to account for

- Players Switching to new teams
  - variable for team and time spent with team?
    - Linked to team class object?
- Number of snaps played per game (similar to ERA in baseball maybe)
- Weather (Snow games, rain games, etc) if possible
- Indoor vs outdoor QB performace (some QBs are terrible outdoor but their team has an indoor stadium)

## **Object Classes**

### Team Class

- Current Coaches or all coaches (?)
- Overall team stats for the season
  - Offensive rushing
  - Defensive rushing
  - offensive passing
  - defensive passing
    - DB rank
    - D-line rank
- Current players or all players (?)

### Coach class

- offensive / defensive
- offense
  - Offensive ranked
    - Overall
    - Passing
    - Rushing
  - Passing yards
  - passing attempts
  - Passing TDs
  - Rushing yards
  - Rushing attempts
- defense
  - defensive rank
    - overall
    - passing
    - rushing
  - Tds allowed
  - defensive line rank
  - DBs rank
  - passing yards allowed
  - passing yards allowed
  - passing attempts allowed
  - passing touchdowns
  - rushing yards allowed
  - rushing tds allowed
  - previous game stats against QB

## Important Links:

-
