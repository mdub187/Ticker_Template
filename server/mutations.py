mutations = [
	{
		"get": "`${team}`[-1:].score",
		"parameters": ["leagues", "season", "team"],
		"errors": {
			"endpoint": "This endpoint does not exist.",
		},
		"results": 100,
		"response": ""
	},
	{
		"get": "`${team}`[-1:].players",
		"parameters": ["leagues", "season", "team"],
		"errors": {
			"endpoint": "This endpoint does not exist.",
		},
		"results": 50,
		"response": ""
	},
	{
		"get": "`${league}`.standings",
		"parameters": ["leagues", "season"],
		"errors": {
			"endpoint": "This endpoint does not exist.",
		},
		"results": 10,
		"response": ""
	},
	{
		"get": "`${player}`.stats",
		"parameters": ["leagues", "season", "team", "player"],
		"errors": {
			"endpoint": "This endpoint does not exist.",
		},
		"results": 1,
		"response": ""
	}
]