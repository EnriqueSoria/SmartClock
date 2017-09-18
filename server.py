from bottle import Bottle, run, request

from utils.BulbArray import BulbArray
from utils.Enumerations import LightParameters, NotificationParameters, SensorParameters, SensorTypes

app = Bottle()
bulbs = BulbArray(timeout=3)


@app.route('/light')
def light():
    print(request.query.index)
    state = {
        param.value: request.query.get(param.value) for param in LightParameters if request.query.get(param.value)
    }

    index = state.get("index", -1)
    print((state, index))

    keys = state.keys()
    print(keys)

    if LightParameters.REFRESH.value in keys:
        global bulbs
        bulbs = BulbArray(timeout=3)
        return "connected" if bulbs is not None else "failed"

    if LightParameters.BRIGHT.value in keys:
        print("bright")
        bulbs.set_brightness(state[LightParameters.BRIGHT], bulb_index=index)

    if (LightParameters.R.value in keys
            or LightParameters.G.value in keys
            or LightParameters.B.value in keys):
        bulbs.set_rgb(
            r=state.get(LightParameters.R.value, None),
            g=state.get(LightParameters.G.value, None),
            b=state.get(LightParameters.B.value, None),
            bulb_index=index
        )

    if LightParameters.TEMP.value in keys:
        bulbs.set_color_temp(color_temp=state.get(LightParameters.TEMP,None))

    if LightParameters.ON.value in keys:
        bulbs.power(on_off=state.get(LightParameters.ON))

    if LightParameters.STATE.value in keys:
        response = ""
        for bulb in bulbs.bulbs:
            response += str(bulb.get_properties()) + "<br />\n"
        return response

    return "Success"


@app.route('/notification')
def notifications():
    print(request.query.index)
    state = {
        param: request.query.get(param) for param in LightParameters if request.query.get(param)
        }

    index = state.get("index", -1)
    print((state, index))

    keys = state.keys()


@app.route('/sensor')
def sensor():
    index = request.GET.index if SensorParameters.INDEX.value in request.GET else -1

    if SensorParameters.TYPE.value in request.GET:
        print(request.GET.type)

        if SensorTypes.TEMPERATURE.value == request.GET.type:
            if SensorParameters.VALUE.value in request.GET:
                # TODO: do something with temperature
                # TODO: check if value is a number between an upper and lower limit
                temperature_value = request.GET.value
            else:
                # TODO: return an error saying there is no temperature
                pass
        # TODO: add more sensors


if __name__ == "__main__":
    run(
        app,
        host='0.0.0.0',
        port=8080,
        debug=True
    )
