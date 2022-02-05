from flask import Flask, render_template, request
from main_utils import *

app = Flask(__name__)


@app.route('/')
def request_proc():
    """
    Processing the request and
        - returning a available image and updating number of shows
        OR
        - returning a 204 error if there is no available image
    """
    req_cat = get_cat(request.args, cats)
    response = get_object_to_show(req_cat, cats_max_show, cats, objects_power)

    if int(objects_num_show[response]) > 0:
        objects_num_show[response] = int(objects_num_show[response]) - 1

        for key in cats:
            temp = str(cats[key]).split('&')
            N = 0
            for k in temp:
                N = N + int(objects_num_show[k])
            cats_max_show[key] = N

        objects_power[response] = int(objects_num_show[response]) * int(objects_num_cat[response])
        return render_template('index.html', pict=f'{response}.png')
    else:
        return ('', 204)


if __name__ == '__main__':

    cats, cats_max_show, objects_num_show, objects_power, objects_num_cat = proc_csv()

    app.run(host='127.0.0.1', port='8000')
