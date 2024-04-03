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
            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
            }
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                background-color: #333;
                overflow: hidden;
            }
            nav li {
                float: left;
            }
            nav li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px;
            }
        """,
        "dark": """
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #333;
                color: #fff;
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
                background-color: #222;
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
            }
            h1 {
                color: #fff;
            }
            p {
                color: #ccc;
            }
            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                background-color: #111;
                overflow: hidden;
            }
            nav li {
                float: left;
            }
            nav li a {
                display: block;
                color: #ccc;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }
            footer {
                background-color: #111;
                color: #ccc;
                text-align: center;
                padding: 10px;
            }
        """
    }

    css_style = css_styles.get(color_scheme, css_styles["default"])

    if css_file_path:
        css_link = f"<link rel='stylesheet' href='{css_file_path}'>"
    else:
        css_link = f"<style>{css_style}</style>"

    nav_items_html = "".join([f"<li><a href='#'>{item.strip()}</a></li>" for item in nav_items])

    if js_file_path:
        js_link = f"<script src='{js_file_path}'></script>"
    elif inline_js:
        js_link = f"<script>{inline_js}</script>"
    else:
        js_link = ""

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        {css_link}
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    {nav_items_html}
                </ul>
            </nav>
        </header>
        <main>
            <section>
                <h1>{title}</h1>
                <p>{content}</p>
            </section>
        </main>
        <footer>
            <p>{footer_text}</p>
        </footer>
        {js_link}
    </body>
    </html>
    """

    return html_template

def save_html(html_content, file_name):
    if not file_name.endswith(".html"):
        file_name += ".html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

def main():
    title = input("Enter the title of the website: ")
    content = input("Enter the content of the website: ")
    color_scheme = input("Choose a color scheme (default/dark): ")
    nav_items = input("Enter navigation menu items (comma-separated): ").split(",")
    footer_text = input("Enter footer text: ")
    css_file_path = input("Enter the path to your CSS file (leave blank for default styles): ")
    js_file_path = input("Enter the path to your JavaScript file (leave blank if not needed): ")
    inline_js = input("Enter inline JavaScript code (leave blank if not needed): ")

    html_content = generate_html(title, content, color_scheme, nav_items, footer_text, css_file_path, js_file_path, inline_js)
    file_name = input("Enter the name of the HTML file to save (without the extension): ")
    save_html(html_content, file_name)

    print(f"HTML file '{file_name}.html' generated successfully!")

if __name__ == "__main__":
    main()