from flask import Flask, render_template, redirect, abort, request

from database import read_all_flats, read_flat, get_flat_count, delete_flat

app = Flask(__name__)


@app.template_filter()
def format_price(price):
    """Returns formatted price value.

    :param price: String with flat price.
    :return: Formatted price value
    """
    return f'{float(price):,.0f} zł'.replace(',', ' ') if price else '???'


@app.route('/')
def index():
    """Redirects to otodom flat offers first page.

    :return: Redirect to otodom flat offers first page.
    """
    return redirect('/ot/1')


@app.route('/ot/<int:page_num>')
def show_all_flats_ot(page_num, flats_per_page=20):
    """Returns otodom flat offers pages with pagination.

    :param page_num: Flat offers page number.
    :param flats_per_page: Flat offers number per page.
    :return: Flat offers page or abort error.
    """
    last_page = get_flat_count() // flats_per_page + 1
    if page_num < 1 or page_num > last_page:
        return abort(404)

    pages = {'previous': page_num-1, 'current': page_num, 'next': page_num+1, 'last': last_page}
    return render_template('flats_ot.html',
                           offers=read_all_flats(flats_per_page, page_num, request.args.get('sort')),
                           pages=pages)


@app.route('/gt/<int:page_num>')
def show_all_flats_gt(page_num, flats_per_page=20):
    """Returns gumtree flat offers pages with pagination.

    :param page_num: Flat offers page number.
    :param flats_per_page: Flat offers number per page.
    :return: Flat offers page or abort error.
    """
    last_page = get_flat_count(oto=False) // flats_per_page + 1
    if page_num < 1 or page_num > last_page:
        return abort(404)

    pages = {'previous': page_num-1, 'current': page_num, 'next': page_num+1, 'last': last_page}
    return render_template('flats_gt.html',
                           offers=read_all_flats(flats_per_page, page_num, request.args.get('sort'), oto=False),
                           pages=pages)


@app.route('/ot/id/<int:flat_id>')
def show_flat_ot(flat_id):
    """Returns otodom flat offer page based on ID from URL.

    :param flat_id: Flat offer ID.
    :return: Single flat offer page or abort error.
    """
    if read_flat(flat_id)[0] is None:
        return abort(404)

    record = read_flat(flat_id)
    timestamped = zip(*(record[0][ts] for ts
                        in ('scraped_date', 'price', 'price_pm', 'added_date', 'updated_date')))
    return render_template('flats_ot.html',
                           offers=record,
                           pages=None,
                           timestamped=timestamped)


@app.route('/gt/id/<int:flat_id>')
def show_flat_gt(flat_id):
    """Returns gumtree flat offer page based on ID from URL.

    :param flat_id: Flat offer ID.
    :return: Single flat  offer page or abort error.
    """
    if read_flat(flat_id, oto=False)[0] is None:
        return abort(404)

    record = read_flat(flat_id, oto=False)
    return render_template('flats_gt.html',
                           offers=record,
                           pages=None)


@app.route('/id', methods=['POST'])
def show_flat_post():
    """Returns flat offer page based on ID from search box.

    :return: Single flat  offer page or abort error.
    """
    flat_id = int(request.form['id'])

    if read_flat(flat_id)[0] is not None:
        return show_flat_ot(flat_id)
    elif read_flat(flat_id, oto=False)[0] is not None:
        return show_flat_gt(flat_id)
    else:
        return abort(404)


@app.route('/delete/<int:flat_id>')
def remove_flat(flat_id):
    """Deletes flat offer record based on given ID.

    :param flat_id: Flat offer ID.
    :return: HTTP no content acknowledgment.
    """
    if read_flat(flat_id)[0] is not None:
        delete_flat(flat_id)
    else:
        delete_flat(flat_id, oto=False)

    return '', 204


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
