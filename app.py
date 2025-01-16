from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoSuchTableError
from dotenv import load_dotenv
import os
from datetime import datetime

# To Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# this is the Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Reflects database tables
with app.app_context():
    db.metadata.reflect(bind=db.engine)

@app.route('/nexus6', methods=['GET'])
def get_all_records():
    try:
        table = db.metadata.tables['nexus6']
        query = db.session.execute(table.select()).mappings().all()
        results = [dict(row.items()) for row in query]
        return jsonify(results), 200
    except KeyError:
        return jsonify({"error": "Table 'nexus6' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/nexus6/<int:record_id>', methods=['GET'])
def get_record_by_id(record_id):
    try:
        table = db.metadata.tables['nexus6']
        query = db.session.execute(table.select().where(table.c.id == record_id)).mappings().one_or_none()
        if not query:
            return jsonify({"error": "Record not found", "time": datetime.utcnow().isoformat()}), 404
        return jsonify(dict(query.items())), 200
    except KeyError:
        return jsonify({"error": "Table 'nexus6' not found", "time": datetime.utcnow().isoformat()}), 404
    except Exception as e:
        return jsonify({"error": str(e), "time": datetime.utcnow().isoformat()}), 400

@app.route('/nexus6', methods=['POST'])
def create_record():
    try:
        table = db.metadata.tables['nexus6']
        new_data = request.get_json()
        insert_statement = table.insert().values(new_data)
        db.session.execute(insert_statement)
        db.session.commit()
        new_data["time"] = datetime.utcnow().isoformat()
        return jsonify({"record_created": new_data}), 201
    except KeyError:
        return jsonify({"error": "Table 'nexus6' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/nexus6/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    try:
        table = db.metadata.tables['nexus6']
        updated_data = request.get_json()
        update_statement = table.update().where(table.c.id == record_id).values(updated_data)
        result = db.session.execute(update_statement)
        db.session.commit()
        if result.rowcount == 0:
            return jsonify({"error": "Record not found"}), 404
        updated_data["time"] = datetime.utcnow().isoformat()
        return jsonify({"record_updated": updated_data}), 200
    except KeyError:
        return jsonify({"error": "Table 'nexus6' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/nexus6/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    try:
        table = db.metadata.tables['nexus6']
        delete_statement = table.delete().where(table.c.id == record_id)
        result = db.session.execute(delete_statement)
        db.session.commit()
        if result.rowcount == 0:
            return jsonify({"error": "Record not found"}), 404
        return jsonify({"message": "Record deleted successfully", "time": datetime.utcnow().isoformat()}), 200
    except KeyError:
        return jsonify({"error": "Table 'nexus6' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False').lower() == 'true')