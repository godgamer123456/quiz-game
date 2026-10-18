import random
import time

def line():
    print("=" * 45)

def welcome():
    line()
    print("            THE QUIZ CHALLENGE")
    line()
    print("Answer questions, earn points, and beat")
    print("your high score!")
    line()

def choose_difficulty():
    print("\nChoose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Mixed")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        elif choice == "4":
            return "Mixed"
        else:
            print("Please enter a number from 1 to 4.")

def get_questions():
    questions = {
        "Easy": [
            ("What is 7 + 8?", ["A. 14", "B. 15", "C. 16", "D. 17"], "B"),
            ("How many days are in a week?", ["A. 5", "B. 6", "C. 7", "D. 8"], "C"),
            ("What color do you get by mixing red and blue?", ["A. Green", "B. Orange", "C. Yellow", "D. Purple"], "D"),
            ("Which animal barks?", ["A. Cat", "B. Dog", "C. Horse", "D. Fish"], "B"),
            ("How many legs does a spider have?", ["A. 6", "B. 8", "C. 10", "D. 4"], "B"),
            ("What is 20 divided by 4?", ["A. 4", "B. 5", "C. 6", "D. 8"], "B"),
            ("Which season comes after spring?", ["A. Winter", "B. Autumn", "C. Summer", "D. Spring"], "C"),
            ("How many months are in a year?", ["A. 10", "B. 11", "C. 12", "D. 13"], "C"),
            ("What is the opposite of tall?", ["A. Short", "B. Wide", "C. Long", "D. Big"], "A"),
            ("Which animal is known as man's best friend?", ["A. Cat", "B. Dog", "C. Rabbit", "D. Bird"], "B"),
            ("How many wheels does a bicycle have?", ["A. 1", "B. 2", "C. 3", "D. 4"], "B"),
            ("What is 9 x 3?", ["A. 18", "B. 21", "C. 27", "D. 30"], "C"),
            ("Which of these is a fruit?", ["A. Carrot", "B. Potato", "C. Apple", "D. Lettuce"], "C"),
            ("What do bees make?", ["A. Milk", "B. Honey", "C. Bread", "D. Juice"], "B"),
            ("How many hours are in a day?", ["A. 12", "B. 18", "C. 24", "D. 30"], "C"),
            ("What is 5 + 5?", ["A. 8", "B. 9", "C. 10", "D. 11"], "C"),
            ("What is the color of a clear daytime sky?", ["A. Red", "B. Blue", "C. Green", "D. Yellow"], "B"),
            ("How many fingers are on one human hand?", ["A. 4", "B. 5", "C. 6", "D. 10"], "B"),
            ("Which animal says meow?", ["A. Dog", "B. Cat", "C. Cow", "D. Duck"], "B"),
            ("What shape is a basketball?", ["A. Square", "B. Triangle", "C. Sphere", "D. Pyramid"], "C"),
            ("Which of these is a mammal?", ["A. Shark", "B. Whale", "C. Eagle", "D. Frog"], "B"),
            ("What is 10 minus 3?", ["A. 5", "B. 6", "C. 7", "D. 8"], "C"),
            ("What do cows drink?", ["A. Milk", "B. Water", "C. Juice", "D. Soda"], "B"),
            ("Which direction does the sun rise?", ["A. North", "B. South", "C. East", "D. West"], "C"),
            ("How many primary colors are there traditionally?", ["A. 2", "B. 3", "C. 4", "D. 5"], "B"),
            ("What is 6 x 2?", ["A. 10", "B. 12", "C. 14", "D. 16"], "B"),
            ("Which bird cannot fly?", ["A. Sparrow", "B. Penguin", "C. Pigeon", "D. Eagle"], "B"),
            ("What is the freezing point of water in Fahrenheit?", ["A. 0", "B. 32", "C. 100", "D. 212"], "B"),
            ("Which of these animals hops?", ["A. Kangaroo", "B. Elephant", "C. Lion", "D. Crocodile"], "A"),
            ("What is 50 divided by 10?", ["A. 2", "B. 5", "C. 10", "D. 50"], "B"),
            ("What do caterpillars turn into?", ["A. Beetles", "B. Butterflies", "C. Spiders", "D. Ants"], "B"),
            ("Which of these is a vegetable?", ["A. Banana", "B. Broccoli", "C. Strawberry", "D. Grape"], "B"),
            ("How many sides does a triangle have?", ["A. 2", "B. 3", "C. 4", "D. 5"], "B"),
            ("What is the color of an emerald?", ["A. Red", "B. Blue", "C. Green", "D. Yellow"], "C"),
            ("Which of these wears a shell?", ["A. Turtle", "B. Rabbit", "C. Fox", "D. Wolf"], "A"),
            ("What is 4 x 4?", ["A. 12", "B. 16", "C. 20", "D. 24"], "B"),
            ("Which month comes first in the year?", ["A. February", "B. December", "C. January", "D. March"], "C"),
            ("What do you use to write on a blackboard?", ["A. Pen", "B. Chalk", "C. Marker", "D. Paint"], "B"),
            ("Which animal is known for having a long neck?", ["A. Giraffe", "B. Zebra", "C. Hippo", "D. Rhino"], "A"),
            ("What is 100 divided by 20?", ["A. 4", "B. 5", "C. 10", "D. 20"], "B"),
            ("How many cents are in a US dollar?", ["A. 10", "B. 50", "C. 100", "D. 1000"], "C"),
            ("Which of these is a cold environment?", ["A. Desert", "B. Arctic", "C. Jungle", "D. Savanna"], "B"),
            ("What is 3 plus 3 plus 3?", ["A. 6", "B. 9", "C. 12", "D. 15"], "B"),
            ("Which fruit is yellow and curved?", ["A. Apple", "B. Banana", "C. Orange", "D. Pear"], "B"),
            ("What sound does a cow make?", ["A. Moo", "B. Baa", "C. Oink", "D. Quack"], "A"),
            ("How many toes does a human typically have on one foot?", ["A. 4", "B. 5", "C. 6", "D. 10"], "B"),
            ("Which of these drinks is made from pressed grapes?", ["A. Milk", "B. Wine", "C. Tea", "D. Coffee"], "B"),
            ("What is 8 minus 5?", ["A. 2", "B. 3", "C. 4", "D. 5"], "B"),
            ("Which animal is known as the king of the jungle?", ["A. Tiger", "B. Lion", "C. Elephant", "D. Cheetah"], "B"),
            ("What is the color of a ruby?", ["A. Blue", "B. Green", "C. Red", "D. Yellow"], "C"),
            ("What is 6 + 6?", ["A. 11", "B. 12", "C. 13", "D. 14"], "B"),
            ("How many days are in February during a leap year?", ["A. 28", "B. 29", "C. 30", "D. 31"], "B"),
            ("What color is a ripe banana?", ["A. Green", "B. Red", "C. Yellow", "D. Blue"], "C"),
            ("Which animal is known for moving very slowly?", ["A. Sloth", "B. Cheetah", "C. Rabbit", "D. Fox"], "A"),
            ("How many sides does a square have?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
            ("What is 15 minus 5?", ["A. 5", "B. 10", "C. 15", "D. 20"], "B"),
            ("Which season is generally the warmest?", ["A. Winter", "B. Spring", "C. Summer", "D. Autumn"], "C"),
            ("How many weeks are in a year?", ["A. 40", "B. 48", "C. 52", "D. 60"], "C"),
            ("What is the opposite of hot?", ["A. Cold", "B. Warm", "C. Bright", "D. Dark"], "A"),
            ("Which animal is known as a giant sea mammal?", ["A. Shark", "B. Whale", "C. Tuna", "D. Eel"], "B"),
            ("How many wheels does a standard car have?", ["A. 2", "B. 3", "C. 4", "D. 6"], "C"),
            ("What is 8 x 2?", ["A. 14", "B. 16", "C. 18", "D. 20"], "B"),
            ("Which of these is a vegetable?", ["A. Carrot", "B. Apple", "C. Banana", "D. Orange"], "A"),
            ("What do cows produce?", ["A. Milk", "B. Juice", "C. Honey", "D. Soda"], "A"),
            ("How many minutes are in an hour?", ["A. 30", "B. 45", "C. 60", "D. 90"], "C"),
            ("What is 3 + 4?", ["A. 6", "B. 7", "C. 8", "D. 9"], "B"),
            ("What color is fresh snow?", ["A. White", "B. Blue", "C. Gray", "D. Yellow"], "A"),
            ("How many hands does a person have?", ["A. 1", "B. 2", "C. 3", "D. 4"], "B"),
            ("Which animal quacks?", ["A. Dog", "B. Duck", "C. Cat", "D. Cow"], "B"),
            ("What shape is a standard stop sign?", ["A. Circle", "B. Square", "C. Triangle", "D. Octagon"], "D"),
            ("Which of these is an insect?", ["A. Ant", "B. Dog", "C. Bird", "D. Fish"], "A"),
            ("What is 12 minus 4?", ["A. 6", "B. 8", "C. 10", "D. 12"], "B"),
            ("What do dogs love to chase for fun?", ["A. Balls", "B. Clouds", "C. Trees", "D. Bricks"], "A"),
            ("Which direction is opposite to North?", ["A. East", "B. South", "C. West", "D. Up"], "B"),
            ("How many primary colors are there?", ["A. 2", "B. 3", "C. 4", "D. 5"], "B"),
            ("What is 7 x 2?", ["A. 12", "B. 14", "C. 16", "D. 18"], "B"),
            ("Which bird swims and quacks?", ["A. Duck", "B. Eagle", "C. Hawk", "D. Owl"], "A"),
            ("What is the freezing point of water in Celsius?", ["A. 0", "B. 10", "C. 32", "D. 100"], "A"),
            ("Which animal jumps around in Australia?", ["A. Kangaroo", "B. Elephant", "C. Wolf", "D. Bear"], "A"),
            ("What is 40 divided by 10?", ["A. 2", "B. 4", "C. 10", "D. 40"], "B"),
            ("What do tadpoles eventually turn into?", ["A. Frogs", "B. Fish", "C. Birds", "D. Snakes"], "A"),
            ("Which of these is a citrus fruit?", ["A. Lemon", "B. Potato", "C. Lettuce", "D. Bread"], "A"),
            ("How many sides does a rectangle have?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
            ("What is the color of coal?", ["A. Black", "B. White", "C. Red", "D. Green"], "A"),
            ("Which of these wears a hard protective shell?", ["A. Crab", "B. Rabbit", "C. Bird", "D. Cat"], "A"),
            ("What is 3 x 5?", ["A. 12", "B. 15", "C. 18", "D. 20"], "B"),
            ("Which month comes right after May?", ["A. April", "B. June", "C. July", "D. August"], "B"),
            ("What do you use to erase pencil marks on paper?", ["A. Eraser", "B. Ruler", "C. Marker", "D. Glue"], "A"),
            ("Which animal is known for jumping very high?", ["A. Kangaroo", "B. Turtle", "C. Snail", "D. Worm"], "A"),
            ("What is 80 divided by 10?", ["A. 6", "B. 8", "C. 10", "D. 20"], "B"),
            ("How many nickels make up one dollar?", ["A. 5", "B. 10", "C. 20", "D. 50"], "C"),
            ("Which environment is extremely hot and dry?", ["A. Desert", "B. Tundra", "C. Rainforest", "D. Glacier"], "A"),
            ("What is 2 + 2 + 2?", ["A. 4", "B. 6", "C. 8", "D. 10"], "B"),
            ("Which fruit is red and has its seeds on the outside?", ["A. Banana", "B. Strawberry", "C. Orange", "D. Apple"], "B"),
            ("What sound does a happy cat make?", ["A. Meow", "B. Bark", "C. Moo", "D. Roar"], "A"),
            ("How many thumbs does a human hand have?", ["A. 1", "B. 2", "C. 3", "D. 4"], "A"),
            ("Which of these drinks is made from roasted beans?", ["A. Milk", "B. Tea", "C. Coffee", "D. Juice"], "C"),
            ("What is 10 minus 5?", ["A. 2", "B. 5", "C. 8", "D. 10"], "B"),
            ("Which animal is known for having a long trunk?", ["A. Elephant", "B. Lion", "C. Zebra", "D. Tiger"], "A"),
            ("What is the color of a sapphire gemstone?", ["A. Red", "B. Blue", "C. Green", "D. Yellow"], "B")
        ],
        "Medium": [
            ("What is the capital of Japan?", ["A. Seoul", "B. Tokyo", "C. Beijing", "D. Bangkok"], "B"),
            ("What is 12 x 12?", ["A. 124", "B. 132", "C. 144", "D. 154"], "C"),
            ("Which planet is closest to the Sun?", ["A. Venus", "B. Earth", "C. Mars", "D. Mercury"], "D"),
            ("How many sides does an octagon have?", ["A. 6", "B. 7", "C. 8", "D. 9"], "C"),
            ("What is the largest ocean?", ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"], "B"),
            ("Who wrote Romeo and Juliet?", ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. J.K. Rowling"], "C"),
            ("What is the square root of 81?", ["A. 7", "B. 8", "C. 9", "D. 10"], "C"),
            ("Which gas do plants absorb?", ["A. Oxygen", "B. Carbon dioxide", "C. Hydrogen", "D. Helium"], "B"),
            ("How many continents are there?", ["A. 5", "B. 6", "C. 7", "D. 8"], "C"),
            ("What is the largest mammal?", ["A. Elephant", "B. Giraffe", "C. Blue whale", "D. Shark"], "C"),
            ("Which country is famous for the pyramids of Giza?", ["A. Greece", "B. Egypt", "C. Italy", "D. India"], "B"),
            ("What is 15% of 200?", ["A. 15", "B. 20", "C. 30", "D. 40"], "C"),
            ("Which organ pumps blood around the body?", ["A. Brain", "B. Liver", "C. Heart", "D. Lung"], "C"),
            ("What is the freezing point of water in Celsius?", ["A. 0", "B. 10", "C. 32", "D. 100"], "A"),
            ("Which language is mainly spoken in Brazil?", ["A. Spanish", "B. Portuguese", "C. French", "D. English"], "B"),
            ("What is the capital of Australia?", ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"], "C"),
            ("What is 14 squared?", ["A. 186", "B. 196", "C. 206", "D. 216"], "B"),
            ("Which planet is known as the Red Planet?", ["A. Venus", "B. Saturn", "C. Mars", "D. Jupiter"], "C"),
            ("How many players are on the field for one soccer team?", ["A. 9", "B. 10", "C. 11", "D. 12"], "C"),
            ("What is the longest river in the world?", ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"], "B"),
            ("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"], "C"),
            ("What is the boiling point of water in Celsius?", ["A. 90", "B. 100", "C. 110", "D. 120"], "B"),
            ("Which chemical element has the symbol 'O'?", ["A. Osmium", "B. Oxygen", "C. Gold", "D. Opal"], "B"),
            ("What is the smallest continent by land area?", ["A. Europe", "B. Antarctica", "C. Australia", "D. South America"], "C"),
            ("Who discovered penicillin?", ["A. Alexander Fleming", "B. Louis Pasteur", "C. Marie Curie", "D. Isaac Newton"], "A"),
            ("What is 25 x 4?", ["A. 75", "B. 100", "C. 125", "D. 150"], "B"),
            ("Which country has the largest land area?", ["A. Canada", "B. China", "C. USA", "D. Russia"], "D"),
            ("What is the currency of the United Kingdom?", ["A. Euro", "B. Dollar", "C. Pound", "D. Franc"], "C"),
            ("Which instrument has black and white keys?", ["A. Violin", "B. Flute", "C. Piano", "D. Trumpet"], "C"),
            ("What is 3 cubed?", ["A. 6", "B. 9", "C. 27", "D. 81"], "C"),
            ("Which gas makes up most of Earth's atmosphere?", ["A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"], "B"),
            ("What is the capital of Italy?", ["A. Venice", "B. Milan", "C. Rome", "D. Naples"], "C"),
            ("Which vitamin is produced when skin is exposed to sunlight?", ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"], "D"),
            ("What is the hardest metal?", ["A. Iron", "B. Titanium", "C. Tungsten", "D. Steel"], "C"),
            ("How many bones are in the spine of an adult human?", ["A. 24", "B. 26", "C. 30", "D. 33"], "B"),
            ("What is 11 x 15?", ["A. 155", "B. 165", "C. 175", "D. 185"], "B"),
            ("Which continent is the Sahara Desert located in?", ["A. Asia", "B. Africa", "C. Australia", "D. South America"], "B"),
            ("Who wrote 'The Odyssey'?", ["A. Homer", "B. Plato", "C. Aristotle", "D. Sophocles"], "A"),
            ("What is the main ingredient in traditional guacamole?", ["A. Tomato", "B. Avocado", "C. Pepper", "D. Onion"], "B"),
            ("Which planet has the most moons?", ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"], "B"),
            ("What is 99 divided by 3?", ["A. 23", "B. 33", "C. 43", "D. 53"], "B"),
            ("Which mountain is the tallest in the world?", ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Lhotse"], "B"),
            ("What is the chemical formula for table salt?", ["A. H2O", "B. NaCl", "C. CO2", "D. CH4"], "B"),
            ("Which US state is known as the Sunshine State?", ["A. California", "B. Texas", "C. Florida", "D. Hawaii"], "C"),
            ("What is the square root of 144?", ["A. 10", "B. 11", "C. 12", "D. 13"], "C"),
            ("Which animal is known as the ship of the desert?", ["A. Horse", "B. Camel", "C. Elephant", "D. Donkey"], "B"),
            ("What is the capital of Spain?", ["A. Barcelona", "B. Madrid", "C. Seville", "D. Valencia"], "B"),
            ("Which bird is a universal symbol of peace?", ["A. Eagle", "B. Dove", "C. Swan", "D. Owl"], "B"),
            ("What is 7 cubed?", ["A. 243", "B. 343", "C. 443", "D. 543"], "B"),
            ("Which ocean lies between Africa and Australia?", ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"], "C"),
            ("What is the capital of France?", ["A. Lyon", "B. Paris", "C. Marseille", "D. Nice"], "B"),
            ("What is 13 x 13?", ["A. 159", "B. 169", "C. 179", "D. 189"], "B"),
            ("Which planet is known as the Ringed Planet?", ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"], "B"),
            ("How many sides does a hexagon have?", ["A. 5", "B. 6", "C. 7", "D. 8"], "B"),
            ("What is the second largest ocean?", ["A. Atlantic", "B. Indian", "C. Arctic", "D. Southern"], "A"),
            ("Who wrote the play Hamlet?", ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Oscar Wilde"], "C"),
            ("What is the square root of 64?", ["A. 6", "B. 8", "C. 9", "D. 7"], "B"),
            ("Which gas is most abundant in Earth's atmosphere?", ["A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Argon"], "B"),
            ("How many US states are there?", ["A. 48", "B. 49", "C. 50", "D. 52"], "C"),
            ("What is the fastest land animal?", ["A. Lion", "B. Tiger", "C. Cheetah", "D. Gazelle"], "C"),
            ("Which country is home to the Taj Mahal?", ["A. Pakistan", "B. India", "C. Bangladesh", "D. Nepal"], "B"),
            ("What is 20% of 150?", ["A. 20", "B. 25", "C. 30", "D. 35"], "C"),
            ("Which organ filters waste products from the blood?", ["A. Heart", "B. Kidney", "C. Liver", "D. Lungs"], "B"),
            ("What is the boiling point of water in Fahrenheit?", ["A. 100", "B. 212", "C. 180", "D. 320"], "B"),
            ("Which language is primarily spoken in Mexico?", ["A. Spanish", "B. Portuguese", "C. French", "D. Italian"], "A"),
            ("What is the capital of Germany?", ["A. Munich", "B. Berlin", "C. Frankfurt", "D. Hamburg"], "B"),
            ("What is 15 squared?", ["A. 215", "B. 225", "C. 235", "D. 245"], "B"),
            ("Which planet is the largest in our solar system?", ["A. Saturn", "B. Jupiter", "C. Neptune", "D. Uranus"], "B"),
            ("How many players are on the court for one basketball team?", ["A. 4", "B. 5", "C. 6", "D. 7"], "B"),
            ("What is the deepest ocean trench in the world?", ["A. Tonga Trench", "B. Mariana Trench", "C. Philippine Trench", "D. Kuril Trench"], "B"),
            ("Who painted The Last Supper?", ["A. Michelangelo", "B. Raphael", "C. Leonardo da Vinci", "D. Donatello"], "C"),
            ("At what temperature are Celsius and Fahrenheit equal?", ["A. 0", "B. -40", "C. -32", "D. 100"], "B"),
            ("Which chemical element has the symbol 'Fe'?", ["A. Fluorine", "B. Iron", "C. Francium", "D. Fermium"], "B"),
            ("What is the smallest independent country in the world?", ["A. Vatican City", "B. Monaco", "C. San Marino", "D. Liechtenstein"], "A"),
            ("Who is credited with inventing the telephone?", ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Guglielmo Marconi"], "A"),
            ("What is 30 x 3?", ["A. 60", "B. 90", "C. 120", "D. 150"], "B"),
            ("Which country has the most natural lakes?", ["A. Canada", "B. Russia", "C. USA", "D. Brazil"], "A"),
            ("What is the official currency of Japan?", ["A. Yuan", "B. Yen", "C. Won", "D. Ringgit"], "B"),
            ("Which musical instrument has strings and is played using a bow?", ["A. Violin", "B. Flute", "C. Trumpet", "D. Clarinet"], "A"),
            ("What is 4 cubed?", ["A. 16", "B. 32", "C. 64", "D. 128"], "C"),
            ("Which layer of atmospheric gas protects Earth from harmful UV rays?", ["A. Troposphere", "B. Ozone", "C. Mesosphere", "D. Thermosphere"], "B"),
            ("What is the capital city of Greece?", ["A. Thessaloniki", "B. Athens", "C. Patras", "D. Heraklion"], "B"),
            ("Which vitamin is commonly known as ascorbic acid?", ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"], "C"),
            ("What is the softest mineral on the Mohs scale?", ["A. Talc", "B. Gypsum", "C. Calcite", "D. Fluorite"], "A"),
            ("How many vertebrae are in the human neck?", ["A. 5", "B. 7", "C. 9", "D. 12"], "B"),
            ("What is 12 x 15?", ["A. 160", "B. 180", "C. 200", "D. 210"], "B"),
            ("Which desert covers much of northern China and Mongolia?", ["A. Sahara", "B. Gobi", "C. Mojave", "D. Kalahari"], "B"),
            ("Who wrote the novel 'The Great Gatsby'?", ["A. F. Scott Fitzgerald", "B. Ernest Hemingway", "C. John Steinbeck", "D. Mark Twain"], "A"),
            ("What is the main protein found in milk?", ["A. Casein", "B. Keratin", "C. Collagen", "D. Albumin"], "A"),
            ("Which moon of Saturn features a dense atmosphere?", ["A. Enceladus", "B. Titan", "C. Mimas", "D. Dione"], "B"),
            ("What is 120 divided by 4?", ["A. 20", "B. 30", "C. 40", "D. 60"], "B"),
            ("Which major mountain range separates Europe from Asia?", ["A. Alps", "B. Ural Mountains", "C. Himalayas", "D. Andes"], "B"),
            ("What is the chemical formula for ammonia?", ["A. CH4", "B. CO2", "C. NH3", "D. H2O"], "C"),
            ("Which US state boasts the longest general coastline?", ["A. Alaska", "B. California", "C. Florida", "D. Texas"], "A"),
            ("What is the square root of 169?", ["A. 11", "B. 13", "C. 15", "D. 17"], "B"),
            ("Which animal is known as the closest relative of the extinct thylacine?", ["A. Tasmanian Devil", "B. Kangaroo", "C. Koala", "D. Wombat"], "A"),
            ("What is the capital of Argentina?", ["A. Cordoba", "B. Buenos Aires", "C. Rosario", "D. Mendoza"], "B"),
            ("Which bird is uniquely capable of flying backwards?", ["A. Hummingbird", "B. Swallow", "C. Swift", "D. Finch"], "A"),
            ("What is 8 cubed?", ["A. 256", "B. 512", "C. 1024", "D. 2048"], "B"),
            ("Which major sea lies directly between Europe and Africa?", ["A. Baltic Sea", "B. Mediterranean Sea", "C. Black Sea", "D. Red Sea"], "B")
        ],
        "Hard": [
            ("What is the chemical symbol for gold?", ["A. Go", "B. Ag", "C. Au", "D. Gd"], "C"),
            ("What is the smallest prime number?", ["A. 0", "B. 1", "C. 2", "D. 3"], "C"),
            ("Which planet has the most prominent ring system?", ["A. Mars", "B. Saturn", "C. Venus", "D. Mercury"], "B"),
            ("What is the capital of Canada?", ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"], "C"),
            ("How many bones are in the adult human body?", ["A. 186", "B. 196", "C. 206", "D. 216"], "C"),
            ("What is the hardest natural substance?", ["A. Iron", "B. Diamond", "C. Quartz", "D. Granite"], "B"),
            ("Which scientist developed the theory of relativity?", ["A. Isaac Newton", "B. Galileo Galilei", "C. Albert Einstein", "D. Nikola Tesla"], "C"),
            ("What is the chemical formula for water?", ["A. CO2", "B. H2O", "C. O2", "D. NaCl"], "B"),
            ("Which country invented paper?", ["A. India", "B. Egypt", "C. China", "D. Greece"], "C"),
            ("What is 17 squared?", ["A. 279", "B. 289", "C. 299", "D. 309"], "B"),
            ("Which blood cells help fight infections?", ["A. Red blood cells", "B. Platelets", "C. White blood cells", "D. Plasma"], "C"),
            ("What is the largest desert in the world?", ["A. Sahara", "B. Gobi", "C. Antarctic Desert", "D. Arabian Desert"], "C"),
            ("Which element has the atomic number 1?", ["A. Helium", "B. Hydrogen", "C. Oxygen", "D. Carbon"], "B"),
            ("What is the capital of New Zealand?", ["A. Auckland", "B. Christchurch", "C. Wellington", "D. Hamilton"], "C"),
            ("How many degrees are in a triangle's angles combined?", ["A. 90", "B. 180", "C. 270", "D. 360"], "B"),
            ("What is the speed of light in a vacuum approximately?", ["A. 300,000 km/s", "B. 150,000 km/s", "C. 450,000 km/s", "D. 600,000 km/s"], "A"),
            ("Who wrote 'Crime and Punishment'?", ["A. Leo Tolstoy", "B. Fyodor Dostoevsky", "C. Anton Chekhov", "D. Alexander Pushkin"], "B"),
            ("What is the capital of Australia's neighbor, Vanuatu?", ["A. Suva", "B. Port Vila", "C. Honiara", "D. Apia"], "B"),
            ("Which element is represented by the symbol 'W'?", ["A. Tungsten", "B. Tin", "C. Sodium", "D. Potassium"], "A"),
            ("What is the value of Pi to four decimal places?", ["A. 3.1415", "B. 3.1416", "C. 3.1428", "D. 3.1315"], "B"),
            ("Which subatomic particle has a negative charge?", ["A. Proton", "B. Neutron", "C. Electron", "D. Positron"], "C"),
            ("What year did the Titanic sink?", ["A. 1910", "B. 1912", "C. 1914", "D. 1916"], "B"),
            ("What is the rarest blood type in humans?", ["A. O-negative", "B. AB-negative", "C. B-negative", "D. A-negative"], "B"),
            ("Who formulated the three laws of motion?", ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Johannes Kepler"], "B"),
            ("What is the capital of Mongolia?", ["A. Astana", "B. Ulaanbaatar", "C. Tashkent", "D. Bishkek"], "B"),
            ("What is the half-life of Carbon-14 approximately?", ["A. 2,500 years", "B. 5,730 years", "C. 10,000 years", "D. 1,200 years"], "B"),
            ("Which philosopher wrote 'Thus Spoke Zarathustra'?", ["A. Immanuel Kant", "B. Friedrich Nietzsche", "C. Arthur Schopenhauer", "D. Søren Kierkegaard"], "B"),
            ("What is the heavy isotope of hydrogen called?", ["A. Tritium", "B. Deuterium", "C. Protium", "D. Alpha"], "B"),
            ("Which empire was ruled by Cyrus the Great?", ["A. Roman Empire", "B. Persian Empire", "C. Ottoman Empire", "D. Byzantine Empire"], "B"),
            ("What is the clinical term for high blood pressure?", ["A. Hypoglycemia", "B. Hypertension", "C. Hyperemia", "D. Hypertrophy"], "B"),
            ("What is the derivative of $x^2$?", ["A. $x$", "B. $2x$", "C. $x^2$", "D. $2$"], "B"),
            ("Which chemical element has the highest melting point?", ["A. Iron", "B. Carbon", "C. Tungsten", "D. Platinum"], "C"),
            ("In what year did World War II end?", ["A. 1943", "B. 1944", "C. 1945", "D. 1946"], "C"),
            ("What is the capital of Iceland?", ["A. Oslo", "B. Helsinki", "C. Reykjavik", "D. Copenhagen"], "C"),
            ("Which organelle is known as the powerhouse of the cell?", ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Endoplasmic Reticulum"], "C"),
            ("What is the square root of 1024?", ["A. 24", "B. 32", "C. 36", "D. 42"], "B"),
            ("Who painted 'The Starry Night'?", ["A. Claude Monet", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Salvador Dalí"], "B"),
            ("What is the atomic number of Iron?", ["A. 24", "B. 26", "C. 28", "D. 30"], "B"),
            ("Which country has the longest coastline in the world?", ["A. Russia", "B. Australia", "C. Canada", "D. Indonesia"], "C"),
            ("What is the hardest mineral on the Mohs scale?", ["A. Corundum", "B. Topaz", "C. Diamond", "D. Quartz"], "C"),
            ("Which galaxy is closest to the Milky Way?", ["A. Andromeda", "B. Triangulum", "C. Sombrero", "D. Large Magellanic Cloud"], "A"),
            ("What is the chemical formula for methane?", ["A. CO2", "B. CH4", "C. NH3", "D. H2O"], "B"),
            ("Who was the first person to travel into space?", ["A. Neil Armstrong", "B. Yuri Gagarin", "C. Buzz Aldrin", "D. John Glenn"], "B"),
            ("What is the capital of Switzerland?", ["A. Zurich", "B. Geneva", "C. Bern", "D. Basel"], "C"),
            ("What is 19 squared?", ["A. 341", "B. 351", "C. 361", "D. 371"], "C"),
            ("Which layer of Earth's atmosphere contains the ozone layer?", ["A. Troposphere", "B. Stratosphere", "C. Mesosphere", "D. Thermosphere"], "B"),
            ("Who wrote the epic poem 'The Divine Comedy'?", ["A. Dante Alighieri", "B. Geoffrey Chaucer", "C. Virgil", "D. Ovid"], "A"),
            ("What is the atomic weight of Carbon?", ["A. 6", "B. 12", "C. 14", "D. 16"], "B"),
            ("Which desert is located in South America?", ["A. Mojave", "B. Atacama", "C. Kalahari", "D. Gobi"], "B"),
            ("What is the capital of Liechtenstein?", ["A. Vaduz", "B. Zurich", "C. Vienna", "D. Bern"], "A"),
            ("What is the chemical symbol for silver?", ["A. Si", "B. Ag", "C. Sr", "D. Sn"], "B"),
            ("What is the next prime number after 7?", ["A. 9", "B. 10", "C. 11", "D. 13"], "C"),
            ("Which planet rotates completely on its side?", ["A. Saturn", "B. Uranus", "C. Neptune", "D. Jupiter"], "B"),
            ("What is the capital of Kazakhstan?", ["A. Almaty", "B. Astana", "C. Shymkent", "D. Karaganda"], "B"),
            ("How many pairs of ribs are typically in a human body?", ["A. 10", "B. 11", "C. 12", "D. 14"], "C"),
            ("What is the densest naturally occurring element on Earth?", ["A. Platinum", "B. Osmium", "C. Iridium", "D. Gold"], "B"),
            ("Who proposed the heliocentric model of the universe?", ["A. Ptolemy", "B. Aristotle", "C. Nicolaus Copernicus", "D. Johannes Kepler"], "C"),
            ("What is the chemical formula for carbon dioxide?", ["A. CO", "B. CO2", "C. C2O", "D. C2O4"], "B"),
            ("Which Chinese dynasty built the vast majority of the modern Great Wall?", ["A. Han Dynasty", "B. Ming Dynasty", "C. Tang Dynasty", "D. Qin Dynasty"], "B"),
            ("What is 18 squared?", ["A. 304", "B. 324", "C. 344", "D. 364"], "B"),
            ("Which specific cells produce antibodies in the human immune system?", ["A. T cells", "B. Natural killer cells", "C. B cells", "D. Macrophages"], "C"),
            ("What is known as the driest non-polar desert on Earth?", ["A. Sahara Desert", "B. Atacama Desert", "C. Mojave Desert", "D. Arabian Desert"], "B"),
            ("Which chemical element has the atomic number 79?", ["A. Silver", "B. Platinum", "C. Gold", "D. Mercury"], "C"),
            ("What is the capital of South Korea?", ["A. Busan", "B. Seoul", "C. Incheon", "D. Daegu"], "B"),
            ("How many radians are contained in a full circle?", ["A. pi", "B. 1.5 pi", "C. 2 pi", "D. 4 pi"], "C"),
            ("What is the approximate escape velocity of Earth?", ["A. 11.2 km/s", "B. 8.5 km/s", "C. 15.4 km/s", "D. 24.1 km/s"], "A"),
            ("Who authored the epic novel 'War and Peace'?", ["A. Leo Tolstoy", "B. Fyodor Dostoevsky", "C. Anton Chekhov", "D. Ivan Turgenev"], "A"),
            ("What is the capital of the island nation of Fiji?", ["A. Suva", "B. Nadi", "C. Lautoka", "D. Labasa"], "A"),
            ("Which chemical element is represented by the symbol 'Sb'?", ["A. Antimony", "B. Sulfur", "C. Scandium", "D. Strontium"], "A"),
            ("What is the value of Euler's number (e) to three decimal places?", ["A. 2.141", "B. 2.718", "C. 3.142", "D. 1.414"], "B"),
            ("Which fundamental subatomic particle carries a positive electrical charge?", ["A. Proton", "B. Electron", "C. Neutron", "D. Positron"], "A"),
            ("In what exact year did the Berlin Wall officially fall?", ["A. 1987", "B. 1989", "C. 1991", "D. 1993"], "B"),
            ("What is considered the rarest blood type within the AB group?", ["A. AB-positive", "B. AB-negative", "C. O-negative", "D. B-negative"], "B"),
            ("Who developed the famous uncertainty principle in quantum mechanics?", ["A. Niels Bohr", "B. Werner Heisenberg", "C. Erwin Schrödinger", "D. Max Planck"], "B"),
            ("What is the capital of Kyrgyzstan?", ["A. Osh", "B. Bishkek", "C. Karakol", "D. Jalal-Abad"], "B"),
            ("What is the approximate half-life of Uranium-238?", ["A. 1 million years", "B. 4.5 billion years", "C. 5,730 years", "D. 100,000 years"], "B"),
            ("Which prominent philosopher authored 'Critique of Pure Reason'?", ["A. Immanuel Kant", "B. Friedrich Nietzsche", "C. Georg Wilhelm Friedrich Hegel", "D. Arthur Schopenhauer"], "A"),
            ("What is the lightest isotope of hydrogen containing zero neutrons?", ["A. Deuterium", "B. Tritium", "C. Protium", "D. Hydride"], "C"),
            ("Which ancient civilization built the famous mountaintop citadel of Machu Picchu?", ["A. Aztec", "B. Inca", "C. Maya", "D. Olmec"], "B"),
            ("What is the clinical medical term for dangerously low blood sugar?", ["A. Hypoglycemia", "B. Hyperglycemia", "C. Hypertension", "D. Hypotension"], "A"),
            ("What is the calculus integral of $2x$ with respect to $x$?", ["A. $2$", "B. $x^2 + C$", "C. $2x^2 + C$", "D. $x + C$"], "B"),
            ("Which pure chemical element has the lowest melting point of all metals?", ["A. Gallium", "B. Mercury", "C. Cesium", "D. Rubidium"], "B"),
            ("In what year did the historic French Revolution begin?", ["A. 1776", "B. 1789", "C. 1804", "D. 1815"], "B"),
            ("What is the capital city of Norway?", ["A. Stockholm", "B. Copenhagen", "C. Oslo", "D. Helsinki"], "C"),
            ("Which microscopic cell organelle is directly responsible for protein synthesis?", ["A. Nucleus", "B. Ribosome", "C. Golgi apparatus", "D. Lysosome"], "B"),
            ("What is the exact square root of 1296?", ["A. 34", "B. 36", "C. 38", "D. 42"], "B"),
            ("Who painted the surrealist masterpiece 'The Persistence of Memory'?", ["A. René Magritte", "B. Salvador Dalí", "C. Pablo Picasso", "D. Joan Miró"], "B"),
            ("What is the exact atomic number of the element Gold?", ["A. 47", "B. 79", "C. 82", "D. 92"], "C"),
            ("Which country possesses the second-longest coastline in the entire world?", ["A. Indonesia", "B. Russia", "C. Australia", "D. Philippines"], "A"),
            ("What is the second hardest mineral on the traditional Mohs scale of hardness?", ["A. Diamond", "B. Corundum", "C. Topaz", "D. Quartz"], "B"),
            ("Which star system hosts the closest known exoplanet to our solar system?", ["A. Proxima Centauri", "B. Sirius", "C. Alpha Centauri A", "D. Barnard's Star"], "A"),
            ("What is the correct chemical formula for concentrated sulfuric acid?", ["A. H2SO3", "B. H2SO4", "C. HSO4", "D. SO2"], "B"),
            ("Who was the very first woman in human history to travel into space?", ["A. Sally Ride", "B. Valentina Tereshkova", "C. Mae Jemison", "D. Svetlana Savitskaya"], "B"),
            ("What is the official capital city of Austria?", ["A. Salzburg", "B. Graz", "C. Vienna", "D. Linz"], "C"),
            ("What is 21 squared?", ["A. 421", "B. 441", "C. 461", "D. 481"], "B"),
            ("Which interior layer of the Earth is known to be completely in a liquid state?", ["A. Crust", "B. Outer core", "C. Inner core", "D. Mantle"], "B"),
            ("Who authored the epic narrative poem 'Paradise Lost'?", ["A. John Milton", "B. Geoffrey Chaucer", "C. Edmund Spenser", "D. John Donne"], "A"),
            ("What is the standard atomic weight of the element Oxygen?", ["A. 8", "B. 12", "C. 14", "D. 16"], "D"),
            ("Which major desert spans across much of southern Africa?", ["A. Sahara Desert", "B. Mojave Desert", "C. Kalahari Desert", "D. Gobi Desert"], "C"),
            ("What is the capital city of the microstate of Monaco?", ["A. Monaco", "B. Monte Carlo", "C. La Condamine", "D. Fontvieille"], "A")
        ]
    }

    return questions

def ask_question(question, number, total, points, streak):
    print()
    line()
    print("Question", number, "of", total)
    print("Current points:", points)
    print("Correct streak:", streak)
    line()
    print(question[0])

    for option in question[1]:
        print(option)

    while True:
        answer = input("Your answer: ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Enter A, B, C, or D.")

def play_quiz():
    all_questions = get_questions()
    difficulty = choose_difficulty()

    if difficulty == "Mixed":
        questions = []

        for category in all_questions.values():
            questions.extend(category)

        random.shuffle(questions)
    else:
        questions = all_questions[difficulty].copy()
        random.shuffle(questions)

    while True:
        try:
            amount = int(input("\nHow many questions do you want? (5-15): "))

            if 5 <= amount <= 15:
                break
            else:
                print("Choose a number between 5 and 15.")
        except ValueError:
            print("Please enter a valid number.")

    questions = questions[:amount]

    score = 0
    correct = 0
    wrong = 0
    streak = 0
    best_streak = 0
    results = []

    start_time = time.time()

    print("\nGet ready!")
    time.sleep(1)

    for number, question in enumerate(questions, 1):
        answer = ask_question(
            question, number, len(questions), score, streak
        )

        if answer == question[2]:
            print("\nCorrect!")
            correct += 1
            streak += 1
            points = 10

            if streak >= 3:
                points += 5
                print("Streak bonus! +5 points")

            score += points
            print("You earned", points, "points!")

            if streak > best_streak:
                best_streak = streak
        else:
            print("\nWrong answer!")
            print("Correct answer:", question[2])
            wrong += 1
            streak = 0

        results.append((question[0], answer, question[2]))
        time.sleep(0.5)

    elapsed = round(time.time() - start_time, 1)
    percentage = correct / len(questions) * 100

    line()
    print("            FINAL RESULTS")
    line()
    print("Difficulty:", difficulty)
    print("Questions answered:", len(questions))
    print("Correct answers:", correct)
    print("Wrong answers:", wrong)
    print("Accuracy:", round(percentage, 1), "%")
    print("Points earned:", score)
    print("Best streak:", best_streak)
    print("Time taken:", elapsed, "seconds")

    if percentage == 100:
        print("\nPerfect score! You got every question right!")
    elif percentage >= 80:
        print("\nAmazing job! You really know your stuff.")
    elif percentage >= 60:
        print("\nGood work! You did pretty well.")
    elif percentage >= 40:
        print("\nNot bad. A little more practice will help.")
    else:
        print("\nKeep practicing and see if you can do better!")

    print("\nWould you like to review your answers?")
    review = input("Enter yes or no: ").strip().lower()

    if review in ["yes", "y"]:
        for question, answer, correct_answer in results:
            print("\n" + question)
            print("Your answer:", answer)
            print("Correct answer:", correct_answer)

    return score, correct, len(questions), elapsed

def show_statistics(games, total_correct, total_questions, best_score):
    line()
    print("             GAME STATISTICS")
    line()

    print("Games played:", games)
    print("Total correct answers:", total_correct)
    print("Total questions answered:", total_questions)
    print("Highest points in one game:", best_score)

    if total_questions > 0:
        accuracy = total_correct / total_questions * 100
        print("Overall accuracy:", round(accuracy, 1), "%")
    else:
        print("Play a game to start your statistics!")

    line()

def main():
    games = 0
    total_correct = 0
    total_questions = 0
    best_score = 0

    welcome()

    while True:
        print("\nMAIN MENU")
        print("1. Play Quiz")
        print("2. View Statistics")
        print("3. How to Play")
        print("4. Quit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            score, correct, total, elapsed = play_quiz()

            games += 1
            total_correct += correct
            total_questions += total

            if score > best_score:
                best_score = score

            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            show_statistics(
                games, total_correct, total_questions, best_score
            )
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            line()
            print("HOW TO PLAY")
            line()
            print("Choose a difficulty and number of questions.")
            print("Answer each question with A, B, C, or D.")
            print("Correct answers earn 10 points.")
            print("Three or more correct answers in a row")
            print("give you 5 bonus points per correct answer.")
            print("Try to get the highest score possible!")
            line()
            input("\nPress Enter to return to the menu...")

        elif choice == "4":
            print("\nThanks for playing the Quiz Challenge!")

            if games > 0:
                print("You played", games, "game(s).")
                print("Your best score was", best_score, "points.")

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
