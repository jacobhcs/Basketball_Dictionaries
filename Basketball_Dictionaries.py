# OBJECT/CLASS
class Player: # First letter must be capitalized when creating classes name.
    newer_team = []
    # Changing the constructor to use a DICTIONARY instead of passing in argument value individually.
    def __init__(self, player_dict): # CONSTRUCTOR/INITIALIZER. DUNDERSCORE.
        # ATTRIBUTES/BASICALLY VARIABLES
        self.name = player_dict["name"] # Bracket Notation to reference dictionary from parameter.
        self.age = player_dict["age"] # Must use quotations the reference the "KEY".
        self.position = player_dict["position"]
        self.team = player_dict["team"]
        self.whole = str(player_dict) # Using str method to covert DICTIONARY to STRING type.
    # Creating string representation of an object. Instead of printing OBJECTS/INSTANCES MEMORY ADDRESS.
    def __repr__(self) -> str:
        return self.whole
    
    @classmethod
    def get_team(cls, team_list):
        for player_dict in team_list:
            player = cls(player_dict)
            cls.newer_team.append(player)
        return cls.newer_team

# DICTIONARIES that will passed as an argument into the OBJECT/CLASS CONSTRUCTOR.

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

# CREATE INSTANCES/OBJECTS. MUST BE INSTANTIATED outside the teh class definition, OUTER SCOPE
player_kevin = Player(kevin) # Passing in arguments by accessing DICT form LIST using index values.
player_jason = Player(jason)
player_kyrie = Player(kyrie)
# # Printing the value of the name from the INSTANCES/OBJECTS.
# print("PLAYER NAMES:")
# print(player_kevin.name)
# print(player_kyrie.name)
# print(player_jason.name)
# print("*"*30)
# # Printing the MEMORY ADDRESSES of the INSTANCES/OBJECTS
# print("These are the MEMORY ADDRESSES of our OBJECTS/INSTANCES:")
# print(player_jason)
# print(player_kyrie)
# print(player_kevin)

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# Prints all instances of the Player class on the outside scope using a for loop.
# new_team = []
# for player_dict in players:
#     player = Player(player_dict)
#     new_team.append(player)
# print(new_team)

# Prints all instances using class method in the innner Player class scope.
print(Player.get_team(players))
# print(player_kevin)