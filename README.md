# Flask_Hbase 
since I can not find a extension for Flask to accees hbase. So I decided to write one by myself. The code mainly use happybase and the extension. and the the code structure I refer from flask_pymongo.

# How to use

    from flask_hbase import FlaskHbase
    import json

    hbase_inst = FlaskHbase()

    app = Flask(__name__)
    hbase_inst.init_app(app, config_prefix="HBASE")

    @app.route("/show_tables")
    def table_list():
        with hbase_inst.conn_from_pool as conn:
            table_list = conn.tables()
        return make_response(json.dumps(result))
        
if you want know more usage of happybase such as filter and scan, please see the document of happybase.
Notice: since we use happybase threads pool, so set the timeout of hbase thrift client as long as possible.
