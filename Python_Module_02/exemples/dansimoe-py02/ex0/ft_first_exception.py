def check_temperature(temp_str: str) -> int | None:
	try:
		temp = int(temp_str)
	except ValueError:
		print(f"Error: '{temp_str}' is not a valid number")
		return None
	if temp > 40:
		print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")
		return None
	if temp < 0:
		print(f"Error: {temp}ºC is too cold for plants (min 0ºC)")
		return None
	else:
		print(f"Temperature {temp}ºC is perfect for plants!")
		return temp


def main() -> None:
	test_values: list[str] = [
		"25",
		"abc",
		"100",
		"-50"
	]

	print("=== Garden Temperature Checker ===\n")

	for temp in test_values:
		print(f"Testing temperature: {temp}")
		check_temperature(temp)
		print()

	print("All tests completed - program didn't crash!")


if __name__ == "__main__":
	main()
