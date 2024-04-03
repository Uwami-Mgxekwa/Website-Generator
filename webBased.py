from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__, static_url_path='/static')

def generate_html(title, content, color_scheme, nav_items, footer_text, css_file_path=None, js_file_path=None, inline_js=None):
    css_styles = {
        "default": """
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }
            header {
                background-color: #333;
                color: #fff;
                padding: 20px 0;
                text-align: center;
                animation: fadeInDown 1s ease-out;
            }
            h1 {
                font-size: 36px;
                margin-bottom: 10px;
            }
            nav {
                margin-bottom: 20px;
                animation: fadeInUp 1s ease-out;
            }
            nav ul {
                list-style-type: none;
                padding: 0;
            }
            nav li {
                display: inline;
                margin-right: 20px;
            }
            nav li a {
                color: #fff;
                text-decoration: none;
                transition: color 0.3s;
            }
            nav li a:hover {
                color: #007bff;
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                animation: fadeIn 1s ease-out;
            }
            h2 {
                font-size: 24px;
                margin-bottom: 10px;
            }
            p {
                line-height: 1.6;
                margin-bottom: 20px;
            }
            footer {
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 20px 0;
                animation: fadeInUp 1s ease-out;
            }
            .logo {
                display: block;
                margin: 30px auto;
                width: 200px;
                animation: bounceIn 1s ease-out;
            }
            @keyframes fadeInDown {
                from {
                    opacity: 0;
                    transform: translateY(-50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
            @keyframes bounceIn {
                from,
                20%,
                40%,
                60%,
                80%,
                to {
                    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
                    transform: translate3d(0, 0, 0);
                }
                0% {
                    opacity: 0;
                    transform: scale3d(0.3, 0.3, 0.3);
                }
                20% {
                    transform: scale3d(1.1, 1.1, 1.1);
                }
                40% {
                    transform: scale3d(0.9, 0.9, 0.9);
                }
                60% {
                    opacity: 1;
                    transform: scale3d(1.03, 1.03, 1.03);
                }
                80% {
                    transform: scale3d(0.97, 0.97, 0.97);
                }
                to {
                    opacity: 1;
                    transform: scale3d(1, 1, 1);
                }
            }
        """,
        "dark": """
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #222;
                color: #ccc;
            }
            header {
                background-color: #111;
                color: #fff;
                padding: 20px 0;
                text-align: center;
                animation: fadeInDown 1s ease-out;
            }
            h1 {
                font-size: 36px;
                margin-bottom: 10px;
            }
            nav {
                margin-bottom: 20px;
                animation: fadeInUp 1s ease-out;
            }
            nav ul {
                list-style-type: none;
                padding: 0;
            }
            nav li {
                display: inline;
                margin-right: 20px;
            }
            nav li a {
                color: #ccc;
                text-decoration: none;
                transition: color 0.3s;
            }
            nav li a:hover {
                color: #007bff;
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
                background-color:
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
                animation: fadeIn 1s ease-out;
            }
            h2 {
                font-size: 24px;
                margin-bottom: 10px;
            }
            p {
                line-height: 1.6;
                margin-bottom: 20px;
            }
            footer {
                background-color: #111;
                color: #ccc;
                text-align: center;
                padding: 20px 0;
                animation: fadeInUp 1s ease-out;
            }
            .logo {
                display: block;
                margin: 30px auto;
                width: 200px;
                animation: bounceIn 1s ease-out;
            }
            @keyframes fadeInDown {
                from {
                    opacity: 0;
                    transform: translateY(-50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
            @keyframes bounceIn {
                from,
                20%,
                40%,
                60%,
                80%,
                to {
                    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
                    transform: translate3d(0, 0, 0);
                }
                0% {
                    opacity: 0;
                    transform: scale3d(0.3, 0.3, 0.3);
                }
                20% {
                    transform: scale3d(1.1, 1.1, 1.1);
                }
                40% {
                    transform: scale3d(0.9, 0.9, 0.9);
                }
                60% {
                    opacity: 1;
                    transform: scale3d(1.03, 1.03, 1.03);
                }
                80% {
                    transform: scale3d(0.97, 0.97, 0.97);
                }
                to {
                    opacity: 1;
                    transform: scale3d(1, 1, 1);
                }
            }
        """
    }

    # Choose CSS style based on color scheme
    css_style = css_styles.get(color_scheme, css_styles["default"])

    # HTML template with dynamic content
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>{css_style}</style>
    </head>
    <body>
        <header>
            <h1>{title}</h1>
            <nav>
                <ul>
                    {''.join(f"<li><a href='#'>{item.strip()}</a></li>" for item in nav_items)}
                </ul>
            </nav>
        </header>
        <div class="container">
            <h2>Welcome to our Website!</h2>
            <p>{content}</p>
        </div>
        <footer>
            <p>{footer_text}</p>
            <img src="logo.png" alt="ByteBlitz Technologies" class="logo">
        </footer>
    </body>
    </html>
    """

    return html_template


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        color_scheme = request.form['color_scheme']
        nav_items = request.form['nav_items'].split(',')
        footer_text = request.form['footer_text']
        css_file_path = request.form['css_file_path']
        js_file_path = request.form['js_file_path']
        inline_js = request.form['inline_js']

        html_content = generate_html(title, content, color_scheme, nav_items, footer_text, css_file_path, js_file_path, inline_js)

        file_stream = io.BytesIO(html_content.encode())
        file_stream.seek(0)

        return send_file(file_stream, as_attachment=True, download_name='generated_website.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
