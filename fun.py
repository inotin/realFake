import random
import math
from IPython.display import clear_output

def funfacts():
    lst = ["Cats can produce over one hundred vocal sounds, while dogs can only produce about ten.",
    "Banging your head against a wall for one hour burns 150 calories.",
    "In Switzerland it is illegal to own just one guinea pig.",
    "Pteronophobia is the fear of being tickled by feathers.",
    "Snakes can help predict earthquakes.",
    "7 percent of American adults believe that chocolate milk comes from brown cows.",
    "If you lift a kangaroo’s tail off the ground it can’t hop.",
    "Bananas are curved because they grow towards the sun.",
    "Billy goats urinate on their own heads to smell more attractive to females.",
    "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
    "During your lifetime, you will produce enough saliva to fill two swimming pools.",
    "If Pinocchio says “My Nose Will Grow Now”, it would cause a paradox.",
    "Polar bears could eat as many as 86 penguins in a single sitting…",
    "Movie trailers were originally shown after the movie, which is why they were called “trailers”.",
    "The United States Navy has started using Xbox controllers for their periscopes.",
    "The average male gets bored of a shopping trip after 26 minutes.",
    "In the 16th Century, Turkish women could initiate a divorce if their husbands didn’t pour coffee for them.",
    "After the premiere of “16 and Pregnant,” teen pregnancy rates dropped.",
    "Approximately 10-20 percent of U.S. power outages are caused by squirrels.",
    "A swarm of 20,000 bees followed a car for two days because their queen was stuck inside.",
    "Sea otters hold hands when they sleep so they don’t drift away from each other.",
    "Los Angeles’s full name is “El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula.",
    "The Twitter bird actually has a name – Larry.",
    "Mike Tyson once offered a zoo attendant 10,000 dollars to let him fight a gorilla.",
    "Dying is illegal in the Houses of Parliaments.",
    "An apple, potato, and onion all taste the same if you eat them with your nose plugged.",
    "41% of the moon is not visible from earth at any time.",
    "In space, astronauts can’t cry properly because of the zero gravity.",
    "Mars appears red because it’s covered in rust.",
    "The longest possible eclipse of the sun is 7.31 minutes.",
    "Our solar system was formed more than 4 billion years ago.",
    "The sun looks 1600 times fainter from the pluto than it does from the earth.",
    "Saturn’s rings are made up of particles of ice, dust and rock. Some particles are as small as grains of sand while others are much larger than skyscrapers.",
    "Some large asteroids even have their own moon.",
    "Halley’s Comet appears about every 76 years.",
    "One million, million, million, million, millionth of a second after the Big Bang, the universe was the size of a pea.",
    "The Universe contains over 100 billion galaxies.",
    "The risk of being struck by a falling meteorite for a human is one occurrence every 9,300 years.",
    "It takes 8 minutes 17 seconds for the light to travel from the Sun’s surface to the Earth.",
    "Every hour the Universe expands by a billion miles in all directions.",
    "Even travelling at the speed of light it would take 2 million years to reach the nearest large galaxy, Andromeda.",
    "The largest galaxies contain nearly 400 billion stars.",
    "A thimbleful of a neutron star would weigh over 100 million.",
    "The International Space Station orbits at 248 miles above the Earth.",
    "The interstellar gas cloud Sagittarius B contains a billion, billion, billion litres of alcohol.",
    "The Temperature on the surface of Mercury exceeds 430 degrees Celsius during the day and at night reaches up to minus 180 degrees.",
    "99% of the solar system’s mass is concentrated in the sun.",
    "The Earth is 4.56 billion years old, the same age as the Moon and the Sun.",
    "If our Sun was just an inch in diameter, the nearest star would be 445 miles away.",
    "Golf the only sport played on the moon – on 6 February 1971, Alan Shepard hit a golf ball.",
    "In the whole solar system, our home planet is the only one not named after a God.",
    "Earth and Mercury are the two most dense planets in the Solar System.",
    "From a distance, Earth would be the brightest of the planets. This is because sunlight is reflected off the planet’s water.",
    "Light from the Earth takes just 1.255 seconds to reach the Moon.",
    "Twelve people have walked on the moon.",
    "The visual “tail” of a comet has nothing to do with its direction of travel; rather, the solar wind pushes it so that it always points away from the Sun.",
    "Jupiter is larger than 1,000 Earths.",
    "The orbits of most asteroids lie partially between the orbits of Mars and Jupiter.",
    "Asteroids are believed to be ancient remnants of the formation of our solar system.",
    "The most dangerous asteroids, those capable of causing major regional or global disasters, usually impact the earth only once every 100,000 years on average.",
    "There are over 20 million observable meteors per day.",
    "Only 1 or 2 meteors reach the surface of earth per day.",
    "The largest found meteorite was found in Hoba, Namibia. It weighed 60 tonnes.",
    "There are over 100 billion galaxies in the universe.",
    "Europa, Jupiter’s moon is completely covered with ice.",
    "There has only been 1 satellite destroyed by a meteor, it was the European Space Agency’s Olympus in 1993.",
    "Light-reflecting off the moon takes 1.2822 seconds to reach earth."]

    print("The more you know...", random.choice(lst))

def funProgressBar(fraction, total, previous, step = 10):
    current = fraction/total
    
    if step <=0 or step>=100:
        step = 10
    probOfFact = max(math.log10(step)/2, 0.25)

    st = total / (100/step)

    if current != previous and round(current % st) == 0:
        clear_output(wait=True)
        print("["+'{:_<20}'.format("*"*round(current * 20))+"]")
        print(f"{round(current * 100)}% COMPLETED")
        
        if random.random() <= probOfFact:
            print("In case you're bored waiting:")
            funfacts()
        
    return current