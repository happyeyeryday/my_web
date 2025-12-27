from flask import Flask, Blueprint, render_template

# --- 创建蓝图 ---
# 蓝图就像一个应用中的“子应用”或模块
# 'my_web' 是蓝图的名字，可以随便起
# __name__ 是必需的参数
# template_folder='templates' 告诉蓝图，它的模板在同级的 'templates' 文件夹里
# static_folder='static' 告诉蓝图，它的静态文件在同级的 'static' 文件夹里
web_bp = Blueprint('my_web', __name__,
                   template_folder='templates',
                   static_folder='static')

# --- 在蓝图上定义路由 ---
# 注意这里用的是 @web_bp.route('/') 而不是 @app.route('/')
@web_bp.route('/')
def home():
    # render_template 会自动在蓝图指定的 template_folder ('templates') 里找文件
    return render_template('index.html')

# --- 创建主应用并注册蓝图 ---
app = Flask(__name__)

# 将我们创建的 web_bp 蓝图注册到主应用 app 上
# url_prefix='/' 表示访问网站根目录时，就交由这个蓝图处理
app.register_blueprint(web_bp, url_prefix='/')


# --- 启动服务器 ---
if __name__ == '__main__':
    # 启动Web服务器，打开调试模式
    app.run(debug=True)