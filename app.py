import sqlite3
import io
import qrcode
from flask import Flask, jsonify, request, send_file, render_template, Blueprint
from flask_cors import CORS

DATABASE_FILE = 'database.db'
def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    CORS(app)

    api_bp = Blueprint('api', __name__, url_prefix='/api')
    main_bp = Blueprint('main', __name__)

    @main_bp.route('/')
    def public_page():
        return render_template('index.html')

    @main_bp.route('/admin')
    def admin_page():
        return render_template('admin.html')

    @api_bp.route('/links', methods=['GET'])
    def get_links():
        with get_db_connection() as conn:
            links_rows = conn.execute('SELECT * FROM links ORDER BY position ASC').fetchall()
            return jsonify([dict(row) for row in links_rows])

    @api_bp.route('/click/<int:link_id>', methods=['POST'])
    def record_click(link_id):
        with get_db_connection() as conn:
            conn.execute("UPDATE links SET clicks = clicks + 1 WHERE id = ?", (link_id,))
            conn.commit()
        return '', 204

    @api_bp.route('/links/add', methods=['POST'])
    def add_link():
        data = request.get_json()
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COALESCE(MAX(position), -1) + 1 FROM links")
            position = cursor.fetchone()[0]
            cursor.execute("INSERT INTO links (title, url, position, thumbnail_url) VALUES (?, ?, ?, ?)",
                           (data['title'], data['url'], position, data.get('thumbnail_url')))
            new_id = cursor.lastrowid
            conn.commit()
        return jsonify({'id': new_id, **data, 'clicks': 0, 'position': position}), 201

    @api_bp.route('/links/<int:link_id>', methods=['PUT'])
    def update_link(link_id):
        data = request.get_json()
        with get_db_connection() as conn:
            conn.execute("UPDATE links SET title = ?, url = ?, thumbnail_url = ? WHERE id = ?",
                         (data['title'], data['url'], data.get('thumbnail_url'), link_id))
            conn.commit()
        return jsonify({'id': link_id, **data})

    @api_bp.route('/links/<int:link_id>', methods=['DELETE'])
    def delete_link(link_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM links WHERE id = ?", (link_id,))
            conn.commit()
        return '', 204

    @api_bp.route('/chart-data', methods=['GET'])
    def get_chart_data():
        with get_db_connection() as conn:
            links_rows = conn.execute('SELECT title, clicks FROM links ORDER BY position ASC').fetchall()
            chart_data = {
                'labels': [row['title'] for row in links_rows],
                'data': [row['clicks'] for row in links_rows]
            }
        return jsonify(chart_data)

    @api_bp.route('/links/update-order', methods=['POST'])
    def update_link_order():
        ordered_ids = request.get_json()
        with get_db_connection() as conn:
            for index, link_id in enumerate(ordered_ids):
                conn.execute("UPDATE links SET position = ? WHERE id = ?", (index, int(link_id)))
            conn.commit()
        return jsonify({'success': True})

    @api_bp.route('/qrcode')
    def generate_qrcode():
        public_url = request.host_url
        img_buffer = io.BytesIO()
        qrcode.make(public_url).save(img_buffer, 'PNG')
        img_buffer.seek(0)
        return send_file(img_buffer, mimetype='image/png')
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)