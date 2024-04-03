def generate_html(title, content, color_scheme):
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
        """
    }

    css_style = css_styles.get(color_scheme, css_styles["default"])

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            {css_style}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            <p>{content}</p>
        </div>
    </body>
    </html>
    """
    return html_template

def save_html(html_content, file_name):
    if not file_name.endswith(".html"):
        file_name += ".html"
    with open(file_name, "w") as file:
        file.write(html_content)

def main():
    title = input("Enter the title of the website: ")
    content = input("Enter the content of the website: ")
    color_scheme = input("Choose a color scheme (default/dark): ")
    file_name = input("Enter the name of the HTML file to save (without the extension): ")

    html_content = generate_html(title, content, color_scheme)
    save_html(html_content, file_name)
    print(f"HTML file '{file_name}.html' generated successfully!")

if __name__ == "__main__":
    main()
