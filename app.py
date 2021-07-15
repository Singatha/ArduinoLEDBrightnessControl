from flask import Flask, render_template, request
import pyfirmata
import time

app = Flask(__name__)

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
led = board.get_pin('d:11:p')

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        print(request.form['value'])
        brightness_control(int(request.form['value']))
    return render_template("index.html")


def brightness_control(analog_value):
    while True:
        led.write(analog_value)
        time.sleep(0.1)


if __name__ == '__main__':
    app.run(debug=True)

# What's next
# improve the serial communication
# add the project to your github
