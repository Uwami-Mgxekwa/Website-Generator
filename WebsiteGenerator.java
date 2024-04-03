import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class WebsiteGenerator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the title of the website: ");
        String title = scanner.nextLine();

        System.out.print("Enter the content of the website: ");
        String content = scanner.nextLine();

        System.out.print("Choose a color scheme (default/dark): ");
        String colorScheme = scanner.nextLine();

        System.out.print("Enter the name of the HTML file to save (without the extension): ");
        String fileName = scanner.nextLine() + ".html";

        String htmlContent = generateHtml(title, content, colorScheme);
        saveHtml(htmlContent, fileName);

        System.out.println("HTML file '" + fileName + "' generated successfully!");
        scanner.close();
    }
    

    public static String generateHtml(String title, String content, String colorScheme) {
        String cssStyle;
        if (colorScheme.equals("dark")) {
            cssStyle = "body {\n" +
                    "    font-family: Arial, sans-serif;\n" +
                    "    margin: 0;\n" +
                    "    padding: 0;\n" +
                    "    background-color: #333;\n" +
                    "    color: #fff;\n" +
                    "}\n" +
                    ".container {\n" +
                    "    width: 80%;\n" +
                    "    margin: auto;\n" +
                    "    padding: 20px;\n" +
                    "    background-color: #222;\n" +
                    "    box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);\n" +
                    "}\n" +
                    "h1 {\n" +
                    "    color: #fff;\n" +
                    "}\n" +
                    "p {\n" +
                    "    color: #ccc;\n" +
                    "}";
        } else {
            cssStyle = "body {\n" +
                    "    font-family: Arial, sans-serif;\n" +
                    "    margin: 0;\n" +
                    "    padding: 0;\n" +
                    "    background-color: #f4f4f4;\n" +
                    "    color: #333;\n" +
                    "}\n" +
                    ".container {\n" +
                    "    width: 80%;\n" +
                    "    margin: auto;\n" +
                    "    padding: 20px;\n" +
                    "    background-color: #fff;\n" +
                    "    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);\n" +
                    "}\n" +
                    "h1 {\n" +
                    "    color: #333;\n" +
                    "}\n" +
                    "p {\n" +
                    "    color: #666;\n" +
                    "}";
        }
    
        return String.format(
                "<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                "    <title>%s</title>\n" +
                "    <style>\n" +
                "        %s\n" +
                "    </style>\n" +
                "</head>\n" +
                "<body>\n" +
                "    <div class=\"container\">\n" +
                "        <h1>%s</h1>\n" +
                "        <p>%s</p>\n" +
                "    </div>\n" +
                "</body>\n" +
                "</html>", title, cssStyle, title, content);
    }
    
    

    public static void saveHtml(String htmlContent, String fileName) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(fileName))) {
            writer.println(htmlContent);
        } catch (IOException e) {
            System.err.println("Error occurred while saving HTML file: " + e.getMessage());
        }
    }
}
