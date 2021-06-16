x = input()
match x:
	case "hello" | "hi" as greeting:
		print(f"hi to your {greeting}")
	case "bye":
		print("bye")
	case _ as y:
		print(f"what is {y}")

