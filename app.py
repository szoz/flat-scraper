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
    return redirect('/ot/1')


@app.route('/ot/<int:page_num>')
def show_all_flats(page_num, flats_per_page=20):
    """Shows all flat records with pagination"""
    last_page = get_flat_count() // flats_per_page + 1
    if page_num < 1 or page_num > last_page:
        return abort(404)  # TODO fix pycharm warnings - read about flask support
    pages = {'previous': page_num-1, 'current': page_num, 'next': page_num+1,'last': last_page}
    return render_template('all_flats.html',
                           offers=read_all_flats(flats_per_page, page_num, request.args.get('sort')), pages=pages)


@app.route('/gt/<int:page_num>')
def show_all_flats_gt(page_num, flats_per_page=20):
    """Shows all flat records with pagination"""
    last_page = get_flat_count(oto=False) // flats_per_page + 1
    if page_num < 1 or page_num > last_page:
        return abort(404)
    pages = {'previous': page_num-1, 'current': page_num, 'next': page_num+1,'last': last_page}
    return render_template('all_flats_gt.html',
                           offers=read_all_flats(flats_per_page, page_num, request.args.get('sort'), oto=False), pages=pages)


@app.route('/ot/id/<int:flat_id>')
def show_flat_ot(flat_id):
    """Shows one otodom flat record with given flat_id."""
    if read_flat(flat_id)[0] is not None:
        record = read_flat(flat_id)
        timestamped = zip(*(record[0][ts] for ts in ('scraped_date', 'price', 'price_pm', 'added_date', 'updated_date')))
        return render_template('one_flat.html', offers=record, pages=None, timestamped=timestamped)
    else:
        return abort(404)


@app.route('/gt/id/<int:flat_id>')
def show_flat_gt(flat_id):
    """Shows one gumtree flat record with given flat_id."""
    if read_flat(flat_id, oto=False)[0] is not None:
        record = read_flat(flat_id, oto=False)
        return render_template('all_flats_gt.html', offers=record, pages=None)
    else:
        return abort(404)


@app.route('/id', methods=['POST'])
def show_flat_post():
    """Shows one flat record based on flat_id sent in form."""
    # return redirect(f'/id/{request.form["id"]}')
    flat_id = int(request.form["id"])
    if read_flat(flat_id)[0] is not None:
        return show_flat_ot(flat_id)
    elif read_flat(flat_id, oto=False)[0] is not None:
        return show_flat_gt(flat_id)
    else:
        return abort(404)


@app.route('/delete/<int:flat_id>')
def remove_flat(flat_id):
    """Deletes one flat record with given flat_id."""
    if read_flat(flat_id)[0] is not None:
        delete_flat(flat_id)
    else:
        delete_flat(flat_id, oto=False)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
