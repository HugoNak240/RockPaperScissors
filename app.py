from ExternalFiles import classTest
from ExternalFiles import GameFunctions
# Entry or Home page
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("<              Welcome~~!                >")
print("<                 TO                     >")
print("<         Rock Paper Scissors            >")
print("<                Game                    >")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Score Key - You : Computer")

# Call game function from external file
GameFunctions.rockPaperScissors(classTest.player, classTest.bot)
