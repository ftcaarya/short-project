import time
import os


class InteractiveStory:
    def __init__(self):
        """Initialize the story with player state and story segments."""
        # Player state tracking
        self.player_name = ""
        self.inventory = []
        self.health = 100
        self.location = "forest_entrance"
        self.game_active = True

        # Story progress tracking
        self.visited_locations = set()
        self.story_choices = []

    def display_text(self, text, delay=0.01):
        """Display text with a typing effect for better user experience."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def get_user_input(self, prompt, options=None):
        """
        Get and validate user input.

        Args:
            prompt (str): The question to ask the user
            options (list, optional): Valid response options

        Returns:
            str: User's validated input
        """
        while True:
            self.display_text("\n" + prompt)

            # Display options if provided
            if options:
                option_text = ", ".join([f"'{o}'" for o in options[:-1]])
                if len(options) > 1:
                    option_text += f", or '{options[-1]}'"
                else:
                    option_text = f"'{options[0]}'"
                self.display_text(f"(Choose {option_text})")

            user_input = input("> ").strip().lower()

            # Check if user wants to stop
            if user_input == "stop":
                self.display_text("\nYou've chosen to stop the story. Goodbye!")
                self.game_active = False
                return "stop"

            # Validate input if options are provided
            if options and user_input not in [opt.lower() for opt in options]:
                self.display_text("That's not a valid choice. Please try again.")
                continue

            return user_input

    def introduction(self):
        """Display the introduction and get the player's name."""
        self.display_text("THE ENCHANTED FOREST ADVENTURE", 0.05)
        self.display_text("================================", 0.02)
        time.sleep(0.5)

        self.display_text("\nWelcome to an interactive adventure where YOUR choices shape the story!")
        self.display_text("At any time, type 'stop' to end the adventure.")
        time.sleep(1)

        # Get player name with validation
        while not self.player_name and self.game_active:
            name = self.get_user_input("\nWhat is your name, brave adventurer?")
            if name == "stop":
                return

            if name:
                self.player_name = name
                self.display_text(f"\nWelcome, {self.player_name}! Your adventure awaits...")
            else:
                self.display_text("Please enter a valid name.")

        time.sleep(1)
        self.forest_entrance()

    def forest_entrance(self):
        """The starting location of the adventure."""
        self.location = "forest_entrance"
        self.visited_locations.add(self.location)

        self.display_text(f"\n{self.player_name}, you stand at the entrance of the Enchanted Forest.")
        self.display_text("Ancient trees tower above you, their leaves shimmering with an odd blue glow.")
        self.display_text("A worn path leads deeper into the forest, while a small cave sits to your right.")

        choice = self.get_user_input("\nWhich way do you go?", ["path", "cave"])

        if not self.game_active:
            return

        if choice == "path":
            self.story_choices.append(("forest_entrance", "path"))
            self.display_text("\nYou decide to follow the path deeper into the forest...")
            time.sleep(1)
            self.forest_clearing()
        else:
            self.story_choices.append(("forest_entrance", "cave"))
            self.display_text("\nYou cautiously approach the mysterious cave...")
            time.sleep(1)
            self.mysterious_cave()

    def forest_clearing(self):
        """A clearing in the forest with a magical fountain."""
        self.location = "forest_clearing"
        self.visited_locations.add(self.location)

        self.display_text("\nThe path opens into a sunlit clearing.")
        self.display_text("In the center stands a stone fountain, water sparkling with multicolored light.")
        self.display_text("A small creature—perhaps a fairy—watches you from behind a tree.")

        choice = self.get_user_input("\nWhat do you do?", ["approach fountain", "talk to fairy"])

        if not self.game_active:
            return

        if choice == "approach fountain":
            self.story_choices.append(("forest_clearing", "approach fountain"))
            self.display_text("\nYou walk toward the beautiful fountain...")
            time.sleep(1)
            self.magic_fountain()
        else:
            self.story_choices.append(("forest_clearing", "talk to fairy"))
            self.display_text("\nYou slowly walk toward the fairy, trying not to scare it...")
            time.sleep(1)
            self.fairy_encounter()

    def mysterious_cave(self):
        """A dark cave with ancient inscriptions."""
        self.location = "mysterious_cave"
        self.visited_locations.add(self.location)

        self.display_text("\nThe cave is darker than expected but surprisingly warm.")
        self.display_text("Your eyes adjust to reveal walls covered in strange glowing symbols.")
        self.display_text("A soft humming noise comes from deeper within.")
        self.display_text("There's also a small opening to your left that leads outside.")

        choice = self.get_user_input("\nWhat will you do?", ["follow sound", "examine symbols", "exit cave"])

        if not self.game_active:
            return

        if choice == "follow sound":
            self.story_choices.append(("mysterious_cave", "follow sound"))
            self.display_text("\nYou decide to follow the mysterious humming sound...")
            time.sleep(1)
            self.crystal_chamber()
        elif choice == "examine symbols":
            self.story_choices.append(("mysterious_cave", "examine symbols"))
            self.display_text("\nYou move closer to study the unusual symbols...")
            time.sleep(1)
            self.ancient_language()
        else:
            self.story_choices.append(("mysterious_cave", "exit cave"))
            self.display_text("\nYou decide to leave the cave...")
            time.sleep(1)
            self.forest_clearing()

    def magic_fountain(self):
        """Interaction with a magical fountain."""
        self.location = "magic_fountain"
        self.visited_locations.add(self.location)

        self.display_text("\nThe fountain's water shifts colors as you approach.")
        self.display_text("An inscription on the basin reads: 'Drink and be changed.'")

        choice = self.get_user_input("\nDo you drink from the fountain?", ["yes", "no"])

        if not self.game_active:
            return

        if choice == "yes":
            self.story_choices.append(("magic_fountain", "drink"))
            self.display_text("\nYou cup your hands and drink the cool, sweet water.")
            self.display_text("A tingling sensation spreads throughout your body.")
            self.display_text("You suddenly understand the language of the forest!")
            self.inventory.append("forest tongue")

            time.sleep(2)
            self.fairy_encounter()
        else:
            self.story_choices.append(("magic_fountain", "refuse"))
            self.display_text("\nYou decide not to risk drinking the strange water.")
            self.display_text("As you step back, you notice a path leading to a tall tree.")

            time.sleep(2)
            self.ancient_tree()

    def fairy_encounter(self):
        """Meeting with a forest fairy."""
        self.location = "fairy_encounter"
        self.visited_locations.add(self.location)

        self.display_text("\nThe tiny fairy flutters before you, glowing with soft blue light.")

        if "forest tongue" in self.inventory:
            self.display_text("'Greetings, human!' the fairy chimes. 'Few come to our woods these days.'")
            self.display_text("'I can guide you to the heart of the forest or to the old guardian's tree.'")

            choice = self.get_user_input("\nWhere would you like the fairy to guide you?",
                                         ["heart of forest", "guardian's tree"])

            if not self.game_active:
                return

            if choice == "heart of forest":
                self.story_choices.append(("fairy_encounter", "heart of forest"))
                self.display_text("\nThe fairy nods and leads you deeper into the forest...")
                time.sleep(1)
                self.forest_heart()
            else:
                self.story_choices.append(("fairy_encounter", "guardian's tree"))
                self.display_text("\nThe fairy grins and zips ahead toward an enormous ancient tree...")
                time.sleep(1)
                self.ancient_tree()
        else:
            self.display_text("The fairy makes melodic sounds you cannot understand.")
            self.display_text("It seems to be trying to communicate something important.")
            self.display_text("After a moment, it looks disappointed and flies away.")

            self.display_text("\nPerhaps there's a way to understand the fairy language...")
            time.sleep(2)
            self.forest_clearing()

    def crystal_chamber(self):
        """A chamber with magical crystals."""
        self.location = "crystal_chamber"
        self.visited_locations.add(self.location)

        self.display_text("\nThe tunnel opens into a chamber lined with glowing crystals.")
        self.display_text("The humming grows louder here—it seems to come from the crystals themselves.")
        self.display_text("In the center of the room is a pedestal with a crystal wand.")

        choice = self.get_user_input("\nWhat do you do?", ["take wand", "touch crystals", "leave chamber"])

        if not self.game_active:
            return

        if choice == "take wand":
            self.story_choices.append(("crystal_chamber", "take wand"))
            self.display_text("\nAs your fingers close around the wand, energy courses through your arm!")
            self.display_text("You've gained a powerful magical tool.")
            self.inventory.append("crystal wand")

            time.sleep(2)
            self.display_text("\nWith the wand in hand, you decide to leave the chamber...")
            self.mysterious_cave()
        elif choice == "touch crystals":
            self.story_choices.append(("crystal_chamber", "touch crystals"))
            self.display_text("\nAs your fingers brush against the crystals, visions flood your mind!")
            self.display_text("You see glimpses of the forest's past, present, and possible futures.")
            self.display_text("The experience leaves you dizzy but enlightened.")

            time.sleep(2)
            self.ancient_language()
        else:
            self.story_choices.append(("crystal_chamber", "leave chamber"))
            self.display_text("\nYou decide not to disturb anything and back out of the chamber...")
            time.sleep(1)
            self.mysterious_cave()

    def ancient_language(self):
        """Discovering the secrets of ancient runes."""
        self.location = "ancient_language"
        self.visited_locations.add(self.location)

        self.display_text("\nYou study the glowing symbols carefully.")

        if "crystal wand" in self.inventory:
            self.display_text("With the crystal wand in your hand, the symbols reorganize themselves!")
            self.display_text("They now form words you can understand, telling an ancient story...")
            self.display_text("The story speaks of a guardian spirit that protects the forest heart.")

            self.inventory.append("guardian knowledge")
            time.sleep(2)

            choice = self.get_user_input("\nNow that you have this knowledge, where do you go?",
                                         ["find guardian", "return to cave entrance"])

            if not self.game_active:
                return

            if choice == "find guardian":
                self.story_choices.append(("ancient_language", "find guardian"))
                self.display_text("\nArmed with new knowledge, you set out to find the forest guardian...")
                time.sleep(1)
                self.ancient_tree()
            else:
                self.story_choices.append(("ancient_language", "return to cave"))
                self.display_text("\nYou decide to head back to the cave entrance...")
                time.sleep(1)
                self.mysterious_cave()
        else:
            self.display_text("The symbols seem to shift as you watch, but you cannot decipher them.")
            self.display_text("Perhaps you need something to help translate them.")

            time.sleep(2)
            self.mysterious_cave()

    def ancient_tree(self):
        """Meeting the ancient tree guardian."""
        self.location = "ancient_tree"
        self.visited_locations.add(self.location)

        self.display_text("\nBefore you stands the largest tree you've ever seen.")
        self.display_text("Its trunk must be thirty feet across, bark twisted into what almost looks like a face.")

        if "guardian knowledge" in self.inventory:
            self.display_text("\nRecognizing this as the guardian from the ancient text, you approach confidently.")
            self.display_text("The bark shifts and cracks as the face becomes more defined!")
            self.display_text("'Who comes to my domain with the knowledge of old?' a deep voice rumbles.")

            response = self.get_user_input(f"\nHow do you respond to the guardian?",
                                           ["seek knowledge", "need help"])

            if not self.game_active:
                return

            if response == "seek knowledge":
                self.story_choices.append(("ancient_tree", "seek knowledge"))
                self.display_text("\n'I seek the wisdom of the forest,' you reply respectfully.")
                self.display_text("The guardian's wooden face creaks into what might be a smile.")
                self.display_text("'Then you shall have it. The heart of the forest welcomes you.'")

                time.sleep(2)
                self.forest_heart()
            else:
                self.story_choices.append(("ancient_tree", "need help"))
                self.display_text("\n'The forest is in danger, and I need your help,' you explain.")
                self.display_text("The guardian tree considers your words carefully.")
                self.display_text("'The balance must be maintained. I shall assist you.'")

                self.inventory.append("guardian blessing")
                time.sleep(2)
                self.forest_heart()
        else:
            self.display_text("\nThe tree stands silent and imposing, showing no signs of life or magic.")
            self.display_text("You feel there must be more to this tree, but you don't know how to proceed.")

            time.sleep(2)
            self.display_text("\nPerhaps there are clues elsewhere in the forest...")

            choice = self.get_user_input("\nWhere do you go next?", ["back to clearing", "explore more"])

            if not self.game_active:
                return

            if choice == "back to clearing":
                self.story_choices.append(("ancient_tree", "back to clearing"))
                self.forest_clearing()
            else:
                self.story_choices.append(("ancient_tree", "explore more"))
                if "crystal wand" not in self.inventory:
                    self.display_text("\nYou decide to explore another part of the forest...")
                    self.mysterious_cave()
                else:
                    self.display_text("\nWith your crystal wand, you sense a powerful presence deeper in the forest...")
                    self.forest_heart()

    def forest_heart(self):
        """The magical center of the forest and story conclusion."""
        self.location = "forest_heart"
        self.visited_locations.add(self.location)

        self.display_text("\nYou enter a perfect circular clearing bathed in ethereal light.")
        self.display_text("The very air seems to shimmer with magic, and the plants glow with inner light.")
        self.display_text("In the center stands a brilliant crystalline structure pulsing with energy.")

        # Check for different endings based on inventory and choices
        if "guardian blessing" in self.inventory:
            self.display_text("\nThe blessing of the guardian protects you as you approach the heart.")
            self.display_text("The crystal resonates with your presence, accepting you as a friend of the forest.")
            self.display_text("Knowledge and understanding flow into your mind.")
            self.display_text(f"\n{self.player_name}, you have become a Guardian of the Enchanted Forest!")

            self.conclusion("guardian")
        elif "crystal wand" in self.inventory and "forest tongue" in self.inventory:
            self.display_text("\nYour crystal wand glows brightly as you approach the heart.")
            self.display_text("With your understanding of the forest tongue, you hear whispers all around.")
            self.display_text("The crystal responds to your wand, creating a bridge of light between them.")
            self.display_text(f"\n{self.player_name}, you have become a Mage of the Enchanted Forest!")

            self.conclusion("mage")
        else:
            self.display_text("\nThe heart of the forest is beautiful but mysterious to you.")
            self.display_text("You sense there's much more to learn about this magical place.")
            self.display_text("Perhaps with more knowledge or tools, you could unlock its secrets.")
            self.display_text(f"\n{self.player_name}, your adventure in the Enchanted Forest has only just begun!")

            self.conclusion("explorer")

    def conclusion(self, ending_type):
        """Display the story conclusion based on the player's journey."""
        self.display_text("\n----- YOUR ADVENTURE SUMMARY -----")
        self.display_text(f"Name: {self.player_name}")
        self.display_text(f"Places visited: {len(self.visited_locations)}")
        self.display_text(f"Items collected: {', '.join(self.inventory) if self.inventory else 'None'}")

        if ending_type == "guardian":
            self.display_text("\nEnding: Guardian of the Forest")
            self.display_text("You've earned the highest honor the forest can bestow.")
            self.display_text("Your connection to this magical place will last a lifetime.")
        elif ending_type == "mage":
            self.display_text("\nEnding: Forest Mage")
            self.display_text("You've unlocked powerful magical abilities and knowledge.")
            self.display_text("The mysteries of nature are yours to explore.")
        else:
            self.display_text("\nEnding: Forest Explorer")
            self.display_text("You've only scratched the surface of what the forest holds.")
            self.display_text("Return again with more knowledge to discover deeper secrets.")

        self.display_text("\nThank you for playing THE ENCHANTED FOREST ADVENTURE!")
        self.game_active = False

    def start_game(self):
        """Begin the interactive story adventure."""
        self.introduction()

        # If game ended early, show a goodbye message
        if not self.game_active and not self.location == "forest_heart":
            self.display_text("\nYour adventure has ended. Perhaps you'll return to the Enchanted Forest another day!")


# Main program execution
if __name__ == "__main__":
    story = InteractiveStory()
    story.start_game()