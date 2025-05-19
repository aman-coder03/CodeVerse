def parse_voice_to_code(voice_input):
    mappings = {
        "make a loop": "for i in range(10):",
        "say hello": "print('Hello!')"
    }
    for phrase, code in mappings.items():
        if phrase in voice_input.lower():
            return code
    return "# Sorry, I didn't understand the voice input."
