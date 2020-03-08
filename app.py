from flask import Flask, render_template, redirect, abort, request

from database import read_all_flats, read_flat, get_flat_count, delete_flat

app = Flask(__name__)


@app.template_filter()
def format_price(price):
    """Returns formatted price value."""
    if price:
        return f'{float(price):,.0f} zł'.replace(',', ' ')
    return '???'


@app.route('/')
def index():
    """Redirects to first page of all flat list."""
    return redirect('/1')


@app.route('/<int:page_num>')
def show_all_flats(page_num, flats_per_page=20):
    """Shows all flat records with pagination"""
    last_page = get_flat_count() // flats_per_page + 1
    if page_num < 1 or page_num > last_page:
        return abort(404)  # TODO fix pycharm warnings - read about flask support
    pages = {'current': page_num, 'last': last_page}  # TODO reformat functions
    return render_template('all_flors.html',
                           offers=read_all_flats(flats_per_page, page_num, request.args.get('sort')), pages=pages)
# TODO fix error page when flat id is incorrect


@app.route('/gt/<int:page_num>')
def show_all_flats_gt(page_num, flats_per_page=20):
    """Shows all flat records with pagination"""
    last_page = get_flat_count(oto=False) // flats_per_page + 1
    if page_num < 1 or page_num > last_page:
        return abort(404)
    pages = {'current': page_num, 'last': last_page}
    return render_template('all_flors_gt.html',
                           offers=read_all_flats(flats_per_page, page_num, request.args.get('sort'), oto=False), pages=pages)


@app.route('/id/<int:flat_id>')
def show_flat(flat_id):
    """Shows one flat record with given flat_id."""
    record = read_flat(flat_id)
    timestamped = ('scraped_date', 'price', 'price_pm', 'added_date', 'updated_date')
    pages = {'current': 1, 'last': 1}
    return render_template('one_flor.html',
                           offers=record, timestamped=zip(*(record[0][ts] for ts in timestamped)), pages=pages)


@app.route('/delete/<int:flat_id>')
def remove_flat(flat_id):
    """Deletes one flat record with given flat_id."""
    delete_flat(flat_id)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
