def NULL_not_found(object: any) -> int:
	match object:
		case None:
			return (print("Nothing : None", type(object)), 0)
		case float():
			return (print("Cheese : nan", type(object)), 0)
		case 0 if not isinstance(object, bool) and isinstance(object, int):
			return (print("Zero : 0", type(object)), 0)
		case '':
			return (print("Empty:", type(object)), 0)
		case False:
			return (print("Fake: False", type(object)), 0)
	return (1)
