from flask import Flask, request, render_template, redirect, url_for
from worker import video_link_parser, ip_info

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['button'].title())

        if request.form['button'] == 'first':
            return redirect(url_for('downloader'))

    return render_template('index.html')


@app.route('/downloader', methods=['GET', 'POST'])
def downloader():
    if request.method == 'POST':
        url = request.form['searched-link']

        return redirect(url_for('result', url=url))
    else:
        return render_template('downloader.html')


@app.route('/result', methods=['GET', 'POST'])
def result():

    if request.method == 'POST':
        return redirect('downloader')   # render_template('downloader.html')

    url = request.args.get('url')
    geo_information = ip_info()
    print(geo_information['ip'], geo_information['country'], geo_information['city'])

    parsed = video_link_parser(url)
    print('Parsed length:', len(parsed))

    parsed = parsed if len(parsed) == 3 else 'NO'

    return render_template('result.html', data=parsed)


@app.errorhandler(404)
def page_not_found(e):
    print('error:', e)

    return render_template('404.html')
