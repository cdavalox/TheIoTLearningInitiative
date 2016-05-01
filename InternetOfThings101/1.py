# Import standard python modules.
import random
import sys
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient


# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = '326bc24efa304c23a60363748e1f6d86'
ADAFRUIT_IO_USERNAME = 'cdavalox'  # See https://accounts.adafruit.com
                                                    # to find your username.


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print 'Connected to Adafruit IO!  Listening for DemoFeed changes...'
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe('DemoFeed')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print 'Feed {0} received new value: {1}'.format(feed_id, payload)


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.  

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()
# Now send new values every 4 seconds.
print 'Publishing a new message every 4 seconds (press Ctrl-C to quit)...'
while True:
    value = random.randint(0, 100)
    print 'Publishing {0} to DemoFeed.'.format(value)
    client.publish('DemoFeed', value)
    time.sleep(4)

