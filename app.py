from flask import Flask, render_template, redirect

from database import read_all_flats, read_flat

app = Flask(__name__)


@app.template_filter()
def format_price(price):
    """Returns formatted price value."""
    return f'{float(price):,.0f} zł'.replace(',', ' ')

@app.route('/')
def index():
    """Redirects to first page of all flat list."""
    return redirect('/1')


@app.route('/<int:page_num>')
def show_all_flats(page_num):
    """Shows all flat records - 10 per page."""
    return render_template('all_flors.html',
                           offers=read_all_flats(10, page_num))


@app.route('/id/<int:flat_id>')
def show_flat(flat_id):
    """Shows one flat record with given flat_id."""
    return render_template('one_flor.html',
                           offers=read_flat(flat_id))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
