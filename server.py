from bottle import Bottle, run, request

from utils.BulbArray import BulbArray
from utils.Enumerations import LightParameters

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


if __name__ == "__main__":
    run(
        app,
        host='0.0.0.0',
        port=8080,
        debug=True
    )
